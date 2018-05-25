from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,    {'fields': ['title', 'alias', 'intro', 'content']}),
        ('Image', {'fields': ['img_path']}),
    ]

admin.site.register(Article, ArticleAdmin)

