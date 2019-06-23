# mkdocs-markdownextradata-plugin

*A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template*

**usecase**

```
As a user with variables that need to be inserted at the markdown level, not the template level.
I need a mkdocs plugin that will inject my `extras` variables into the markdown template before it gets rendered to html.
So that I can build my markdown pages with different values for images, urls, client_names, etc. 
```

## Installation

**Note:** This package requires MkDocs version 0.17 or higher. 

Install the package with pip:

```bash
pip install mkdocs-markdownextradata-plugin
```

Enable the plugin in your `mkdocs.yml`:

```yaml
plugins:
    - search
    - markdownextradata: {}
```

You are then able to use the mkdocs `extra: {}` hash to pass context data into your files

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.


### Using external data files

If the `extra: {}` hash is not enough for your data then you are able to make use of external yaml files to provide that context data

```yaml
plugins:
    - search
    - markdownextradata:
        data: path/to/datafiles
```

The data path is optional; when absent, it will look for a `_data`
folder adjacent to your `mkdocs.yml` and inside your `docs_dir`.
If this path is found, the plugin will read all `.yml` and `.json`
files inside it and add the data in them to the data available to the templates.
The paths to these become their variable names, so if inside your data folder you have a file
called `sections/captions.yml`, the data inside that file will be available in your
templates as `sections.captions`.

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

### Contributors

- [Ross Crawford-d'Heureuse](https://github.com/rosscdh)
- [Emiliano Heyns](https://github.com/retorquere)