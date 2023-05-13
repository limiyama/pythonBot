#!/usr/bin/env python
import tweepy

#from our keys module (keys.py), import the keys dictionary

print("o bot está rodando!!")

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

FILE_NAME = 'last.txt'
api = tweepy.API(auth)

def check_mentions(api, keywords, since_id):
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,

        since_id = since_id).items():

        new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is not None:

            continue


        print('procurando menções')
        if any(keyword in tweet.text.lower() for keyword in keywords):

            print('respondendo...')

            if not tweet.user.following:

                tweet.user.follow()

            api.update_status ( status='alo',
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    since_id = 1

    while True:

        since_id = check_mentions(api, ['texto especifico'], since_id)

main()
