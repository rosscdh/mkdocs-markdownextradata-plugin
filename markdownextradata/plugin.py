import os
import sys
import json
import yaml
import mkdocs
from mkdocs.plugins import BasePlugin

from jinja2 import Template
from pathlib import Path
from itertools import chain

CONFIG_KEYS = [
    'site_name',
    'site_author',
    'site_url',
    'repo_url',
    'repo_name'
]

if sys.version_info[0] >= 3:
    str_type = str
else:
    str_type = mkdocs.utils.string_types

class MarkdownExtraDataPlugin(BasePlugin):
    """
    Inject certain config variables into the markdown
    """

    config_scheme = (
        ('data', mkdocs.config.config_options.Type(str_type, default=None)),
    )

    def __add_data__(self, config, namespace, data):
        # creates the namespace and adds the data there
        namespace = ['extra'] + namespace.split(os.sep)
        holder = config
        while len(namespace) > 1:
            if not namespace[0] in holder: holder[namespace[0]] = {}
            holder = holder[namespace[0]]
            del namespace[0]
        holder[namespace[0]] = data

    def on_pre_build(self, config):
        # this loads all data from the supplied data directory, or otherwise a _data directory next to mkdocs.yml or inside the docs_dir. Does nothing if the dir does not exist.

        data = self.config.get('data')
        for datadir in [ os.path.dirname(config['config_file_path']), config['docs_dir'] ]:
            if not data:
                data = os.path.join(datadir, '_data')
                if not os.path.exists(data): data = None

        if data and os.path.exists(data):
            path = Path(data)
            for filename in chain(path.glob('**/*.yml'), path.glob('**/*.json')):
                with open(filename) as f:
                    namespace = os.path.splitext(os.path.relpath(filename, data))[0]
                    self.__add_data__(config, namespace, (yaml.load(f, Loader=yaml.FullLoader) if filename.suffix == '.yml' else json.load(f)))

    def on_page_markdown(self, markdown, config, **kwargs):
        context = {key: config.get(key) for key in CONFIG_KEYS if key in config}
        context.update(config.get('extra', {}))
        extra = config.get('extra')
        md_template = Template(markdown)
        return md_template.render(**extra)
