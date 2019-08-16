#!/usr/bin/env python
import click
import yaml
from . import validator
from .resume import Resume


def no_tag(self, *args, **kw):
    """Drop tag in yaml.dump()"""
    pass


def str_presenter(dumper, data):
    """Use literal block scalar style for multiline strings"""
    if len(data.splitlines()) > 1:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style="|"
        )
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


@click.group()
@click.version_option(prog_name="yaml-resume")
def cli():
    """
    This is the command that will be used.
    We define a click group that will includes all subcommands.
    """
    pass


@cli.command()
@click.argument("filename")
def init(filename):
    """
    cli subcommand.
    Create a resume from questionnaire and writes it in file from argument.
    """
    resume = Resume.ask()
    with open(filename, "w+") as outfile:
        yaml.emitter.Emitter.process_tag = no_tag
        yaml.add_representer(str, str_presenter)
        yaml.dump(resume, outfile, default_flow_style=False)
    outfile.close()


@cli.command()
@click.argument("filename")
def validate(filename):
    """
    cli subcommand.
    Validate (or not) the resume file from argument.
    """
    (result, errors) = validator.validate(filename)
    if not result:
        raise click.ClickException(errors)
    else:
        click.echo("Resume is well formed.")


if __name__ == "__main__":
    cli()
