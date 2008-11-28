django-perfect404
=================

Easy to install perfect 404 page, based on [A List Apart's article][article].

The main goal of this small project — to provide a simple but flexible
way to add an excellent 404 page, which handles referers, broken links,
searches from different engines, etc..

Installation
------------

* Place somewhere in your python path or install using `easy_install django-perfect404`.
* Add `perfect404` to the INSTALLED_APPS.
* Add `handler404 = 'perfect404.views.page_not_found'` to the `urls.py`.

TODO
----

* Add support for search engine referrals and custom links output.

Contribution
------------

Clone [this project on GitHub][github] and dont't forget to send me patches! :-)

[github]: http://github.com/svetlyak40wt/django-perfect404/
[article]: http://www.alistapart.com/articles/perfect404/
