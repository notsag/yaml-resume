from pallets_sphinx_themes import ProjectLink
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "yaml-resume"
copyright = "2019, Maxime GASTON"
author = "Maxime GASTON"

# The short X.Y version
version = "0.2.0"

# The full version, including alpha/beta/rc tags
release = "0.2.0"

# -- General configuration ---------------------------------------------------

extensions = ["pallets_sphinx_themes", "sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

html_theme = "flask"

html_static_path = ["_static"]
html_logo = "_static/yaml-resume.png"
html_title = "YAML Resume Documentation ({})".format(version)
html_show_sourcelink = False
html_context = {
    "project_links": [
        ProjectLink("YAML Resume Website", "https://yaml-resume.com"),
        ProjectLink("PyPI releases", "https://pypi.org/project/yaml-resume/"),
        ProjectLink("Source Code", "https://github.com/notsag/yaml-resume/"),
        ProjectLink(
            "Issue Tracker", "https://github.com/notsag/yaml-resume/issues/"
        ),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
