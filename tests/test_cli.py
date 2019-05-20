from yaml_resume.cli import cli
from click.testing import CliRunner
import logging

TESTFILE = 'tests/test.yml'


def test_init():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['init', TESTFILE],
        input='John Doe\nCaptain\njohn@doe.com\n+33611111111\n' +
              '10 Downing Street\nLondon,SW1A 2AA\n\nUK\n'
        )
    assert result.exit_code == 0


def test_validate():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['validate', TESTFILE]
        )
    if result.output != "":
        logging.error(result.output)
    assert result.exit_code == 0
