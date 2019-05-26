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
              '10 Downing Street\nLondon\nSW1A 2AA\n\nUK\ny\n' +
              'Facebook\nhttps://facebook.com/johndoe\ny\n' +
              'Twitter\nhttps://twitter.com/nottherealjohndoe\nn\ny\n' +
              'Starfleet\nCaptain\nJanuary 2150\n\nCommanding officer of ' +
              'starship Enterprise\n\nFought Klingons\n\nDisccoverd worlds' +
              '\nn\nofficer commander warp\nn\ny'
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
