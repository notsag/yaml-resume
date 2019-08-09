# yaml-resume

[![PyPI version](https://badge.fury.io/py/yaml-resume.svg)](https://badge.fury.io/py/yaml-resume)
[![Build Status](https://travis-ci.org/notsag/yaml-resume.svg?branch=master)](https://travis-ci.org/notsag/yaml-resume)
[![codecov](https://codecov.io/gh/notsag/yaml-resume/branch/master/graph/badge.svg)](https://codecov.io/gh/notsag/yaml-resume)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
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

## Contributions

Please have a look at the [contributing guide](https://github.com/notsag/yaml-resume/blob/master/CONTRIBUTING.md) and the [code of conduct](https://github.com/notsag/yaml-resume/blob/master/CODE_OF_CONDUCT.md).

### TL;DR

You can ask for features/report bugs using Github issues.
You can submit work using Github Pull Requests.

To test development version without installing : 

```
# To install dependencies
python3 -m pip install -r requirements.txt

# To run the cli
python3 -m yaml_resume.cli

# To run the test suite
python3 -m pytest --cov=yaml_resume tests/
```

## Credits

This project was inspired by : [JSON Resume](https://github.com/jsonresume).

Special thanks to all contributors of the following projects used by yaml-resume :
 - [click](https://github.com/pallets/click/)
 - [cerberus](https://github.com/pyeve/cerberus)
