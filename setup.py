#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


# version
here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'RaspberryModules',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev0')

setup(
    name="RaspberryModules",
    version=version,
    url='https://github.com/chizuchizu/pypipkg',
    author='chizuchizu',
    author_email='ochimasumi@gmail.com',
    maintainer='kinpira',
    maintainer_email='ochimasumi@gmail.com',
    description='For Raspberry pi',
    long_description=readme,
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    # entry_points="""
    #   # -*- Entry points: -*-
    #   [console_scripts]
    #   pkgdep = RaspberryModules.scripts.command:main
    # """,
)
