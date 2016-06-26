# Django Simple Links

[![Build Status](https://travis-ci.org/kplaube/django-simple-links.svg?branch=master)](https://travis-ci.org/kplaube/django-simple-links)
[![Coverage Status](https://coveralls.io/repos/github/kplaube/django-simple-links/badge.svg?branch=master)](https://coveralls.io/github/kplaube/django-simple-links?branch=master)
[![PyPI version](https://badge.fury.io/py/django-simple-links.svg)](https://badge.fury.io/py/django-simple-links)

A pluggable application for adding a list of links (like a blogroll)
to your Django project.

## Disclaimer

Unfortunately, `simple_links` doesn't support Django>=1.7 and Python>=3.
But we are working on making the app runs in the last versions of Python and Django.

## Installing

You can install the app through `pip`:

    pip install django-simple-links

After that, add `simples_links` to `INSTALLED_APPS` in your
`settings.py`. Finally, run `syncdb`/`migrate` for adding tables
to the database.

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

Contributions are very welcome.
