from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    content = 'index test content'

    return render(request, 'content/index.html', locals())
