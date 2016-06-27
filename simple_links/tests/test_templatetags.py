from django.test import TestCase
from simple_links.models import Link
from simple_links.templatetags.link_list import LinkListNode


class LinksTemplatetagsTests(TestCase):
    fixtures = ['links_testdata.json', ]

    def test_link_list(self):
        """
        Should return a list of links used in templates.
        """
        # By category
        link = Link.objects.get(pk=4)
        link.category.is_active = True
        link.is_active = True
        link.save()

        context = {}
        node = LinkListNode(link.category.slug, 'links', 'category')
        node.render(context)
        self.assertEquals(len(context['links']), 1)
        self.assertEquals(context['links'][0], link)
        self.assertEquals(context['category'], link.category)

        # Wrong category slug
        context = {}
        node = LinkListNode('lipsum', 'links', 'category')
        node.render(context)
        self.assertFalse(context['links'])
        self.assertFalse(context['category'])
