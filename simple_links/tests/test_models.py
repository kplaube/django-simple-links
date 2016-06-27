from django.test import TestCase
from simple_links.models import Category, Link


class BaseLinksTests(TestCase):
    """
    An abstract base class that provides basic instructions to tests.
    """
    fixtures = ['links_testdata.json', ]

    def setUp(self):
        self.category = Category.objects.get(pk=1)


class CategoryModelTests(BaseLinksTests):
    def test_repr(self):
        """
        Should return a representation of the object.
        """
        self.assertEquals(str(self.category), '1st Category')

    def test_bring_only_active(self):
        """
        Should bring only active categories.
        """
        self.category.is_active = False
        self.category.save()

        self.assertEquals(len(Category.actives.all()), 1)


class LinkModelTests(BaseLinksTests):
    def test_repr(self):
        """
        Should return a representation of the object.
        """
        link = Link.objects.get(pk=1)
        self.assertEquals(str(link), '1st Link')

    def test_bring_only_active(self):
        """
        Should bring only active links.
        """
        # Test link is_active property
        self.assertEquals(len(Link.actives.all()), 3)

        # Test category is_active property
        self.category.is_active = False
        self.category.save()
        self.assertFalse(len(Link.actives.all()))
