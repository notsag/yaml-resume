import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "yaml-resume"
copyright = "2019, Maxime GASTON"
author = "Maxime GASTON"

version = "dev"
extensions = ["sphinx.ext.autodoc"]

# -- General configuration ---------------------------------------------------

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

html_static_path = ["_static"]
html_logo = "_static/yaml-resume.png"
html_title = "YAML Resume Documentation ({})".format(version)
html_show_sourcelink = False
html_sidebars = {
    "**": ["globaltoc.html", "relations.html", "sourcelink.html", "searchbox.html"]
}
