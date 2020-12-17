import os
import yaml
import click
import pytest
import tempfile
from pathlib import Path
from click.testing import CliRunner
from mkdocs.__main__ import build_command

config = yaml.load(open('test/mkdocs.yml', 'rb'), Loader=yaml.Loader)

def test_basic_working():
    runner = CliRunner()
    customer = config.get('extra', {}).get('customer', {})
    test_json_string = config.get('extra', {}).get('test_json_string', "")

    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(build_command, ['--config-file', 'test/mkdocs.yml', '--site-dir', tmpdir])
        assert result.exit_code == 0

        index_file = Path(tmpdir) / 'index.html'
        assert index_file.exists(),  f"{index_file} does not exist, it should"
        contents = index_file.read_text()

        assert '<a href="page/" class="nav-link">Hi there, Your name here</a>' in contents, f"customer.name is not in index"
        assert '<p>Inside the included md file there 3 <img alt="star" src="ressources/star.png" /></p>' in contents, f"customer.star is not in index or not rendering as expected"
        assert f"Welcome to {customer.get('web_url')}" in contents, f"customer.web_url is not in index"
        assert f"{{#binding.path}}" in contents, f"Jinja2 comment syntax wasn't reconfigured via jinja_options as expected"
        assert isinstance(test_json_string, str), "test_json_string is not a str it should be"
        assert '{"name": "Bob"}' == test_json_string, f"Json string is not correct"
