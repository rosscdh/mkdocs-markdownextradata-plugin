# mkdocs-markdownextradata-plugin

*A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template*

As a user with variables that need to be substituted for multiple projects at the markdown and not the template level.
In order to defined values such as site urls, client names etc 
So that I can build my docs with different values for images and urls etc. 

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

```yaml
extra:
  customer:
    name: Your name here
    web: www.example.com
    salt: salt.example.com
```

and then in your `*.md` files

```jinja
{{ customer.name }}
<a href="{{ customer.web }}">{{ customer.web }}</a>
```

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
