#!/usr/bin/env python

import re
from setuptools import setup

with open("README.md") as f:
    README = f.read()

with open("yaml_resume/__init__.py") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="yaml-resume",
    packages=["yaml_resume", "yaml_resume.resume", "yaml_resume.validator"],
    package_data={"yaml_resume": ["templates/*.html"]},
    description="Command line interface to build/validate YAML resumes",
    long_description=README,
    long_description_content_type="text/markdown",
    version=version,
    url="https://github.com/notsag/yaml-resume",
    author="Maxime GASTON",
    author_email="maxime@gaston.sh",
    license="gpl-3.0",
    keywords=["resume", "yaml"],
    install_requires=["click", "pyyaml", "cerberus"],
    entry_points={"console_scripts": ["yaml-resume = yaml_resume.cli:cli"]},
    tests_require=["pytest", "pytest-cov"],
    python_requires=">=3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
