#!/usr/bin/env python
"""Python package setup file."""

from setuptools import setup

setup(
    name='CelebFaceMatcher',
    version='1.0.0',
    scripts=['CelebFaceMatcher.py'],
    license_files=('LICENSE',),
    install_requires=[
        'tensorflow',
        'numpy',
    ],
    extras_require={'tensorflow': ['tensorflow'],
                    'tensorflow with gpu': ['tensorflow-gpu']},
)
