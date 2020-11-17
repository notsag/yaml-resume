# yaml-resume

![](https://yaml-resume.com/logo.png)

[![PyPI version](https://badge.fury.io/py/yaml-resume.svg)](https://badge.fury.io/py/yaml-resume)
[![Build Status](https://travis-ci.com/notsag/yaml-resume.svg?branch=master)](https://travis-ci.com/notsag/yaml-resume)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=notsag_yaml-resume&metric=alert_status)](https://sonarcloud.io/dashboard?id=notsag_yaml-resume)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Pypy-3.6](https://img.shields.io/badge/pypy-3.6-blue.svg)](https://pypy.org/download.html)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
=======

## Purpose

This is an open source initiative to create a YAML-based resume.

## Getting Started

### Install

Package is available on Pypi : 

```
pip install yaml-resume
```

### Usage

Init a new resume through an interactive cli:

```
yaml-resume init FILENAME
```

Validate your yaml resume:

```
yaml-resume validate FILENAME
```

Export you resume in html or pdf:

```
yaml-resume export FILENAME [-t <theme>] [-e <html|pdf>] [-i <picture>] [-o <output-file>]
```

## Contributions

Please have a look at the [contributing guide](https://github.com/notsag/yaml-resume/blob/master/CONTRIBUTING.md) and the [code of conduct](https://github.com/notsag/yaml-resume/blob/master/CODE_OF_CONDUCT.md).

### TL;DR

You can ask for features/report bugs using Github issues.
You can submit work using Github Pull Requests.

To test development version without installing : 

```
# To install dependencies
python3 -m pip install -r requirements.txt
python3 -m pip install pytest pytest-cov flake8 black pre-commit

# To run the cli
python3 -m yaml_resume

# To run the test suite
python3 -m pytest --cov=yaml_resume tests/

# To install pre-commit hook
pre-commit install
```

## Credits

This project was inspired by : [JSON Resume](https://github.com/jsonresume).

Special thanks to all contributors of the following projects used by yaml-resume :
 - [click](https://palletsprojects.com/p/click/)
 - [cerberus](https://python-cerberus.org)
 - [PyYAML](https://pyyaml.org/)
 - [jinja2](https://palletsprojects.com/p/jinja/)
 - [WeasyPrint](https://weasyprint.org/)
