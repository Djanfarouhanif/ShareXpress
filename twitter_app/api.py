import tweepy
from .models import ApiKeys


#Code pour obtenir un jetons pour acceder a un compte

API_INFO= ApiKeys.objects.first()


def ApiInformations(API_INFO):
    try:
        
        api_keys =API_INFO.api_keys
        api_secret =  API_INFO.api_secrets
        print(api_keys)
        auth = tweepy.OAuth1UserHandler(api_keys, api_secret)

        redirect = auth.get_authorization_url()
        
        print(redirect)

        return redirect, auth
    except:
        return None

def redirectTwitterPage():
    return ApiInformations(API_INFO)

def exchange_code_for_acces_token(code):
    redirec, auth =redirectTwitterPage()
    try:

        access_token_url = 'https://api.twitter.com/oauth/access_token'
        access_token_response = auth.fech.access_token(access_token_url, verifer=code)

        #Recuper les jeton d'acces partire de la response
        access_token = access_token_response['oauth_token']
        access_token_secret = access_token_response['oauth_token_secret']

        if acces_token and access_token_secret:
            return access_token, access_token_secret
        else:
            return None
    except:
        return None