from tkinter import *
root=Tk()
canvas=Canvas(root,height=100,width=200)
canvas.pack()
newline=canvas.create_line(0,0,10,90,fill="green")#(xtox,ytoy)
root.mainloop()