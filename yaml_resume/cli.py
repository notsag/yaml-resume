import click
import yaml
import os
from jinja2 import Environment, PackageLoader
from weasyprint import HTML, CSS
from . import validator
from .resume import Resume

THEMES = {
    "classic": "optional",
    "material": "mandatory",
    "modern": "optional"
}  # optional or mandatory depending if the theme must have an profile picture

PAGE_FORMATS = {
    "A4": "@page { size: A4; margin: 0cm }",
    "US_Letter": "@page { size: letter; margin: .5in }" 
}

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
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


@click.group()
@click.version_option(prog_name="yaml-resume")
def cli():
    """yaml-resume CLI

    This function is a `click.group()` which will be used to provide
    the main yaml-resume command.

    """
    pass


@cli.command(short_help="Interactive resume creation")
@click.argument("filename")
def init(filename):
    """cli subcommand to create a resume

    This function is a subcommand of yaml-resume.
    It will prompt questions to the user to build a Resume
    object and write it to a file.
    \f

    :param filename: The name of the file to create.
    :type filename: str

    """
    resume = Resume.ask()
    with open(filename, "w") as outfile:
        yaml.emitter.Emitter.process_tag = no_tag
        yaml.add_representer(str, str_representer)
        yaml.dump(resume, outfile, default_flow_style=False)
    outfile.close()


@cli.command(short_help="Validate resume file content")
@click.argument("filename")
def validate(filename):
    """cli subcommand to validate a YAML resume

    This function is a subcommand of yaml-resume.
    It checks the resume against the schema to ensure it is well formed.
    \f

    :param filename: The path of the file to validate.
    :type filename: str
    :raises: ClickException

    """
    (result, errors) = validator.validate(filename)
    if not result:
        raise click.ClickException(errors)
    else:
        click.echo("Resume is well formed.")


@cli.command(short_help="Export resume to HTML or PDF")
@click.argument("filename")
@click.option(
    "-t",
    "--theme",
    default="classic",
    type=click.Choice(THEMES),
    help="Name of the theme to use.",
)
@click.option(
    "-e",
    "--extension",
    default="html",
    type=click.Choice(["html", "pdf"]),
    help="Format of exported data.",
)
@click.option("-i", "--image", default=None, help="Portrait to include in the resume.")
@click.option("-o", "--output", default="resume", help="Name of the file to write.")
@click.option(
    "-pt",
    "--page-type",
    default="A4",
    type=click.Choice(PAGE_FORMATS),
    help="Page Type: A4 or 8.5\"x11\""
)
def export(filename, theme, extension, image, output, page_type):
    """cli subcommand to export a YAML resume to HTML or PDF

    This function is a subcommand of yaml-resume.
    It exports the resume in html or pdf using a template.
    \f

    :param filename: The name of the file to load.
    :type filename: str
    :param theme: The name of the theme to use.
    :type theme: str
    :param extension: The format of the exported data.
    :type format: str
    :param image: Path to Resume Image
    :type format: str
    :param output: Output filename
    :type format: str
    :param page: Page Type
    :type format: str
    :raises: ClickException

    """
    if THEMES[theme] == "mandatory" and not image:
        error = (
            "Material theme MUST have an image for profile picture."
            + "\nYou should add the following parameter :\n"
            + "\t--image <path-to-png>"
        )
        raise click.ClickException(error)
    (result, errors) = validator.validate(filename)
    if not result:
        raise click.ClickException(errors)
    else:
        env = Environment(
            loader=PackageLoader("yaml_resume", "templates"), autoescape=True
        )
        resume = yaml.load(open(filename, "r"), yaml.SafeLoader)
        template = env.get_template("{}.html".format(theme))
        if image:
            image = os.path.abspath(image)
        if extension == "html":
            with open("{}.{}".format(output, extension), "w") as outfile:
                outfile.write(template.render(resume=resume, image=image))
            outfile.close()
        else:
            html = HTML(string=template.render(resume=resume, image=image))
            css = CSS(string=PAGE_FORMATS[page_type])
            html.write_pdf("{}.{}".format(output, extension), stylesheets=[css])


if __name__ == "__main__":
    cli()
