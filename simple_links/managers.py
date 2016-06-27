from django.db import models


class CategoryActiveManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        """
        Filter a queryset with is_active as True.
        """
        qs = super(CategoryActiveManager, self).get_queryset(*args, **kwargs)
        return qs.filter(is_active=True)


class LinkActiveManager(CategoryActiveManager):
    def get_queryset(self, *args, **kwargs):
        """
        Filter a queryset with is_active of category model as True.
        """
        qs = super(LinkActiveManager, self).get_queryset(*args, **kwargs)
        return qs.filter(category__is_active=True)
