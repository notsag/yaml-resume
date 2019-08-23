.. _installation:

Installation
============

Python Version
--------------

We recommend using the latest version of Python 3. yaml-resume supports Python 3.5
and newer.

Dependencies
------------

These distributions will be installed automatically when installing yaml-resume.

* `Click`_ is a framework for writing command line applications. It provides
  the ``yaml-resume`` command.
* `PyYaml`_ is the yaml framework used to dump Python object into Yaml.
* `Cerberus`_ is the framework used to validate the resume against a defined schema.
* `Jinja2`_ is the template engine used to generate HTML resumes.
* `WeasyPrint`_ is the library used to export resumes to PDF.

.. _Click: https://palletsprojects.com/p/click/
.. _PyYaml: https://pyyaml.org/
.. _Cerberus: https://python-cerberus.org/
.. _Jinja2: https://palletsprojects.com/p/jinja/
.. _WeasyPrint: https://weasyprint.org/

Install yaml-resume
-------------------

.. code-block:: sh

    $ python3 -m pip install yaml-resume


yaml-resume is now installed. Check out the :doc:`/tutorial` or go to the
:doc:`Documentation Overview </index>`.
