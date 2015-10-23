#!/usr/bin/python

#Open emotions.txt file and build up the sets
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

for i in range(numLines):
	toParse = linesInFile[i].split()
	classifyIntoSet(toParse[0], toParse[1], toParse[2])

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

emotionsFile.close()