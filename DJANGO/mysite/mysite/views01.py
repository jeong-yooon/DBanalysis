from django.http import HttpResponse

def index(request):
 return HttpResponse( "Hello")

def list(request):
 return HttpResponse( "List")

def post(request, id):
 return HttpResponse( f"Post {id}")

def gugu(request, num):
    num = int(num)
    gugudan = [f"{num} * {i} = {num * i}" for i in range(1, 10)]
    print(gugudan)
    print("\n".join(gugudan))
    return HttpResponse( "<br>".join(gugudan))

def naver(req):
    import requests
    res = requests.get('https://www.naver.com')
    return HttpResponse(res.content)

# <img src="/img.jpg">