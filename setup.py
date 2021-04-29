from setuptools import setup, find_packages

setup(
    name='django-perfect404',
    version=__import__('perfect404').__version__,
    description='Simple but perfect 404 page for django projects.',
    keywords='django apps webdev',
    license='New BSD License',
    author='Alexander Artemenko',
    author_email='svetlyak.40wt@gmail.com',
    url='http://github.com/richardbarran/django-perfect404/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['demo_project']),
    package_data={
        'templates': ['perfect404/templates/*.html'],
    },
    include_package_data=True,
    zip_safe=True,
)
