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

Clone [this project on GitHub][github] and dont't forget to send me patches! :-)

[github]: http://github.com/svetlyak40wt/django-perfect404/
[article]: http://www.alistapart.com/articles/perfect404/


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/svetlyak40wt/django-perfect404/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

