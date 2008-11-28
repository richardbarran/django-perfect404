django-perfect404
=================

Easy to install perfect 404 page, based on [A List Apart's article][article].

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
