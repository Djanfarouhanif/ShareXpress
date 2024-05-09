from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .api import redirectTwitterPage





def index(request):
    pass

def signup(request):
    if reqeust.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get("passowrd", None)
        password2 = request.POST.get('password2', None)

        if len(password) < 7 :
            #pass is Shorte
            return 
        elif password != passowrd2:
            #signup page
            return 
        elif User.objects.filter(email=email).exists():
            #email exists
            return 
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()

            user_login = User.objects.get(username=new_user.username, email=new_user.email)
            auth = authenticate(request, user_login)
            if auth is not None:
                login_user = login(request, user_login.username, user_login.password)

                #redriec twiter
                return 
            else:
                #message erreure  connections
                return 
    #return signup page
            

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        passowrd = request.POST.get('password', None)

        auth = authenticate(request, username=username, password=password)

        if auth is not None:
            login(request, auth)
            #return page d'acc
            return 
        else: 
            #meessage
            return 

def logout(request):
    logout(request)
    return redirect()
