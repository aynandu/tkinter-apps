#System Application Toolkit
from tkinter import *
Root_Window=Tk() #Open
#Frame
frame1=Frame(Root_Window)
frame1.pack()
#Label
label_Name=Label(frame1,text="Hello Nandu").pack() #.pack :- AutoSave
#Button
btn=Button(frame1,text="OK",fg="red",bg="blue")
btn.pack()
Root_Window.mainloop() # Close