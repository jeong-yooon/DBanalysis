"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

# def index(req):
#     html = """<!doctype html>
#     <html>
#     <head>
#     <title>Django</title>
#     <meta charset="utf-8">
#     </head>
#     <body>
#     <h1><a href="/">Django</a></h1>
#     <ol>
#     <li><a href="/chapter01/">Setting & Deploy</a></li>
#     <li><a href="/chapter02/">Routing & View</a></li>
#     </ol>
#     <h2>Django</h2>
#     <p><a href="https://www.djangoproject.com/" target="_blank">Django</a>는
#     Python으로 작성된 오픈 소스 웹 프레임워크로, 빠르고 쉬운 웹 개발을 가능하게 합니다.
#     </p>
#     </body>
#     </html>"""
#     return HttpResponse(html)

# def list(request):
#  return HttpResponse("List")

# def post(request, id):
#  return HttpResponse(f"Post {id}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', views.list),
    path('blog/post/<id>/', views.post),
    path('blog/gugu/<num>/', views.gugu),
    path('naver/', views.naver),
]