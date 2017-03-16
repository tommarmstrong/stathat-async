#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = ['requests==2.13.0']

setup(
    name='stathat-async',
    version='0.0.3',
    description='A simple multithreaded async API wrapper for StatHat.com',
    author='Jamie Matthews',
    author_email='jamie.matthews@gmail.com',
    url='https://github.com/j4mie/stathat-async',
    py_modules= ['stathatasync'],
    install_requires=required,
    license='MIT',
)
