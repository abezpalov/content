from django.conf import settings
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse # without templates

from .models import *


def index(request):

    site_name = settings.SITE_NAME

    # TODO
    content = 'index test content'

    return render(request, 'content/index.html', locals())


def article_by_alias(request, alias):

    site_name = settings.SITE_NAME

    try:
        article = Article.objects.get(alias = alias)
    except Article.DoesNotExist:
        raise Http404('Ошибка! Статья не найдена.')

    return render(request, 'content/article.html', locals())
