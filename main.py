#!/usr/bin/python3.6
import pyaudio
import wave
import sys
import tkinter as tk
import time

def startCallBack():
	CHUNK = 1024

	#if len(sys.argv) < 2:
	#    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
	#    sys.exit(-1)

	wf = wave.open('bensoundshort.wav', 'rb')

	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		        channels=wf.getnchannels(),
		        rate=wf.getframerate(),
		        output=True)

	data = wf.readframes(CHUNK)

	while data != '':
	    stream.write(data)
	    data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()

def getSelectedText(textbox):
	return textbox.get(tk.SEL_FIRST, tk.SEL_LAST)

def getAllText(textbox):
	return textbox.get("1.0",'end-1c')
def colorCallback():
	speechText.tag_config("word2", background="black", foreground="green")
def colourText():
	speechText.tag_add("word1", "1.0", "1.4")
	speechText.tag_add("word2", "1.4", "1.11")
	speechText.tag_config("word1", background="black", foreground="green")
	
	speechText.after(1000, colorCallback)

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



