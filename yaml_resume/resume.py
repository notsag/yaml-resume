#!/usr/bin/env python
import click
import yaml


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--path',
    prompt='Path of your resume: '
    )
@click.option(
    '--name',
    prompt='Your name: '
    )
def init(path, name):
    with open(path, 'w+') as outfile:
        resume = {'resume': {'name': name}}
        yaml.dump(resume, outfile, default_flow_style=False)


@cli.command()
@click.argument('filename')
def validate(filename):
    pass


if __name__ == '__main__':
    cli()
