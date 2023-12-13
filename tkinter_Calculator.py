import parser
from tkinter import *


root=Tk()
root.title("Calculator")
display=Entry()
display.grid(rows=1,columnspan=6,sticky=W+E)
#get number in to input box
i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1

def clearAll():
    display.delete(0,END)

def undoAll():
    entireString=display.get()
    if len(entireString):
        newstring=entireString[:-1]
        clearAll()
        display.insert(0,newstring)
    else:
        clearAll()
        display.insert(0, "Error")

def getOperator(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entireString=display.get()
    try:
        evaluateResult=parser.expr(entireString).compile()
        result=eval(evaluateResult)
        clearAll()
        display.insert(0,result)
    except Exception:
        clearAll()
        display.insert(0, "Error")

#Adding Button
Button(root,text="1",command=lambda :get_variable(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda :get_variable(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda :get_variable(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda :get_variable(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :get_variable(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :get_variable(6)).grid(row=3,column=2)
Button(root,text="7",command=lambda :get_variable(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda :get_variable(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda :get_variable(9)).grid(row=4,column=2)
Button(root,text="0",command=lambda :get_variable(0)).grid(row=5,column=0)
Button(root,text="AC",command=lambda :clearAll()).grid(row=5,column=1)
Button(root,text="=",command=lambda :calculate()).grid(row=5,column=2)
Button(root,text="+",command=lambda :getOperator("+")).grid(row=2,column=3)
Button(root,text="-",command=lambda :getOperator("-")).grid(row=3,column=3)
Button(root,text="*",command=lambda :getOperator("*")).grid(row=4,column=3)
Button(root,text="/",command=lambda :getOperator("/")).grid(row=5,column=3)
Button(root,text="pi",command=lambda :getOperator("*3.14")).grid(row=2,column=4)
Button(root,text="%",command=lambda :getOperator("%")).grid(row=3,column=4)
Button(root,text="( ",command=lambda :getOperator("(")).grid(row=4,column=4)
Button(root,text=") ",command=lambda :getOperator(")")).grid(row=5,column=4)
Button(root,text="exp",command=lambda :getOperator("**")).grid(row=2,column=5)
Button(root,text="->",command=lambda :undoAll()).grid(row=3,column=5)
Button(root,text="^2",command=lambda :getOperator("**2")).grid(row=4,column=5)
root.mainloop()