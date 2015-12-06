#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import music

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
bHandle = Button(handleFrame, text="Analyze!")
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
b1 = Button(bWrapperFrame, text="Like", fg="green", bg="green")
b2 = Button(bWrapperFrame, text="Dislike", fg="red", bg="red")
b1.pack(side = LEFT)
b2.pack(side = RIGHT)

Lb1 = Listbox(bFrame, height = 5)
Lb1.insert(1, "Song1")
Lb1.insert(2, "Song2")
Lb1.insert(3, "Song3")
Lb1.insert(4, "Song4")
Lb1.insert(5, "Song5")
Lb1.pack(fill="both", expand=True, padx=20, pady=20)

top.mainloop()
#two buttons
