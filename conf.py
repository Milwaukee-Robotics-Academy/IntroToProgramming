# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'XRP'
copyright = '2023, Worcester Polytechnic Institute. Modified by Milwaukee Robotics Academy'
author = 'Worcester Polytechnic Institute'
release = '2023.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_new_tab_link',
    "sphinx_design",
    'sphinx_toolbox.collapse',
    "sphinxcontrib.youtube",
    "sphinxcontrib.video",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'prev_next_buttons_location': 'both'
}
html_static_path = ['_static']
master_doc = 'index'
