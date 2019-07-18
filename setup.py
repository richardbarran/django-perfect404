from setuptools import setup, find_packages

setup(
    name = 'django-perfect404',
    version = __import__('perfect404').__version__,
    description = 'Simple but perfect 404 page for django projects.',
    keywords = 'django apps webdev',
    license = 'New BSD License',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/django-perfect404/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(exclude=['demo_project']),
    package_data = {
        'templates': ['*.html'],
    },
    include_package_data = True,
    zip_safe = True,
)

