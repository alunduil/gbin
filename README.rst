Description
===========

Gentoo Binary Management Service

This software contains a web service that stores and manages binary packages 
for a heterogeneous set of Gentoo clients.

It also contains a client application and stock `cron.hourly` file for keeping
packages up to date for a client.

Installation
============

This package is available via portage using an overlay::
    layman -fo http://www.alunduil.com/svn/portage/trunk/alunduil-overlay.xml -a alunduil-overlay
    emerge gbin

If you would prefer to clone this package directly from git or assist with
development, the URL is https://github.com/alunduil/gbin and the current status
of the build is:

.. image:: https://secure.travis-ci.org/alunduil/gbin.png?branch=master
    :target: http://travis-ci.org/alunduil/gbin

Usage
=====

Usage of this package is outlined in the included man pages:

* man 1 gbc
* man 8 gbd

Authors
=======

* Alex Brandt <aludnuil@alunduil.com>

Known Issues
============

Known issues can be found in the github issue list at
https://github.com/alunduil/gbin/issues.

Troubleshooting
===============

If you need to troubleshoot an issue or submit information in a bug report, we
recommend obtaining the following pieces of information:

* output with debug logging turned on in gbc or gbd
* any relevant stacktraces
