from yaml_resume.cli import cli
from click.testing import CliRunner
import logging

TESTFILE = "tests/test.yml"


def test_usage():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert "Usage:" in result.output
    assert result.exit_code == 0


def test_init():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["init", TESTFILE],
        input="John Doe\n10/10/1990\nCaptain\njohn@doe.com\n+33611111111\n"
        + "10 Downing Street\nLondon\nSW1A 2AA\n\nUK\ny\n"
        + "Facebook\nhttps://facebook.com/johndoe\ny\n"
        + "Twitter\nhttps://twitter.com/nottherealjohndoe\nn\ny\n"
        + "Starfleet\nCaptain\nJanuary 2150\n\nCommanding officer of "
        + "starship Enterprise\nFought Klingons\nDisccoverd worlds"
        + "\n\nofficer commander warp\nhttps://starfleet.com\nn\ny\n"
        + "Starfleet\nCaptain MD\nJanuary 2145\nDecember 2150\n"
        + "http://starfleet.com\nn\ny\nManagement\n100\ny\nFighting\n75\nn\ny"
        + "\nEnglish\nNative\nn\ny\ntestproject\nnothing special\n"
        + "https://google.com\nn\ny\nSport\nRunning and stuff\nn\ny",
    )
    assert result.exit_code == 0


def test_validate():
    runner = CliRunner()
    result = runner.invoke(cli, ["validate", TESTFILE])
    if result.output != "":
        logging.error(result.output)
    assert result.exit_code == 0


def test_fail_validate():
    wrongfile = "tests/wrong.yml"
    with open(wrongfile, "w") as out:
        out.write("contact:")
    runner = CliRunner()
    result = runner.invoke(cli, ["validate", wrongfile])
    assert result.exit_code != 0
