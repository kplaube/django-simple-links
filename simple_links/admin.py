from django.contrib import admin

from simple_links.models import Category, Link


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'category', 'is_active', )
    search_fields = ('title', 'description', )
    list_filter = ('category', 'is_active', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
