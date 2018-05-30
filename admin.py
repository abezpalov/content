from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,    {'fields': ['title', 'alias', 'content']}),
        ('Preview', {'fields': ['intro', 'img_path']}),
        ('Publish', {'fields': ['author', 'state', 'description']}),
    ]

admin.site.register(Article, ArticleAdmin)
