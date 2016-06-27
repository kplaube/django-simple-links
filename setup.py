from setuptools import setup
from simple_links import get_version


setup(
    name='django-simple-links',
    version=get_version(),
    license='GNU Lesser General Public License (LGPL), Version 3',

    description='Simple bookmarking application for Django projects',
    long_description=('Simple Links is a pluggable app that '
                      'that lets you easily add links in your Django project.'),
    keywords='django apps links bookmark',

    author='Klaus Laube',
    author_email='kplaube@gmail.com',

    url='https://github.com/kplaube/django-simple-links',
    packages=['simple_links',
              'simple_links.templatetags', ],
    include_package_data=True,
    zip_safe=False,

    classifiers=[
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
