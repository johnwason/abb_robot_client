# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'abb_robot_client'
copyright = '2022, Wason Technology, LLC'
author = 'John Wason'

import abb_robot_client

# The short X.Y version.
# version = abb_robot_client.__version__
# The full version, including alpha/beta/rc tags.
# release = abb_robot_client.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
     "sphinx.ext.autodoc",
     "sphinx_autodoc_typehints"
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
