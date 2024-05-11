from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .api import redirectTwitterPage, exchange_code_for_acces_token, sendTwitterTweet
from .models import ApUser, ApiKeys
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serialzer import UserSerializer
from django.contrib.auth.decorators import  login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required(login_url="signin")
@api_view(['POST'])
def index(request):
    apiKeys = ApiKeys.objects.first()
    apUser  = ApUser.objects.get(user=request.user)

    api_keys = apiKeys.api_keys
    api_secrets = apiKeys.api_secrets
    access_token = apUser.twitter_access_token
    access_token_secret = apUser.twitter_access_secret
    if request.method == 'POST':
        post = request.POST.get("post", None)
        if request.FILES.get('post_image'):
            post_image = request.FILES.get("post_image")
        else:
            post_image = None

    #Fonction for send post sendTwitterTweet()
        post = sendTwitterTweet(api_keys, api_secrets, access_token, access_token_secret, post, post_image)
        return Response({"succes": "Opertions success"}, status=200)
    else:
        return Response({"error": "message not send"}, status=400)

    

@csrf_exempt
@api_view(['POST'])
def profile(request):
    apUser = ApUser.objects.get(user=request.user)
    if request.method == 'POST':
        #Recuper les token des Api
        #Token de Twitre------------------------------------------------:
        code_verification = request.POST.get("code", None)
        access_token, access_token_secret = exchange_code_for_acces_toke(code_verification)
        
        apUser.twitter_access_token = access_token
        apUser.twitter_access_secret = access_token_secret
        apUser.save()

        return Response({"succes":True}, status=200)
    else:
        return Response({"error": "Method Not Allowed"}, status=405)

@api_view(['POST'])
def signup(request):
    if reqeust.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get("passowrd", None)
        password2 = request.POST.get('password2', None)

        if len(password) < 7 :
            
            return Response({"erreur": "password is not securite"}, status=400)
        elif password != passowrd2:
            #signup page
            return Response({"erreur": "Password not macthing"}, status=400)
        elif User.objects.filter(email=email).exists():
            #email exists
            return Response({'erreure', 'Email exists alredy'}, status=400)
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()

            user_login = User.objects.get(username=new_user.username, email=new_user.email)
            auth = authenticate(request, user_login)
            if auth is not None:
                login_user = login(request, user_login.username, user_login.password)

                new_apUser = ApUser.objects.create(user=new_user)
                new_apUser.save()
                return  Response({'data':f"{redirectTwitterPage()}"}, status=200)
            else:
                #message erreure  connections
                return Response({"erreur": "Error authenticating user"}, status=400)
    #return signup page
    else:
        return Response({"erreur": "Method Not Allowed"}, status=405)
            
@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        passowrd = request.POST.get('password', None)

        auth = authenticate(request, username=username, password=password)

        if auth is not None:
            login(request, auth)
            #return page d'acc
            return Response({"succes": "user authenticate"}, status=200)
        else: 
            #meessage
            return Response({'erreure': "Error authenfications user"}, status=400)
    return Response({"erreur": "Method Not Allowed"}, status=405)

@login_required(login_url='signin')
@api_view(['GET'])
def logout(request):
    logout(request)
    return Response({'succes':" User logour"}, status=200)
