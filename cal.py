from tkinter import *

expression = ""

def clear():
    global expression
    expression = ""
    displayValue.set(expression)

def equal():
    global expression
    expression = str(eval(expression))
    displayValue.set(expression)

def btnClick(num):
    global expression
    expression += str(num)
    displayValue.set(expression)




win = Tk()
win.title("cws Calculator")
win.geometry("300x400")
win.configure(background="light green")


displayValue = StringVar()

displayValue.set("lets Calculate")



display = Entry(win,width=24,justify=RIGHT,textvariable=displayValue)

display.grid(row=0,columnspan=4,pady=20,padx=10)



btn1 = Button(win,width=7,height=2,fg="black",bg="white",text="1",command=lambda:btnClick(1))
btn1.grid(row=1,column=0)

btn2 = Button(win,width=7,height=2,fg="black",bg="white",text="2",command=lambda:btnClick(2))
btn2.grid(row=1,column=1)

btn3 = Button(win,width=7,height=2,fg="black",bg="white",text="3",command=lambda:btnClick(3))
btn3.grid(row=1,column=2)

btn4 = Button(win,width=7,height=2,fg="black",bg="white",text="+",command=lambda:btnClick('+'))
btn4.grid(row=1,column=3)

####################### 2nd ROW ############################

btn5 = Button(win,width=7,height=2,fg="black",bg="white",text="4",command=lambda:btnClick(4))
btn5.grid(row=2,column=0)

btn6 = Button(win,width=7,height=2,fg="black",bg="white",text="5",command=lambda:btnClick(5))
btn6.grid(row=2,column=1)

btn7 = Button(win,width=7,height=2,fg="black",bg="white",text="6",command=lambda:btnClick(6))
btn7.grid(row=2,column=2)

btn8 = Button(win,width=7,height=2,fg="black",bg="white",text="/",command=lambda:btnClick('/'))
btn8.grid(row=2,column=3)

#################### 3rd ROW ###################

btn9 = Button(win,width=7,height=2,fg="black",bg="white",text="7",command=lambda:btnClick(7))
btn9.grid(row=3,column=0)

btn10 = Button(win,width=7,height=2,fg="black",bg="white",text="8",command=lambda:btnClick(8))
btn10.grid(row=3,column=1)

btn11 = Button(win,width=7,height=2,fg="black",bg="white",text="9",command=lambda:btnClick(9))
btn11.grid(row=3,column=2)

btn12 = Button(win,width=7,height=2,fg="black",bg="white",text="*",command=lambda:btnClick('*'))
btn12.grid(row=3,column=3)

#################### 4rd ROW ###################

btn13 = Button(win,width=7,height=2,fg="black",bg="white",text="0",command=lambda:btnClick(0))
btn13.grid(row=4,column=0)

btn14 = Button(win,width=7,height=2,fg="black",bg="white",text="=",command=equal)
btn14.grid(row=4,column=1)

btn15 = Button(win,width=7,height=2,fg="white",bg="red",text="C",command=clear)
btn15.grid(row=4,column=2)

btn16 = Button(win,width=7,height=2,fg="black",bg="white",text="-",command=lambda:btnClick('-'))
btn16.grid(row=4,column=3)



win.mainloop()