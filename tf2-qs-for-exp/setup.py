"""
Python package setup file.
"""

from setuptools import setup

setup(
    name='tf2-qs-for-exp',
    version='1.0.0',
    scripts=['tf2-qs-for-exp.py'],
    install_requires=[
        "ssl",
    ],
    extras_require={'tensorflow': ['tensorflow'],
                    'tensorflow with gpu': ['tensorflow-gpu']},
)
