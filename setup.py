# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018, 2019 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA-Workflow-Engine-Yadage."""

from __future__ import absolute_import, print_function

import os
import re

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2,<4.3',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.4.4',
        'sphinx-rtd-theme>=0.1.9',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for key, reqs in extras_require.items():
    if ':' == key[0]:
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.7',
]

install_requires = [
    'adage==0.8.5',
    'celery>=4.1.0,<4.3',
    'click>=7,<8',
    'enum34>=1.1.6',
    'packtivity==0.10.0',
    'pyOpenSSL==17.5.0',  # FIXME remove once yadage-schemas solves deps.
    'reana-commons[kubernetes]>=0.5.0.dev20190402,<0.6.0',
    'requests==2.20.0',
    'rfc3987==1.3.7',  # FIXME remove once yadage-schemas solves deps.
    'strict-rfc3339==0.7',  # FIXME remove once yadage-schemas solves deps.
    'SQLAlchemy-Utils>=0.32.18',
    'SQLAlchemy>=1.1.14',
    'yadage-schemas==0.7.16',
    'yadage==0.13.5',
    'webcolors==1.7',  # FIXME remove once yadage-schemas solves deps.
]

packages = find_packages()


# Get the version string. Cannot be done with import!
with open(os.path.join('reana_workflow_engine_yadage',
                       'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='reana-workflow-engine-yadage',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    author='REANA',
    author_email='info@reana.io',
    url='https://github.com/reanahub/reana-workflow-engine-yadage',
    packages=['reana_workflow_engine_yadage', ],
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'run-yadage-workflow='
            'reana_workflow_engine_yadage.tasks:run_yadage_workflow',
        ]
    },
    extras_require=extras_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
