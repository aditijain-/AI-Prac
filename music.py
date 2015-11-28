#!/usr/bin/python
import string
from pyechonest import config
from pyechonest import artist
from PyLyrics import *

import random
import sys
import urllib
import json
from pyechonest import playlist

import parsing_emotions

seedset = ["Taylor Swift","AC/DC","One Direction","Beyonce","Drake",
      "Blake Shelton","The Blues Brothers","Guns N' Roses","AVICII",
      "Simon and Garfunkel"]

#import pyechonest
config.ECHO_NEST_API_KEY="KDNXOX04ZZQ1OMLLW"

def getSeedArtist():
  seed = random.randint(0,len(seedset)-1)
  return artist.Artist(seedset[seed])

#method for getting similar artists
def getSimilarArtist(singer):
  sim = random.randint(0,len(singer.similar)-1)
  return singer.similar[sim]

def getSong(singer):
  songs = singer.get_songs()
  rand = random.randint(0, len(songs)-1)
  return songs[rand]

# print getSong(artist.Artist("taylor swift"))

#method for getting lyrics to a song
def getLyrics(artist, song):
	return (PyLyrics.getLyrics(artist,song))

# a = artist.Artist("taylor swift")
# result = getSong(a)
# print result
#print(getLyrics(a.name, result.title))

def getMood(lyrics, mood_index, level):
  assert level <= 5 and level >= 1

  it = iter(lyrics.splitlines())
  lines = []
  for i in range(level):
    lines.append(it.next())
  
  (e_counts, s_counts) = parsing_emotions.getCounts(lines)

  #find max count in e_counts -> this represents the predominant emotion
  e_max = max(e_counts)
  if e_max == mood_index:
    return True

  return False

def getSongForMood(mood, seed, level):
  artist = seed
  while True:
    song = getSong(artist)
    lyrics = getLyrics(artist.name, song.title)
    result = getMood(lyrics, mood, level)
    if result == True:
      return (song.title, artist.name)
    else:
      artist = getSimilarArtist(artist)

  return False

def createPlaylists(mood, seed, level):
  i = 1
  song_set = []
  while i > 0:
    song = getSongForMood(mood, seed, level)
    song_set.append(song)
    i -= 1

  return song_set


if __name__ == "__main__":
  parsing_emotions.buildSets()
  #print list(angerSet)

  tweets = parsing_emotions.get_five_tweets("itsmeaditi_")
  #print(tweettexts)

  (e_counts, s_counts) = parsing_emotions.getCounts(tweets)

  e_max = parsing_emotions.getMaxCount(e_counts)

  seed_artist = getSeedArtist()

  song_set = createPlaylists(e_max, seed_artist, 1)
  print song_set

  #print list(counts)
  #print list(sent_counts)


# getMood(getLyrics(a.name,result.title), "happy", 4)




