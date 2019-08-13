#!/usr/bin/env python
import click
import yaml
from yaml_resume import validator
from yaml_resume.resume import Resume


def no_tag(self, *args, **kw):
    """Drop tag in yaml.dump()"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.argument("filename")
def init(filename):
    """Setup a new resume through cli questionnaire"""
    resume = Resume.ask()
    with open(filename, "w+") as outfile:
        yaml.emitter.Emitter.process_tag = no_tag
        yaml.dump(resume, outfile, default_flow_style=False)
    outfile.close()


@cli.command()
@click.argument("filename")
def validate(filename):
    """Validate YAML file"""
    (result, errors) = validator.validate(filename)
    if not result:
        raise click.ClickException(errors)


if __name__ == "__main__":
    cli()
