#!/usr/bin/python
import string
import tweepy

#global data

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="BxEa0a7otNC7IvIQG65ir8Yqm"
consumer_secret="XOfwYzc7mD3RABGRuHWeD2z2rXqTtJt6FY474dKXcJj5nv8vDm"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="1337652349-nTJAw5CQWK7l1SJkD1XlOBcAqQbPeNRRi6JDyZ0"
access_token_secret="NDPVz04sjw0Vgn2xy9n7AnKRgkndJnEwSCVBDCmQfZHPq"

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

arr_of_emotions = [angerSet, anticipationSet, disgustSet, fearSet, joySet, 
					sadnessSet, surpriseSet, trustSet]
arr_of_sents = [negativeSet, positiveSet]

############################################################################
#Methods

def get_five_tweets(screen_name):
  tweettexts = []	
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.secure = True
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)

  # If the authentication was successful, you should
  # see the name of the account print out
  alltweets = api.user_timeline(screen_name = screen_name,count=5)
  i=0
  for p in alltweets: 
    tweettexts.append(p.text)

  return tweettexts

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
def buildSets():
	emotionsFile = open("emotions.txt", "r")
	linesInFile = emotionsFile.readlines()
	numLines = len(linesInFile)
	for i in range(numLines):
		toParse = linesInFile[i].split()
		classifyIntoSet(toParse[0], toParse[1], toParse[2])
	emotionsFile.close()

def getCounts(tweettexts):
	#array of counts
	counts = [0] * 8
	#array of sentiments
	sent_counts = [0] * 2

	for i in range(len(tweettexts)):
		toProcess = (tweettexts[i].split())
		for j in range(len(toProcess)):
			temp = toProcess[j].encode('ascii', 'ignore').lower().strip(string.punctuation)
			#print temp
			if temp != "":
				if temp[0] == "#":
					#print "here"
					temp = temp[1:]
				if temp[0] != "@":
					#print temp
					if temp in angerSet:
						counts[0] += 1
					if temp in anticipationSet:
						counts[1] += 1
					if temp in disgustSet:
						counts[2] += 1
					if temp in fearSet:
						counts[3] += 1
					if temp in joySet:
						counts[4] += 1
					if temp in sadnessSet:
						counts[5] += 1
					if temp in surpriseSet:
						counts[6] += 1
					if temp in trustSet:
						counts[7] += 1
					if temp in positiveSet:
						sent_counts[0] += 1
					if temp in negativeSet:
						sent_counts[1] += 1

		return (counts, sent_counts)

def getMaxCount(counts):
	e_max = max(counts)
	return e_max

##########################################################################################
# #script code

# buildSets()
# #print list(angerSet)

# tweets = get_five_tweets("itsmeaditi_")
# #print(tweettexts)

# getCounts(tweets)
# #print list(counts)
# #print list(sent_counts)


