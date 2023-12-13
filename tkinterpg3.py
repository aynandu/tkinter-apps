#Self adjuesting widget
from tkinter import *
root=Tk()
lbl1=Label(root,text="Hai",bg="red",fg="blue")
lbl1.pack(fill=X)
lbl2=Label(root,text="Hai",bg="yellow",fg="green")
lbl2.pack(side=RIGHT,fill=Y)
root.mainloop()