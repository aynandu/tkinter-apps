from tkinter import *
root=Tk()
myMenu=Menu(root)
root.config(menu=myMenu)

def fun1():
        print("New Project")
def fun2():
        print("New")
def fun3():
        print("New Scrach File")

def fun4():
    print("Open")

def fun5():
    print("Undo")

def fun6():
     print("Redo")
def fun7():
    print("Cut")

def fun8():
    print("Copy")

def fun9():
    print("Paste")

def fun10():
    print("Tool Window")

def fun11():
    print("Definition")

def fun12():
    print("Quick Type")

def fun13():
    print("Compare with")

def fun14():
    print("Active Editor")

def fun15():
 print("Back")

def fun16():
     print("Search Every Where")

def fun17():
     print("Class")

def fun18():
    print("File")

def fun19():
    print("Symbol")

subMenu=Menu(myMenu)
myMenu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command=fun1)
subMenu.add_command(label="New",command=fun2)
subMenu.add_command(label="New Scrach File",command=fun3)
subMenu.add_separator()
subMenu.add_command(label="Open..",command=fun4)
subMenu.add_command(label="Exit",command=quit)

subMenu2=Menu(myMenu)
myMenu.add_cascade(label="Edit",menu=subMenu2)
subMenu2.add_command(label="Undo",command=fun5)
subMenu2.add_command(label="Redo",command=fun6)
subMenu2.add_separator()
subMenu2.add_command(label="Cut",command=fun7)
subMenu2.add_command(label="Copy",command=fun8)
subMenu2.add_command(label="Paste",command=fun9)

subMenu3=Menu(myMenu)
myMenu.add_cascade(label="Tools",menu=subMenu3)
subMenu3.add_command(label="Tool Window",command=fun10)
subMenu3.add_command(label="Definition",command=fun11)
subMenu3.add_separator()
subMenu3.add_command(label="Quik type",command=fun12)
subMenu3.add_command(label="Compare with",command=fun13)
subMenu3.add_command(label="Active Editor",command=fun14)

subMenu4=Menu(myMenu)
myMenu.add_cascade(label="Navigation",menu=subMenu4)
subMenu4.add_command(label="Back",command=fun15)
subMenu4.add_command(label="Search EveryWhere",command=fun16)
subMenu4.add_separator()
subMenu4.add_command(label="Class",command=fun17)
subMenu4.add_command(label="File",command=fun18)
subMenu4.add_command(label="Symbol",command=fun19)

toolBar=Frame(root,bg="pink")
inbutton=Button(toolBar,text="Crop")
inbutton.pack(side=LEFT,padx=2,pady=2)
toolBar.pack(side=TOP,fill=X)

status=Label(root,text="This is Pycharm 2023.23.1",relief=SUNKEN,bd=1,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()