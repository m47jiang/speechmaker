#!/usr/bin/python3.6
import pyaudio
import wave
import sys
import tkinter as tk
import time
from line import * 
interval = 100
def highlightSentence(currentLine):
	speechText.tag_add("highlighted", "2.0","2." + str(currentLine.numChars + 1))
	speechText.tag_config("highlighted", background="white", foreground="blue")
def startCallBack():
	speech = Speech(getAllText(speechText))
	addCounterToTextbox(speechText)
	line = speech.getnextline()
	updateCounter(speechText, line.timeExpected)
	speechText.after(interval, karaokeLoopCallback, speech, line)
	highlightSentence(line)
	# hightlight current sentence

def karaokeLoopCallback(speech, line):
	if not line:
		return
	if line.timeExpected <= 0:
		print(line.numChars)
		lines = getAllText(speechText)#.strip('. ')
		lines = lines[0:6] + lines[counterLen() + 1 + line.numChars:]
		print(lines)
		speechText.delete("1.0", tk.END)
		speechText.insert('1.0', lines)
		
		line = speech.getnextline()
		if not line:
			return
		
		updateCounter(speechText, line.timeExpected)
		highlightSentence(line)
		#speech.delete("2.0", str((20+line.numchar())/10
		# delete current sentence, highlight next sentence
	else:
		
		print(line.timeExpected)
		line.timeExpected -= interval 
		updateCounter(speechText, line.timeExpected)
	speechText.after(interval, karaokeLoopCallback, speech, line)

def counterLen():
	return 6
def addCounterToTextbox(textbox):
	textbox.insert('1.0', '00000\n')

def updateCounter(textbox, val):
	valstr = str(val).zfill(5)
	textbox.delete('1.0','1.5')
	textbox.insert('1.0', valstr)

def getAllText(textbox):
	return textbox.get("1.0",'end-1c')



def colorCallback():
	speechText.delete("1.0", "1.4")
	speechText.tag_config("word2",font = "Helvetica 44 bold", background="white", foreground="blue")

def colourText():
	speechText.tag_add("word1", "1.0", "1.4")
	speechText.tag_add("word2", "1.4", "1.11")
	
	speechText.tag_config("word1", background="white", foreground="blue")
	
	speechText.after(interval, colorCallback)

def analyzeText():
	try:
		text = getSelectedText(speechText)
	except:
		text = getAllText(speechText)
	print(text)
	colourText()

top = tk.Tk()
top.geometry("1920x1080")

#frame1 = tk.Frame(top, width=600, height=300)
#frame1.pack_propagate(False)
#frame1.place(x=0,y=0)
#code to add widgets will go here...

speechText = tk.Text(top, font = "Helvetica 44 bold", width = 40, height=10)
speechText.insert('1.0', 'hello world')

#speechText.rowconfigure(0, weight=1)
#speechText.columnconfigure(0, weight=2)
speechText.grid(row=0, column=0, sticky='nsew', rowspan=10)

startButton = tk.Button(top, text ="Start Speech", bd = 5, command = startCallBack, anchor='s')
#startButton.grid_rowconfigure(0, weight=1)
#startButton.grid_columnconfigure(0, weight=1)
startButton.grid(row=0, column=1, sticky='s')

analyseButton = tk.Button(top, text ="Analyse Text", bd = 5, command=analyzeText, anchor='n')
#analyseButton.grid_rowconfigure(0, weight=1)
#analyseButton.grid_columnconfigure(0, weight=1)
analyseButton.grid(row=1, column=1, sticky='n')


top.mainloop()



