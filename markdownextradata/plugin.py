import os
import sys
import json
import yaml
import mkdocs
import logging
from mkdocs.plugins import BasePlugin
from mkdocs.utils import warning_filter

import jinja2
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

    JINJA_OPTIONS = "jinja_options"

    config_scheme = (
        ("data", mkdocs.config.config_options.Type(str_type, default=None)),
        (JINJA_OPTIONS, mkdocs.config.config_options.Type(dict, default={}))
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
        data_source_folders = self.config.get("data", {})
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

    # Apply template substitution to both page content and title
    def on_page_markdown(self, markdown, page, **kwargs):
        page.title = self.apply_template(page.title)
        return self.apply_template(markdown)

    # Initialize this mkdocs config and Jinja2 env
    def on_config(self, mkdocsConfig, **kwargs):
        jinja_options = self.config[self.JINJA_OPTIONS]
        self.env = jinja2.Environment(undefined=jinja2.DebugUndefined, **jinja_options)
        self.mkdocsConfig = mkdocsConfig

    # Apply Jinja2 substitution to specified string
    def apply_template(self, template_string):
        md_template = self.env.from_string(template_string)
        return md_template.render(**self.mkdocsConfig.get("extra"))
