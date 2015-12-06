#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import parsing_emotions
import music

level = 1
song_set = []

def readTwitterHandle():
  return twittahHandle.get()

def dataInitializer():
  parsing_emotions.buildSets()

def displayData(song_set):
  Lb1.delete(0)
  Lb1.insert(0, song_set[0])
  Lb1.delete(1)
  Lb1.insert(1, song_set[1])
  Lb1.delete(2)
  Lb1.insert(2, song_set[2])
  Lb1.delete(3)
  Lb1.insert(3, song_set[3])
  Lb1.delete(4)
  Lb1.insert(4, song_set[4])
  Lb1.pack(fill="both", expand=True, padx=20, pady=20)
  
def analyze():
  s = readTwitterHandle()
  tweets = parsing_emotions.get_five_tweets(s)
  (e_counts, s_counts) = parsing_emotions.getCounts(tweets)
  e_max = parsing_emotions.getMaxCount(e_counts)
  global level 
  level = 1
  global song_set 
  song_set = music.createPlaylist(e_max, 1)
  displayData(song_set)

def dislike():
  s = readTwitterHandle()
  global level
  level += 1
  tweets = parsing_emotions.get_five_tweets(s)
  (e_counts, s_counts) = parsing_emotions.getCounts(tweets)
  e_max = parsing_emotions.getMaxCount(e_counts)
  global song_set
  song_set = music.createPlaylist(e_max, level)
  displayData(song_set)

def like():
  s = readTwitterHandle()
  global level
  global song_set
  tweets = parsing_emotions.get_five_tweets(s)
  (e_counts, s_counts) = parsing_emotions.getCounts(tweets)
  e_max = parsing_emotions.getMaxCount(e_counts)
  if level > 1:
    level -= 1
  new_song_set = music.createSimilarPlaylist(e_max, song_set, level)
  song_set = new_song_set
  displayData(song_set)

##############################GUI CODE##########################################

top = Tk()
top.wm_title("TweetTunes")
top.minsize(width=400, height=200)
top.maxsize(width=400, height=200)

tFrame = Frame(top, height=50, width = 400)
tFrame.pack(side = TOP)

bFrame = Frame(top, height =150, width = 400)
bFrame.pack(side = BOTTOM)

introFrame = Frame(tFrame, height = 50, width = 100)
introFrame.pack(side=LEFT)

L1 = Label(introFrame, text="Twittah Handle:")
L1.pack()

handleFrame = Frame(introFrame, height = 25, width = 100)
handleFrame.pack(side=BOTTOM)

twittahHandle = Entry(handleFrame, bd = 1)
twittahHandle.pack(side = LEFT)
bHandle = Button(handleFrame, text="Analyze!", command = analyze)
bHandle.pack(side = RIGHT)

buttonFrame = Frame(tFrame, height=50, width=100)
buttonFrame.pack(side = RIGHT)

nameFrame = Frame(buttonFrame, height = 25, width = 100)
nameFrame.pack(side = TOP)

nameLabel = Label(nameFrame, text="By Aditi and Lucas")
nameLabel.pack(side = TOP)

bWrapperFrame = Frame(buttonFrame, height = 25, width = 100)
bWrapperFrame.pack(side = BOTTOM)

# Code to add widgets will go here...
b1 = Button(bWrapperFrame, text="Like", fg="green", bg="green", command = like)
b2 = Button(bWrapperFrame, text="Dislike", fg="red", bg="red", command = dislike)
b1.pack(side = LEFT)
b2.pack(side = RIGHT)

Lb1 = Listbox(bFrame, height = 5)
Lb1.insert(0, "Song1")
Lb1.insert(1, "Song2")
Lb1.insert(2, "Song3")
Lb1.insert(3, "Song4")
Lb1.insert(4, "Song5")
Lb1.pack(fill="both", expand=True, padx=20, pady=20)
Lb1.config(width=200)

top.mainloop()


