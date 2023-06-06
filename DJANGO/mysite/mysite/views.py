from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import views

html = """<!doctype html>
    <html>
    <head>
    <title>Django</title>
    <meta charset="utf-8">
    </head>
    <body>
    <h1><a href="/">Django</a></h1>
    <ol>
    <li><a href="/chapter01/">Setting & Deploy</a></li>
    <li><a href="/chapter02/">Routing & View</a></li>
    </ol>
    <h2>Django</h2>
    <p><a href="https://www.djangoproject.com/" target="_blank">Django</a>는
    Python으로 작성된 오픈 소스 웹 프레임워크로, 빠르고 쉬운 웹 개발을 가능하게 합니다.
    </p>
    </body>
"""

chapters = {
 "01": {"title": "Setting & Deploy" , "content": "Setting & Deploy is ..." },
 "02": {"title": "Routing & View" , "content": "Routing & View is ..." },
}

def index(req):
    d = {'title': 'django', 'content': 'django is...'}
    return HttpResponse( html.format(**d))
    
def chapter(req, id):
 return HttpResponse( html.format(**chapters.get(id)))

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def search(request):
 print(request.method)
 print(f"Query String: {request.GET.get( 'q')}")
 print(f"BODY: {request.POST.get( 'key', '')}")
 return HttpResponse( f'search')
