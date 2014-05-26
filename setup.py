import os
from setuptools import setup

import sphinx_fancy_theme


def read_file(filename):
    """Open and a file, read it and return its contents."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()


setup(
    name='sphinx-fancy-theme',
    version=sphinx_fancy_theme.__version__,
    author='Evgeny Prilepin',
    author_email='esp.home@gmail.com',
    description='Sphinx Fancy Theme',
    long_description=read_file('README.rst'),
    url='https://github.com/espdev/sphinx-fancy-theme',
    license=read_file('LICENSE'),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Documentation',
    ],
    packages=['sphinx_fancy_theme'],
    include_package_data=True,
    zip_safe=False
)
