
# coding: utf-8

# In[5]:


import csv

datafile = 'data/sarcasm_detection_dataset.csv'

sarcastic = []
non_sarcastic = []

with open(datafile, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if (row[0] == "True"):
            sarcastic.append(tuple(row[1:]))

print ("Sarcastic tweets: %s" %(len(sarcastic)))


# In[3]:


import tweepy
from time import sleep

CONSUMER_KEY = "9yIxS8HjWWFPKaoZLHH59TI2t"
CONSUMER_SECRET = "wLbl8aCqzb6X0J6TjOgY2gYARLBor7JIzMc1Sh7t1EcdIp1bbm"
OAUTH_TOKEN = "912547733214347264-SFZtEUYxeLvUSFx1v3NVP1rb9dUJH8c"
OAUTH_TOKEN_SECRET = "NWYfIHTSadsYn5WSYdh8g7ZUwD6j3ksrYfv2iAkFbuLlk"

f1 = open('sarcastic.txt', 'w')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# In[4]:


tweet_delimiter = "|||||"
user_delimiter = "\n;;;;;\n"

i = 0
while i < len(sarcastic):
    try:
        # Try to retrieve the tweets corresponding to tweetIDs of user i
        full_tweets = api.statuses_lookup(sarcastic[i])  
        # Process further only if the first sarcastic tweet is retrieved
        success = False
        first_tweet_idx = 0
        for j, x in enumerate(full_tweets):
            if (x._json['id_str'] == sarcastic[i][0]):
                first_tweet_idx = j
                success = True
                break
        if (success):
            print ("First [sarcastic] retrieved for user %s" %(i))
            f1.write(full_tweets[first_tweet_idx]._json['text'] + tweet_delimiter)
            full_tweets.remove(full_tweets[first_tweet_idx])
            for tweet in full_tweets:
                f1.write(tweet._json['text'] + tweet_delimiter)
            f1.write(user_delimiter)
        else:
            print ("First tweet not available for user %s. Discarding tweets ..." %(i)) 
        i += 1
    except Exception as e:
        print ("Tweets could not be retrieved for user %s" %(i))
        print (e)
        i += 1

