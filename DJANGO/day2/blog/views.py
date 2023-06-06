# blog/views.py
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
def post_list(req: HttpRequest) -> HttpResponse:
 posts = [
 {'id': 1, 'title': 'html', 'content': 'html is ...'},
 {'id': 2, 'title': 'css', 'content': 'css is ...'},
 {'id': 3, 'title': 'javascript',
 'content': 'javascript is ...'},
 ]
 return render(req, 'blog/index.html', { 'post_list': posts })