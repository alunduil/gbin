# Copyright (C) 2013 by Alex Brandt <alunduil@alunduil.com>
#
# gbin is freely distributable under the terms of an MIT-style license.
# See COPYING or http://www.opensource.org/licenses/mit-license.php.

# -----------------------------------------------------------------------------
import sys
import traceback

if sys.version_info.major < 3:
    import ConfigParser
    configparser_name = 'ConfigParser'
else:
    import configparser
    configparser_name = 'configparser'

original_sections = sys.modules[configparser_name].ConfigParser.sections

def monkey_sections(self):
    '''Return a list of sections available; DEFAULT is not included in the list.

    Monkey patched to exclude the nosetests section as well.

    '''

    _ = original_sections(self)

    if any([ 'distutils/dist.py' in frame[0] for frame in traceback.extract_stack() ]) and _.count('nosetests'):
        _.remove('nosetests')

    return _

sys.modules[configparser_name].ConfigParser.sections = monkey_sections
# -----------------------------------------------------------------------------

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

from gbin import information

PARAMS = {}

PARAMS['name'] = information.NAME
PARAMS['version'] = information.VERSION
PARAMS['description'] = information.DESCRIPTION

with open('README.rst', 'r') as fh:
    PARAMS['long_description'] = fh.read()

PARAMS['author'] = information.AUTHOR
PARAMS['author_email'] = information.AUTHOR_EMAIL
PARAMS['url'] = information.URL
PARAMS['license'] = information.LICENSE

PARAMS['classifiers'] = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Software Distribution',
        ]

PARAMS['keywords'] = [
        'gbin',
        'gentoo',
        'package',
        'emerge',
        'ebuild',
        'portage',
        'binary',
        ]

PARAMS['provides'] = [
        'gbin',
        ]

with open('requirements.txt', 'r') as req_fh:
    PARAMS['install_requires'] = req_fh.readlines()

with open('test_gbin/requirements.txt', 'r') as req_fh:
    PARAMS['tests_require'] = req_fh.readlines()

PARAMS['test_suite'] = 'nose.collector'

PARAMS['packages'] = [
        'gbin',
        ]

PARAMS['data_files'] = [
        ('share/doc/{P[name]}-{P[version]}'.format(P = PARAMS), [
            'README.rst',
            ]),
        ]

setup(**PARAMS)
