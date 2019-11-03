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

    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(build_command, ['--config-file', 'test/mkdocs.yml', '--site-dir', tmpdir])
        assert result.exit_code == 0

        index_file = Path(tmpdir) / 'index.html'
        assert index_file.exists(),  f"{index_file} does not exist, it should"
        contents = index_file.read_text()

        assert f"Hi there, {customer.get('name')}" in contents, f"customer.name is not in index"
        assert f"Welcome to {customer.get('web_url')}" in contents, f"customer.web_url is not in index"
