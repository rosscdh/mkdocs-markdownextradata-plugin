# mkdocs-markdownextradata-plugin

[![Build Status](https://travis-ci.org/rosscdh/mkdocs-markdownextradata-plugin.svg?branch=master)](https://travis-ci.org/rosscdh/mkdocs-markdownextradata-plugin)

*A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template*

**usecase**

```
As a user with variables that need to be inserted at the markdown level, not the template level.
I need a mkdocs plugin that will inject my `extras` variables into the markdown template before it gets rendered to html.
So that I can build my markdown pages with different values for images, urls, client_names, etc. 
```

## Installation

> **Note:** This package requires MkDocs version 0.17 or higher. 

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


## Features

### Use Extra Variables in your markdown files

The variables you define in the mkdown.yml `extra:` slot will become available in your templates

```yaml
site_name: My fantastic site

plugins:
    - search
    - markdownextradata

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

### Using external data files

If the `extra: {}` hash is not enough for your data then you are able to make use of external yaml files to provide that context data

```yaml
plugins:
    - search
    - markdownextradata:
        data: path/to/datafiles
```

or if you have multiple locations provide a comma (,) separated list of locations

```yaml
plugins:
    - search
    - markdownextradata:
        data: path/to/datafiles, another/path/to/datafiles
```

if you leave `markdownextradata.data` empty

```yaml
plugins:
    - search
    - markdownextradata
```

by default it will search in the folder where your mkdocs.yml is kept
and in the docs folder for another folder called `_data`

i.e. `./docs/_data/site.yaml` - available as '{{ site.whatever_variable_in_the_yaml}}'

If this path is found, the plugin will read all `.yml|.yaml` and `.json`
files inside it and add the data in them, to the template context.

If inside your data folder you have a directory and a file file
called `[path/to/datafiles/]sections/captions.yaml` - where `[path/to/datafiles/]` is the path in your configuration -
the data inside that file will be available in your templates as `sections.captions.whatever_variable_in_the_yaml`.

### Jinja2 Template Engine Configuration

You may provide [Jinja2 configuration](https://jinja.palletsprojects.com/en/2.11.x/api/#high-level-api) as plugin options:

```yml
plugins:
    - markdownextradata:
        jinja_options:
          comment_start_string: __CUSTOMCOMMENTSTART__
```

The above example will make it so that instead of `{#`, the template engine will interpret `__CUSTOMCOMMENTSTART__` as comment start delimiter. This is useful in cases where
you write Markdown that contains Jinja-like syntax that's colliding with the template engine. Alternatively, it lets you control what the variable delimiter is (instead of the default `{{ }}`).

## Testing

```
virtualenv venv -p python3.7
source venv/bin/activate
python setup.py test
pytest test
```

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
- [Michael Jess](https://github.com/miffels)
