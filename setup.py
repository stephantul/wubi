#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wubi',
    version='1.0',
    description='Translate chinese chars to wubi',
    long_description=long_description,
    author='arcsecw',
    author_email='tob-wang@qq.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={
        '': ['LICENSE']},
    url='https://github.com/arcsecw/wubi',
    license="BSD",
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
