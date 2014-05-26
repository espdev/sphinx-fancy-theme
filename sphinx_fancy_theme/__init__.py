"""
Sphinx Fancy Theme

A readable and airy sphinx-doc theme for comfortable reading.

"""

import os

__version__ = '1.0.0'


def get_html_theme_path():
    """Return path to directory containing package theme."""
    return [os.path.abspath(os.path.dirname(__file__))]
