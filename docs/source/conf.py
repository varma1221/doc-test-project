# At the bottom of conf.py, add or update:
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# On ReadTheDocs, we need to import the package
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    # Install the package in development mode
    import subprocess
    subprocess.call('pip install -e .', shell=True)

# Theme - use ReadTheDocs theme for better integration
html_theme = 'sphinx_rtd_theme'  # Change from alabaster to this
