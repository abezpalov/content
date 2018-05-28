from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,    {'fields': ['title', 'alias', 'content']}),
        ('Preview', {'fields': ['intro', 'img_path']}),
        ('Publish', {'fields': ['state', 'description']}),
        ('Hystory', {'fields': ['created_at', 'edited_at', 'published_at']}),
    ]

admin.site.register(Article, ArticleAdmin)
