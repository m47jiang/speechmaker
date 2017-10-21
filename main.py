#!/usr/bin/python3.6
import pyaudio
import wave
import sys
import tkinter as tk

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

top = tk.Tk()
top.geometry("700x280")

#frame1 = tk.Frame(top, width=600, height=300)
#frame1.pack_propagate(False)
#frame1.place(x=0,y=0)
#code to add widgets will go here...

speechText = tk.Text(top, height=20)
speechText.insert('1.0', 'hello world')
#speechText.rowconfigure(0, weight=1)
#speechText.columnconfigure(0, weight=2)
speechText.grid(row=0, column=0, sticky='nsew', rowspan=10)

startButton = tk.Button(top, text ="Start Speech", bd = 5, command = startCallBack, anchor='s')
#startButton.grid_rowconfigure(0, weight=1)
#startButton.grid_columnconfigure(0, weight=1)
startButton.grid(row=0, column=1, sticky='s')

analyseButton = tk.Button(top, text ="Analyse Text", bd = 5, anchor='n')
#analyseButton.grid_rowconfigure(0, weight=1)
#analyseButton.grid_columnconfigure(0, weight=1)
analyseButton.grid(row=1, column=1, sticky='n')





top.mainloop()



