#!/usr/bin/python
import string
from pyechonest import config
from pyechonest import artist
from PyLyrics import *


import sys
import urllib
import json
from pyechonest import playlist

import parsing_emotions.py

#import pyechonest
config.ECHO_NEST_API_KEY="KDNXOX04ZZQ1OMLLW"

#method for getting similar artists
def getSimilarArtist(name):
	similarArtists = []
	mm = artist.Artist('%s' % name)
	#print "Artists similar to: %s:" % (mm.name,)
	for similar_artist in mm.similar: 
		similarArtists.append(similar_artist.name)
		#print "\t%s" % (similar_artist.name,)
	return similarArtists

# artists = getSimilarArtist("taylor swift")
# print artists

#method for getting lyrics to a song
def getLyrics(artist, song):
	return (PyLyrics.getLyrics(artist,song))

#print(getLyrics('Taylor Swift', 'Wildest Dreams'))

