#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    README = f.read()

setup(
    name="yaml-resume",
    packages=["yaml_resume", "yaml_resume.resume", "yaml_resume.validator"],
    description="Command line interface to build/validate YAML resumes",
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1.2",
    url="http://github.com/notsag/yaml-resume",
    author="Maxime GASTON",
    author_email="maxime@gaston.sh",
    license="gpl-3.0",
    keywords=["resume", "yaml"],
    install_requires=["click", "pyyaml", "cerberus"],
    entry_points={"console_scripts": ["yaml-resume = yaml_resume.cli:cli"]},
    tests_require=["pytest", "pytest-cov"],
)
