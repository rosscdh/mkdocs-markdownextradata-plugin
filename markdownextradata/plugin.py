import os
import sys
import json
import yaml
import mkdocs
import logging
from mkdocs.plugins import BasePlugin
from mkdocs.utils import warning_filter

from jinja2 import Template
from pathlib import Path
from itertools import chain

log = logging.getLogger(__name__)
log.addFilter(warning_filter)

CONFIG_KEYS = ["site_name", "site_author", "site_url", "repo_url", "repo_name"]

if sys.version_info[0] >= 3:
    str_type = str
else:
    str_type = mkdocs.utils.string_types


class MarkdownExtraDataPlugin(BasePlugin):
    """
    Inject certain config variables into the markdown
    """

    config_scheme = (
        ("data", mkdocs.config.config_options.Type(str_type, default=None)),
    )

    def __add_data__(self, config, namespace, data):
        # creates the namespace and adds the data there
        namespace = ["extra"] + namespace.split(os.sep)
        holder = config
        while len(namespace) > 1:
            if not namespace[0] in holder:
                holder[namespace[0]] = {}
            holder = holder[namespace[0]]
            del namespace[0]
        holder[namespace[0]] = data

    def on_pre_build(self, config, **kwargs):
        # Loads all data from the supplied data directories
        # or, otherwise a _data directory next to mkdocs.yml and/or inside the docs_dir.
        # Does nothing if the dir does not exist.

        # assume an empty list if not defined
        data_source_folders = self.config.get("data")
        # cast as a list if is defined but is a string
        if isinstance(data_source_folders, str):
            data_source_folders = data_source_folders.split(',')

        # if we have not value, then proceed to look in default folders
        # and assume a _data folder, add to list of folders to check
        if not data_source_folders:
            for datadir in [
                os.path.dirname(config["config_file_path"]),
                config["docs_dir"],
            ]:
                ds_folder = os.path.join(datadir, "_data")
                if os.path.exists(ds_folder):
                    data_source_folders.append(ds_folder)

        if not data_source_folders:
            return

        # iterate of a list of folders and look for data files
        for ds_folder in data_source_folders:
            if os.path.exists(ds_folder):
                path = Path(ds_folder)
                for filename in chain(
                    path.glob("**/*.yaml"),
                    path.glob("**/*.yml"),
                    path.glob("**/*.json"),
                ):
                    namespace = os.path.splitext(os.path.relpath(filename, ds_folder))[0]
                    # add data into dict based on its path as a namespace
                    self.__add_data__(
                        config,
                        namespace,
                        (
                            yaml.load(filename.read_bytes(), Loader=yaml.FullLoader)
                            if filename.suffix in [".yml", ".yaml"]
                            else json.loads(filename.read_bytes())
                        ),
                    )

    def on_page_read_source(self, page, config, **kwargs):
        context = {key: config.get(key) for key in CONFIG_KEYS if key in config}
        context.update(config.get("extra", {}))
        try:
            with open(page.file.abs_src_path, 'r', encoding='utf-8-sig', errors='strict') as f:
                md_template = Template(f.read())
            return md_template.render(**config.get("extra"))
        except OSError:
            log.error('File not found: {}'.format(self.file.src_path))
            raise
        except ValueError:
            log.error('Encoding error reading file: {}'.format(self.file.src_path))
            raise
