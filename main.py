#!/usr/bin/python3.6
import pyaudio
import wave
import sys
import tkinter as tk

top = tk.Tk()
top.geometry("600x300")
frame1 = tk.Frame(top, width=600, height=300)
frame1.pack_propagate(False)
frame1.place(x=0,y=0)
#code to add widgets will go here...

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

start = tk.Button(frame1, text ="hello", bd = 5, command = startCallBack)


start.pack()

speechText = tk.Text(frame1, width=600, height=300)
speechText.insert('1.0', 'hello world')
speechText.pack()
#frame1.geometry("300x300")
top.mainloop()



