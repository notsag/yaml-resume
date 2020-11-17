from yaml_resume.cli import cli
from click import ClickException
from click.testing import CliRunner
from .scenarios import SCENARIO_VALID
import logging
import pytest


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
    result = runner.invoke(cli, ["init", SCENARIO_VALID["file"]], input=answers)
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


@pytest.mark.xfail(raises=ClickException)
def test_fail_validate():
    """
    Yaml file with single 'contact:' line should return an error
    """
    wrongfile = "test-results/wrong.yml"
    with open(wrongfile, "w") as out:
        out.write("contact:")
    runner = CliRunner()
    runner.invoke(cli, ["validate", wrongfile])


@pytest.mark.parametrize(
    "extension, theme",
    [
        ("html", "classic"),
        ("html", "material"),
        ("pdf", "classic"),
        ("pdf", "material"),
    ],
)
def test_export(extension, theme):
    """
    Test exporting files to html/pdf
    """
    runner = CliRunner()
    export = "test-results/{}".format(theme)
    result = runner.invoke(
        cli,
        [
            "export",
            "sample.yml",
            "-e",
            extension,
            "-i",
            "sample_id.png",
            "-t",
            theme,
            "-o",
            export,
        ],
    )
    # expected = "examples/{}".format(export)
    # exported = export
    assert result.exit_code == 0


@pytest.mark.xfail(raises=ClickException)
@pytest.mark.parametrize(
    "options",
    [
        ["export", "test-results/wrong.html"],
        ["export", "sample.yml", "-e", "html", "-t", "material"],
    ],
)
def test_fail_export(options):
    """
    Test export failures.
    """
    runner = CliRunner()
    runner.invoke(cli, options)
