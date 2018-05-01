from mkdocs.plugins import BasePlugin

from jinja2 import Template


class MarkdownExtraDataPlugin(BasePlugin):
    """
    Inject config 'extra' variables into the markdown
    """
    def on_page_markdown(self, markdown, page, config, site_navigation, **kwargs):
        if 'extra' not in config:
            return markdown
        else:
            extra = config.get('extra')
            md_template = Template(markdown)
            return md_template.render(**extra)
