#Button Click
from tkinter import *
def fun():
    print("Click Here")
root=Tk()
btn=Button(root,text="Ok",command=fun).pack()
root.mainloop()

