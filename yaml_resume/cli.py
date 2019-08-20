import click
import yaml
from . import validator
from .resume import Resume


def no_tag(self, *args, **kw):
    """Drop tag in yaml.dump()

    This function should be used to set the
    `yaml.emitter.Emitter.process_tag` to have a nice YAML file.
    """
    pass


def str_representer(dumper, data):
    """Use literal block scalar style for multiline strings.

    This function should be used as the `representer` argument of
    the yaml.add_representer() function before dumping the YAML.

    """
    if len(data.splitlines()) > 1:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style="|"
        )
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


@click.group()
@click.version_option(prog_name="yaml-resume")
def cli():
    """Define a command as a group.

    This function is a `click.group()` which will be used to provide
    the yaml-resume command.

    """
    pass


@cli.command(short_help="Interactive resume creation")
@click.argument("filename")
def init(filename):
    """cli subcommand to create a resume

    This function is a subcommand of `cli`.
    It will prompt questions to the user to build a Resume
    object and write it to a file.

    :param filename: The name of the file to create.
    :type filename: str.

    """
    resume = Resume.ask()
    with open(filename, "w+") as outfile:
        yaml.emitter.Emitter.process_tag = no_tag
        yaml.add_representer(str, str_representer)
        yaml.dump(resume, outfile, default_flow_style=False)
    outfile.close()


@cli.command(short_help="Validate resume file content")
@click.argument("filename")
def validate(filename):
    """cli subcommand to validate a YAML resume

    This function is a subcommand of `cli`.
    It checks the resume against the schema to ensure it is well formed.

    :param filename: The name of the file to create.
    :type filename: str.
    :raises: ClickException

    """
    (result, errors) = validator.validate(filename)
    if not result:
        raise click.ClickException(errors)
    else:
        click.echo("Resume is well formed.")


if __name__ == "__main__":
    cli()
