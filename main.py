#!/usr/bin/python3.6

import tkinter as tk
top = tk.Tk()
top.geometry("600x300")
frame1 = tk.Frame(top, width=600, height=300)
frame1.pack_propagate(False)
frame1.place(x=0,y=0)
#code to add widgets will go here...

start = tk.Button(frame1, text ="hello", bd = 5)
start.pack()
#frame1.geometry("300x300")
top.mainloop()

