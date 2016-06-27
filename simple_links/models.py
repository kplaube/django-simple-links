# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from simple_links import managers


class Category(models.Model):
    """
    A category for links.
    """
    title = models.CharField(_('Title'), max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(_('Active'), default=True)

    objects = models.Manager()
    actives = managers.CategoryActiveManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('title', )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Link(models.Model):
    """
    A link entry for blogrolls and similar.
    """
    category = models.ForeignKey(Category, verbose_name=_('Category'))
    title = models.CharField(_(u'Title'), max_length=100)
    description = models.TextField(_(u'Description'), blank=True, null=True)
    href = models.URLField(_(u'Address'))
    is_active = models.BooleanField(_('Active'), default=True)

    objects = models.Manager()
    actives = managers.LinkActiveManager()

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        ordering = ('category__title', 'title', )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
