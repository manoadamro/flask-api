# coding: utf-8

import setuptools


NAME = 'flask-api'
VERSION = '0.0.0'
REQUIRES = [
    'flask',
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    install_requires=REQUIRES,
    packages=setuptools.find_packages()
)
