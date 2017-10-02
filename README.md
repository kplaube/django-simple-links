# Django Simple Links

[![Build Status](https://travis-ci.org/kplaube/django-simple-links.svg?branch=master)](https://travis-ci.org/kplaube/django-simple-links)
[![Coverage Status](https://coveralls.io/repos/github/kplaube/django-simple-links/badge.svg?branch=master)](https://coveralls.io/github/kplaube/django-simple-links?branch=master)
[![PyPI version](https://badge.fury.io/py/django-simple-links.svg)](https://badge.fury.io/py/django-simple-links)

A pluggable application for adding a list of links (like a blogroll)
to your Django project.

## Installing

You can install the app through `pip`:

    pip install django-simple-links

After that, add `simples_links` to `INSTALLED_APPS` in your
`settings.py`:

    INSTALLED_APPS = (
        ...
        'simple_links',
        ...
    )

Finally, run `syncdb`/`migrate` to add tables to the database.

## Usage

* **Admin interface:** Add a category called "blogroll" and a few links within this category.
* **In your template:** Load `link_list` and call `{% get_link_list "blogroll" as links, category %}`.

`blogroll` turns to be the category slug, `links` and `category` are variables that will keep those information
you've added through Admin interface:

    {% load link_list %}

    {% get_link_list "blogroll" as links, category %}

    {% if links %}
        <div class="module">
            <h3 class="title">{{ category.title }}</h3>
            <ul>
                {% for link in links %}
                    <li>
                        <a href="{{ link.href }}"
                            title="{{ link.description }}">{{ link.title }}</a>
                    </li>
                {% endfor %}
            </ul>
        </div>
    {% endif %}

That's all!

## Contributors

* [@pixelexel](https://github.com/pixelexel)
* [@gvangool](https://github.com/gvangool)

Contributions are very welcome.

## Changelog

### 0.1.4

* Fix `setup.py` by adding the `migrations` path to packages (thanks @gvangool)

### 0.1.3

* Updating documentation

### 0.1.2

* Maintaining compatibility with Django 1.4, 1.5, 1.6 and 1.7
* Suporting new versions of Django (1.8 and 1.9)
* Suporting Python 2.7 and Python 3.5
