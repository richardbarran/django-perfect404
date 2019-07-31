django-perfect404
=================

.. image:: https://img.shields.io/pypi/v/django-perfect404.svg
    :target: https://pypi.python.org/pypi/django-perfect404/
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/richardbarran/django-perfect404.svg?branch=master
    :target: https://travis-ci.org/richardbarran/django-perfect404

.. image:: https://coveralls.io/repos/github/richardbarran/django-perfect404/badge.svg?branch=master
    :target: https://coveralls.io/github/richardbarran/django-perfect404?branch=master


A easy to install perfect 404 page, based on `A List Apart's article <http://www.alistapart.com/articles/perfect404/>`_.

The main goal of this small project is to provide a simple way to add a clean 404 page,
which handles referers, broken links, searches from different engines, etc..

Installation
------------

Install::

    pip install django-perfect404

Add to ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
         # ...other installed applications,
         'perfect404',
    )
    
Finally, add to the base ``urls.py`` of your project::

    handler404 = 'perfect404.views.page_not_found'

Customization
-------------

If you want to customize your 404 page, then override template ``perfect404.html``. Its
context contains the following variables:

* ``request_path``: page's location.
* ``referer``: URL of the page that refer to the missing one. This variable can be empty
  string in case if user entered the URL by hand.
* ``internal``: boolean variable which is True if broken link is internal.
* ``contact``: dict with two keys: ``name`` and ``email``. These are taken from ``settings.ADMINS[0]``.

TODO
----

* Add support for search engine referrals and custom links output.
* This app needs ``Sites`` to be installed - we need to remove this dependency.
* The 404 template needs cleaning.

Contribution
------------

Clone this project on GitHub and don't forget to send in patches! :-)
