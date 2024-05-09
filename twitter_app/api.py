import tweepy
from .models import ApiKeys


#Code pour obtenir un jetons pour acceder a un compte

API_INFO= ApiKeys.objects.first()


def ApiInformations(API_INFO):
    try:
        
        api_keys =API_INFO.api_keys
        print(f"****{api_keys}*******")
        api_secret =  API_INFO.api_secrets
        print(api_keys)
        auth = tweepy.OAuth1UserHandler(api_keys, api_secret)

        redirect = auth.get_authorization_url()
        
        print(redirect)

        return redirect
    except:
        return None

def redirectTwitterPage():
    return ApiInformations(API_INFO)