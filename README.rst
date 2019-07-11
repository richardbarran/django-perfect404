django-perfect404
=================

.. image:: https://img.shields.io/pypi/v/django-perfect404.svg
    :target: https://pypi.python.org/pypi/django-perfect404/
    :alt: Latest PyPI version

Easy to install perfect 404 page, based on `A List Apart's article<http://www.alistapart.com/articles/perfect404/>`_.

The main goal of this small project — to provide a simple but flexible
way to add an excellent 404 page, which handles referers, broken links,
searches from different engines, etc..

Installation
------------

* Place somewhere in your python path or install using `easy_install django-perfect404`.
* Add `perfect404` to the INSTALLED_APPS.
* Add `handler404 = 'perfect404.views.page_not_found'` to the `urls.py`.

Customization
-------------

If you want to customize your 404 page, then override template 'perfect404.html'. It's
context contains following variables:

  * `request_path` -- page's location.
  * `referer` -- URL of the page that refer to the missing one. This variable can be empty
    string in case if user entered the URL by hand.
  * `internal` -- boolean variable which is True if broken link is internal.
  * `contact` -- dict with two keys: 'name' and 'email'. These are taken from settings.ADMINS[0].

TODO
----

* Add support for search engine referrals and custom links output.

Contribution
------------

`Clone this project on GitHub <http://github.com/svetlyak40wt/django-perfect404/>`_ and don't
forget to send me patches! :-)
