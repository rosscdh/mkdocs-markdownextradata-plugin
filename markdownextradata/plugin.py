from mkdocs.plugins import BasePlugin

from jinja2 import Template


CONFIG_KEYS = [
    'site_name',
    'site_author',
    'site_url',
    'repo_url',
    'repo_name'
]


class MarkdownExtraDataPlugin(BasePlugin):
    """
    Inject certain config variables into the markdown
    """
    def on_page_markdown(self, markdown, config, **kwargs):
        context = {key: config.get(key) for key in CONFIG_KEYS if key in config}
        context.update(config.get('extra', {}))
        extra = config.get('extra')
        md_template = Template(markdown)
        return md_template.render(**extra)
