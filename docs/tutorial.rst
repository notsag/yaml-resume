.. _tutorial:

Tutorial
========

This is where you will learn how to use yaml-resume.

Create a resume
---------------

Create a resume is easy. You can obviously edit the `sample.yml` or use the
`yaml-resume` cli to prompt the questions to build your resume:

.. code-block:: sh

    $ yaml-resume init my-resume.yml

The `init` subcommand of `yaml-resume` will prompt all the fields of the resume
according to the schema.

Validate the resume
-------------------

To validate your yaml file, just use the `yaml-resume` cli again:

.. code-block:: sh

    $ yaml-resume validate my-resume.yml

The `validate` subcommand of `yaml-resume` will check your yaml file against the schema
and return the possible errors like missing or unknown field, regex not matched...

Export the resume to html/pdf
-----------------------------

To export your yaml resume to html/pdf and apply a theme:

.. code-block:: sh

    $ yaml-resume export my-resume.yml [-t <theme>] [-e <html|pdf>] [-i <picture>] [-o <output-file>]

By default, the theme is `classic`, the format is `html` and the output file will be `resume.html`.

Schema
------

yaml-resume uses `Cerberus`_ to define a schema and validate our yaml-resume
against this schema.

.. _Cerberus: https://python-cerberus.org/

The schema is available inside the `yaml_resume.validator.schema` module.

Global schema
`````````````

The global schema shows the different sections and restrictions including subschemas.

.. literalinclude:: ../yaml_resume/validator/schema.py
    :language: python
    :linenos:
    :lines: 69-118

Subschemas
``````````

The subschemas are defined the same as the global schema but describes inner sections.
For example:

.. literalinclude:: ../yaml_resume/validator/schema.py
    :language: python
    :linenos:
    :lines: 55-67

Regular expressions
```````````````````

The regular expressions are defined to verify validity of the data: for example
an email address should respect a format such as `john@doe.com`.

.. literalinclude:: ../yaml_resume/validator/schema.py
    :language: python
    :linenos:
    :lines: 2

Example
```````

An YAML resume example is avalaible in the project as `sample.yml`:

.. literalinclude:: ../sample.yml
    :language: yaml
