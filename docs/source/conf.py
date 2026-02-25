"""Configuration file for Sphinx documentation."""

import os
import sys

# Add the project root to Python path so autodoc can find your modules
sys.path.insert(0, os.path.abspath('../..'))

# Project information
project = 'Weather Tools'
copyright = '2026, Penmatsa Tanoj Pavan Surya Varma'
author = 'Penmatsa Tanoj Pavan Surya Varma'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',      # Generate docs from docstrings
    'sphinx.ext.napoleon',      # Support Google-style docstrings
    'sphinx.ext.viewcode',      # Add links to source code
    'nbsphinx',                 # Support Jupyter notebooks
    'myst_parser',              # Support Markdown files
]

# Napoleon settings for Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}
autodoc_typehints = 'description'
autodoc_member_order = 'bysource'

# HTML output options
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# HTML static path
html_static_path = ['_static']

# Output file base name for HTML help builder
htmlhelp_basename = 'WeatherToolsdoc'

# ReadTheDocs specific settings
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    # On ReadTheDocs, we need to ensure the package is installed
    import subprocess
    subprocess.call('pip install -e .', shell=True)

# The suffix of source filenames
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

# Language
language = 'en'

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False
