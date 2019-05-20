#!/usr/bin/env python

from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))
INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

setup(
    name='yaml-resume',
    packages=['yaml_resume'],
    description="YAML resume command line interface",
    long_description=README,
    version='0.0.1',
    url='http://github.com/notsag/yaml-resume',
    author='Maxime GASTON',
    author_email='maxime@gaston.sh',
    license='gpl-3.0',
    keywords=['resume', 'yaml'],
    install_requires=INSTALL_PACKAGES,
    entry_points={
            'console_scripts': [
                        'yaml-resume = yaml_resume.resume:cli',
                        ]
            },
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-sugar'
        ]
    )
