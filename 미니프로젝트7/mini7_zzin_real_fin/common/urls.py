# blog/urls.py
from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('', views.index, name='index'),
]
