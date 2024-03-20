import tweepy

# twitter api credentials
from config import consumer_key, consumer_secret, access_token, access_token_secret

# authenticate twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def post(proposal):
    message = f'{proposal["title"]}\n\n{proposal["notice_id"]}\n\nPublished Date: {proposal["date"]}'
    second_message = f'Description:\n{proposal["description"]}\n\nLink: {proposal["link"]}'

    print(f"first tweet:\n{message}")
    print()
    print(f"second tweet:\n{second_message}")
