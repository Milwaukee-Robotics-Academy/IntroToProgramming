# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'FRC 2027 Programming with WPILib & YAGSL'
copyright = '2026, Milwaukee Robotics Academy'
author = 'Milwaukee Robotics Academy'
release = '2027.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_new_tab_link',
    'sphinx_design',
    'sphinxcontrib.youtube',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
]

# Prefix section labels with document path to avoid duplicate label warnings
autosectionlabel_prefix_document = True

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'navigation_depth': 3,
}

master_doc = 'index'
