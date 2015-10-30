#!/usr/bin/python

import tweepy

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="BxEa0a7otNC7IvIQG65ir8Yqm"
consumer_secret="XOfwYzc7mD3RABGRuHWeD2z2rXqTtJt6FY474dKXcJj5nv8vDm"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="1337652349-nTJAw5CQWK7l1SJkD1XlOBcAqQbPeNRRi6JDyZ0"
access_token_secret="NDPVz04sjw0Vgn2xy9n7AnKRgkndJnEwSCVBDCmQfZHPq"

tweetexts = ()

def get_five_tweets(screen_name):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.secure = True
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)

  # If the authentication was successful, you should
  # see the name of the account print out
  alltweets = api.user_timeline(screen_name = screen_name,count=5)
  i=0
  for p in alltweets: 
    tweettexts = tweettexts + (p.text,)

emotionsFile = open("emotions.txt", "r")

#Emotions
angerSet = set()
anticipationSet = set()
disgustSet = set()
fearSet = set()
joySet = set()
sadnessSet = set()
surpriseSet = set()
trustSet = set()

#Overall Sentiments
negativeSet = set()
positiveSet = set()

linesInFile = emotionsFile.readlines()

numLines = len(linesInFile)

def classifyIntoSet(word, senti, flag):
	if senti == "anger":
		if int(flag) == 1:
			angerSet.add(word)

	if senti == "anticipation":
		if int(flag) == 1:
			anticipationSet.add(word)

	if senti == "disgust":
		if int(flag) == 1:
			disgustSet.add(word)

	if senti == "fear":
		if int(flag) == 1:
			fearSet.add(word)

	if senti == "joy":
		if int(flag) == 1:
			joySet.add(word)

	if senti == "sadness":
		if int(flag) == 1:
			sadnessSet.add(word)

	if senti == "surprise":
		if int(flag) == 1:
			surpriseSet.add(word)

	if senti == "trust":
		if int(flag) == 1:
			trustSet.add(word)

	if senti == "positive":
		if int(flag) == 1:
			positiveSet.add(word)

	if senti == "negative":
		if int(flag) == 1:
			negativeSet.add(word)
	return;

#Iterate through each line in the file and add the words to the sets

for i in range(numLines):
	toParse = linesInFile[i].split()
	classifyIntoSet(toParse[0], toParse[1], toParse[2])

emotionsFile.close()

#print list(angerSet)
#print list(anticipationSet)
#print list(disgustSet)
#print list(fearSet)
#print list(joySet)
#print list(sadnessSet)
#print list(surpriseSet)
#print list(trustSet)
#print list(positiveSet)
#print list(negativeSet)
