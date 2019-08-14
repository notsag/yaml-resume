#!/usr/bin/env python
import click
import yaml
from yaml_resume import validator
from yaml_resume.resume import Resume


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
def cli():
    pass


@cli.command()
@click.argument("filename")
def init(filename):
    """Setup a new resume through cli questionnaire"""
    resume = Resume.ask()
    with open(filename, "w+") as outfile:
        yaml.emitter.Emitter.process_tag = no_tag
        yaml.add_representer(str, str_presenter)
        yaml.dump(resume, outfile, default_flow_style=False)
    outfile.close()


@cli.command()
@click.argument("filename")
def validate(filename):
    """Validate YAML file"""
    (result, errors) = validator.validate(filename)
    if not result:
        raise click.ClickException(errors)
    else:
        click.echo("Resume is well formed.")


if __name__ == "__main__":
    cli()
