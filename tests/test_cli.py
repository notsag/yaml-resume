from yaml_resume.cli import cli
from click.testing import CliRunner
from .scenarios import SCENARIO_VALID
import logging


def test_usage():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert "Usage:" in result.output
    assert result.exit_code == 0


def test_init():
    """
    Create a resume using SCENARIO_VALID
    """
    runner = CliRunner()
    answers = ""
    for answer in SCENARIO_VALID["answers"]:
        answers += answer + "\n"
    result = runner.invoke(
        cli, ["init", SCENARIO_VALID["file"]], input=answers
    )
    assert result.exit_code == 0


def test_validate():
    """
    SCENARIO_VALID should validate
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["validate", SCENARIO_VALID["file"]])
    if result.output != "":
        logging.error(result.output)
    assert result.exit_code == 0


def test_fail_validate():
    """
    Yaml file with single 'contact:' line should return an error
    """
    wrongfile = "tests/wrong.yml"
    with open(wrongfile, "w") as out:
        out.write("contact:")
    runner = CliRunner()
    result = runner.invoke(cli, ["validate", wrongfile])
    assert result.exit_code != 0


def test_export_html():
    pass
