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
from .code import scripts

scripts(redirectTwitterPage())

@api_view(['POST'])
def index(request, pk):
    apiKeys = ApiKeys.objects.first()
    apUser  = ApUser.objects.get(id=pk)

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


@api_view(['POST'])
def profile(request):
    if request.method == 'POST':
        #Recuper les token des Api
        #Token de Twitre------------------------------------------------:
        code_verification = request.POST.get("code", None)
        access_token, access_token_secret = exchange_code_for_acces_toke(code_verification)
        apUser = ApUser.objects.create(twitter_access_token=access_token, twitter_access_secret=access_token_secret)
        apUser.save()

        return Response({"succes":True}, status=200)
    else:
        return Response({"error": "Method Not Allowed"}, status=405)






