import tweepy
from .models import ApiKeys


#Code pour obtenir un jetons pour acceder a un compte

API_INFO= ApiKeys.objects.first()


def ApiInformations(API_INFO):
    try:
        
        api_keys =API_INFO.api_keys
        api_secret =  API_INFO.api_secrets
        auth = tweepy.OAuth1UserHandler(api_keys, api_secret)

        redirect = auth.get_authorization_url()
        
        return redirect, auth
    except:
        return None

def redirectTwitterPage():
    if ApiInformations(API_INFO) is not None:
        redi  = ApiInformations(API_INFO)
        return redi[0]


def exchange_code_for_acces_token(code):
    if ApiInformations(API_INFO):
        #Authentification get
        Auth[1] = ApiInformations(API_INFO)
        auth = Auth[1]
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

def sendTwitterTweet(key, secret, token, token_secret, media, post):
    auth = tweepy.OAuth1(key, secret, token, token_secret)
    api = tweepy.API(auth)
    try:
        if media or post:
            media_root = f'../media/{media}'
            media_image = api.media_upload(media_root)
            texte_tweet = post
            return api.update_status(status=texte_tweet, media_ids=[media.media_id])
        elif post:
            texte_tweet = post
            return api.update_status(status=texte_tweet)
        elif media:
            return api.update_status(status=" ", media_ids=[media.media_id])
        else:
            return None
        
        
    except:
        return None


    