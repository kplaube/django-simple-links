import re
from django import template
from simple_links.models import Link

register = template.Library()


class LinkListNode(template.Node):
    def __init__(self, category_slug, links_var_name, category_var_name):
        self.category_slug = category_slug
        self.links_var_name = links_var_name
        self.category_var_name = category_var_name

    def render(self, context):
        links = (Link.actives.filter(category__slug=self.category_slug)
            .select_related())

        if links:
            category = links[0].category
        else:
            category = None

        context[self.links_var_name] = links
        context[self.category_var_name] = category
        return ''


@register.tag('get_link_list')
def do_link_list(parser, token):
    """
    Using category slug as parameter returns a list of links and a
    category instance.

    Usage:: 

        {% load link_list %}
        {% get_link_list "blogroll" as links, category %}

        <h3>{{ category.title }}<h3>
        <ul>
        {% for link in links %}
            <li><a href="{{ link.get_absolute_url }}">
                {{ link.title }}</a></li>
        {% endfor %}
        </ul>
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise (template.TemplateSyntaxError("%r tag requires arguments"\
            % token.contents.split()[0]))

    m = re.search(r'"(.*?)" as (\w+),\s?(\w+)', arg)
    if not m:
        raise (template.TemplateSyntaxError("%r tag has invalid arguments"\
            % tag_name))

    category_slug, links_var, category_var = m.groups()
    return LinkListNode(category_slug, links_var, category_var)
