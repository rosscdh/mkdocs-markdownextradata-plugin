# mkdocs-markdownextradata-plugin

*A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template*

The markdownextra plugin allows you to customize how your pages show up the navigation of your MkDocs without having to configure the full structure in your `mkdocs.yml`. It extracts the title from your markdown files and gives you detailed control using a small configuration file directly placed in the relevant directory of your documentation.

> **Note:** This plugin works best without a `pages` entry in your `mkdocs.yml`. Having a `pages` entry is supported, but you might not get the results you expect, especially if your `pages` structure doesn't match the file structure.

<br/>

## Installation

> **Note:** This package requires MkDocs version 0.17 or higher. 

Install the package with pip:

```bash
pip install mkdocs-markdownextra-plugin
```

Enable the plugin in your `mkdocs.yml`:

```yaml
plugins:
    - search
    - markdownextra
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation][mkdocs-plugins]

<br/>

## Features

### Use Extra Variables in your markdown files

The variables you define in the mkdown.yml `extra:` slot will become available in your templates
<br/>

## Contributing

From reporting a bug to submitting a pull request: every contribution is appreciated and welcome.
Report bugs, ask questions and request features using [Github issues][github-issues].
If you want to contribute to the code of this project, please read the [Contribution Guidelines][contributing].

[travis-status]: https://travis-ci.org/rosscdh/mkdocs-markdownextradata-plugin.svg?branch=master
[travis-link]: https://travis-ci.org/rosscdh/mkdocs-markdownextradata-plugin
[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[github-issues]: https://github.com/rosscdh/mkdocs-markdownextradata-plugin/issues
[contributing]: CONTRIBUTING.md
