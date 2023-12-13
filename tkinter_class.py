from tkinter import *
class  myfun:
    def __init__(self,root):
        frame=Frame(root)
        frame.pack()
        self.lbl=Label(frame,text="Click - Cancel - Quit").pack()
        self.btn=Button(frame,text="Click",command=self.clk)
        self.btn.pack()
        self.btn2 = Button(frame, text="Cancel", command=self.can)
        self.btn2.pack(side=LEFT)
        self.btn3 = Button(frame, text="Quit", command=quit)
        self.btn3.pack(side=RIGHT)
    def clk(self):
        print("Clicked")
    def can(self):
            print("Cancelled")
root=Tk()
ini=myfun(root)
root.mainloop()