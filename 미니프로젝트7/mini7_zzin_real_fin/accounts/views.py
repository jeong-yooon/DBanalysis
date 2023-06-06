from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        if (request.POST['password1'] == request.POST['password2']) and request.POST['password1'] != "" and request.POST['username'] != "" and request.POST['email'] != "":
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'acc/signup.html')
    return render(request, 'acc/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'acc/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'acc/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request, 'index.html')