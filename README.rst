Django Simple Links
===================

**Django Simple Links** is a pluggable application that helps you to add 
a blogroll to projects wrote in Django.


Installation & Configuring
--------------------------

You can use pip to install the app:

``pip install django-simple-contact``

After that, add ``'simple_links'`` to ``INSTALLED_APPS`` in your project's
settings.py. Finally, run the ``syncdb`` to add the tables to the database.


Usage
-----

* **In the admin:** add a category called "blogroll" and a few links within this category.
* **In your template:** load the ``get_link_list`` template tag and call ``{% get_link_list "blogroll" as links, category %}``

``blogroll`` is the category's slug, ``links`` is the variable that will store your links and category is the variable that will store the category object. So you can handle it in "Django way", like this::

            {% get_link_list "blogroll" as links, category %}
            {% if links %}
                <div class="module">
                    <h3 class="title">{{ category.title }}</h3>
                    <ul>
                        {% for link in links %}
                            <li>
                                <a href="{{ link.get_absolute_url }}" 
                                title="{{ link.description|safe }}">{{ link.title }}</a>
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            {% endif %}

That's all.
