# coding=utf-8
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

import sphinx_py3doc_enhanced_theme as sphinx_theme
from importlib.metadata import version
from typing import Any, TYPE_CHECKING, Tuple  # noqa: F401

if TYPE_CHECKING:
    from sphinx.application import Sphinx   # noqa: F401
    from sphinx.ext.autodoc import Options  # noqa: F401

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('../../src'))
# print(sys.path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'polynomial'
copyright = '2023 ff., Michael Amrhein'
author = 'Michael Amrhein'
# The full version, including alpha/beta/rc tags.
full_version = version(project)
release = '.'.join(full_version.split('.')[:3])
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

add_module_names = False
pygments_style = 'sphinx'
python_use_unqualified_type_names = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = sphinx_theme.__name__

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
add_css = """
/* light lilac background for class and function head-lines */
dl.class > dt, dl.function > dt, dl.exception > dt{
    background: rgb(245,245,255) none repeat scroll 0% 0%;
    border-radius: 4px;
    padding-left: 10px;
    margin-left: -10px;
    line-height: 2em
}
/* light grey background for labels in signature table */
dl.field-list > dt{
    background: rgb(245,245,245) 
}
/* overwrite enlarged font for toc */
.toctree-l1 {
    font-size: 100%;
}
/* show nav-links also on the top of the page */
div.related:first-child li.right {
    display: inherit;
}
"""

html_theme_options = {
    "bodyfont": "sans-serif",
    "headfont": "sans-serif",
    "codefont": "monospace",
    # "externalrefs": True,
    "sidebardepth": 3,
    "codebgcolor": "rgb(255,255,245) !important",
    "appendcss": add_css
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [
    sphinx_theme.get_html_theme_path(),
]
html_show_sourcelink = False

# -- Options for ext.napoleon ---------------------------------------------
napoleon_use_rtype = False

# -- Options for ext.autodoc ----------------------------------------------
autoclass_content = 'class'
autodoc_class_signature = 'separated'
autodoc_member_order = 'groupwise'
autodoc_typehints = 'signature'
autodoc_preserve_defaults = True
