import json
import os
import tweepy
from datetime import datetime

# twitter api credentials
from config import consumer_key, consumer_secret, bearer_token, access_token, access_token_secret 

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

# post new proposals to twitter
def post():
    # load the proposals from the json file
    with open("proposals.json", "r") as f:
        proposals = json.load(f)

    # load the posted proposals from the json file (if it exsits)
    posted_proposals_file = "posted_proposals.json"
    if os.path.exists(posted_proposals_file):
        with open(posted_proposals_file, "r") as f:
            posted_proposals = set(json.load(f))
    else:
        posted_proposals = set()

    # iterate over the proposals and post new ones
    for proposal in proposals:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if proposal["notice_id"] not in posted_proposals:
            first_message = f"{proposal['title']}\n\n{proposal['notice_id']}\n\nPublished Date: {proposal['date']}"
            second_message = f"Description:\n{proposal['description']}\n\nLink: {proposal['link']}"

            try:
                # post first tweet 
                first_tweet  = client.create_tweet(text=first_message)
                first_tweet_id = first_tweet.data["id"]

                # post second tweet as a reply to first tweet
                second_tweet = client.create_tweet(text=second_message, in_reply_to_tweet_id=first_tweet_id)

                # update the set of posted proposals
                posted_proposals.add(proposal['notice_id'])

                # save the updated set of posted proposals to the json file
                with open(posted_proposals_file, "w") as f:
                    json.dump(list(posted_proposals), f)
                    
                print(f"{current_time}: Posted new proposal: {proposal['title']}")

            except tweepy.TweepyException as e:
                print(f"{current_time}: Error posting proposal: {proposal['title']}")
                print(f"Error: {str(e)}")
        else: print(f"{current_time}: No new proposals")

