#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Paulo Henrique Silva <ph.silva@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

METADATA = {
    'name': 'pcb-tools-extension',
    'version': "0.1.1",
    'author': 'Hiroshi Murayama <opiopan@gmail.com>',
    'author_email': "opiopan@gmail.com",
    'description': ("Extension for pcb-tools package to panelize gerber files"),
    'license': "Apache",
    'keywords': "pcb gerber tools extension",
    'url': "http://github.com/opiopan/pcb-tools-extension",
    'packages': ['gerberex'],
    'long_description': read('README.md'),
    'classifiers':[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language:: Python:: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
}

SETUPTOOLS_METADATA = {
    'install_requires': ['pcb-tools', 'dxfgrabber'],
}


def install():
    """ Install using setuptools, fallback to distutils
    """
    try:
        from setuptools import setup
        METADATA.update(SETUPTOOLS_METADATA)
        setup(**METADATA)
    except ImportError:
        from sys import stderr
        stderr.write('Could not import setuptools, using distutils')
        stderr.write('NOTE: You will need to install dependencies manualy')
        from distutils.core import setup
        setup(**METADATA)

if __name__ == '__main__':
    install()
