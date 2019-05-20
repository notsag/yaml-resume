#!/usr/bin/env python
import click
import yaml
from yaml_resume import validator


@click.group()
def cli():
    pass


def ask_contact():
    """Prompt questions for contact informations"""
    contact = {}
    name = click.prompt("What is your name?")
    contact['name'] = name
    job = click.prompt("What is your job title?")
    contact['job'] = job
    email = click.prompt("What is your email address?")
    contact['email'] = email
    phone = click.prompt("What is your phone number?")
    contact['phone'] = phone
    location = {}
    address = click.prompt("What is your address?")
    location['address'] = address
    city = click.prompt("In what city?")
    location['city'] = city
    zipcode = click.prompt("Postal/Zip code of that city?")
    location['zip'] = zipcode
    state = click.prompt("In what state? (optional)", default="")
    if state != "":
        location['state'] = state
    country = click.prompt("In what country? (optional)", default="")
    if country != "":
        location['country'] = country
    contact['location'] = location
    return contact


@cli.command()
@click.argument('filename')
def init(filename):
    """Setup a new resume through cli questionnaire"""
    contact = ask_contact()
    with open(filename, 'w+') as outfile:
        resume = {
            'contact': contact,
            }
        yaml.dump(resume, outfile, default_flow_style=False)
    outfile.close()


@cli.command()
@click.argument('filename')
def validate(filename):
    """Validate YAML file"""
    (result, errors) = validator.validate(filename)
    if not result:
        raise click.ClickException(errors)


if __name__ == '__main__':
    cli()
