Django Simple Links
===================

.. image:: https://secure.travis-ci.org/kplaube/django-simple-links.png
    :target: https://travis-ci.org/kplaube/django-simple-links
.. image:: https://coveralls.io/repos/kplaube/django-simple-links/badge.png
    :target: https://coveralls.io/r/kplaube/django-simple-links
.. image:: https://badge.fury.io/py/django-simple-links.png
    :target: http://badge.fury.io/py/django-simple-links
.. image:: https://pypip.in/d/django-simple-links/badge.png
    :target: https://crate.io/packages/django-simple-links/

**Django Simple Links** is a pluggable application that helps you to add
a blogroll to projects wrote in Django.


Installation & Configuring
--------------------------

You can use pip to install the app:

``pip install django-simple-links``

After that, add ``'simple_links'`` to ``INSTALLED_APPS`` in your project's
settings.py. Finally, run the ``syncdb`` to add the tables to the database.


Usage
-----

* **In the admin:** add a category called "blogroll" and a few links within this category.
* **In your template:** load ``link_list`` and call ``{% get_link_list "blogroll" as links, category %}``

``blogroll`` is the category's slug, ``links`` is the variable that will store your links and category is the variable that will store the category object. So you can handle it in "Django way", like this::

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

That's all.
