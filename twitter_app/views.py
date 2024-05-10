from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .api import redirectTwitterPage, exchange_code_for_acces_token
from .models import ApUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serialzer import UserSerializer

auth = redirectTwitterPage()
print(auth)
@csrf_exempt
def index(request):
    apUser  = ApUser.objects.get(user=request.user)
    if request.method == 'POST':
        #Recuper les token de l'utisateur
        Code_verification = request.POST.get("code", None)
        access_token, access_token_secret = exchange_code_for_acces_token(Code_verification)

        apUser.twitter_access_token = access_token
        apUser.twitter_access_secret = access_token_secret
        apUser.save()
        return JsonResponse({'succes':True})

    return JsonResponse({"error": 'Method Not Allowed'}, status=405)


@csrf_exempt
def signup(request):
    if reqeust.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get("passowrd", None)
        password2 = request.POST.get('password2', None)

        if len(password) < 7 :
            
            return JsonResponse({"erreur": "password is not securite"}, status=400)
        elif password != passowrd2:
            #signup page
            return JsonResponse({"erreur": "Password not macthing"}, status=400)
        elif User.objects.filter(email=email).exists():
            #email exists
            return JsonResponse({'erreure', 'Email exists alredy'}, status=400)
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()

            user_login = User.objects.get(username=new_user.username, email=new_user.email)
            auth = authenticate(request, user_login)
            if auth is not None:
                login_user = login(request, user_login.username, user_login.password)

                new_apUser = ApUser.objects.create(user=new_user)
                new_apUser.save()
                return  JsonResponse({'data':f"{redirectTwitterPage()}"}, status=200)
            else:
                #message erreure  connections
                return JsonResponse({"erreur": "Error authenticating user"}, status=400)
    #return signup page
    else:
        return JsonResponse({"erreur": "Method Not Allowed"}, status=405)
            

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        passowrd = request.POST.get('password', None)

        auth = authenticate(request, username=username, password=password)

        if auth is not None:
            login(request, auth)
            #return page d'acc
            return JsonResponse({"succes": "user authenticate"}, status=200)
        else: 
            #meessage
            return JsonResponse({'erreure': "Error authenfications user"}, status=400)
    return JsonResponse({"erreur": "Method Not Allowed"}, status=405)

def logout(request):
    logout(request)
    return ResponseJson({'succes':" User logour"}, status=200)
