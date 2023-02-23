from tkinter import *
from tkinter.ttk import Combobox
import datetime

month=['January','February','March','April','May','June','July','August','September','October','November','December']
y = list(range(2020, 2040))
d = list(range(1,32))

def issuebook():
    global win
    win=Tk()
    win.title('Issue Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    name=Label(win,text='ISSUE ',font='Helvetica 30 bold')
    branch=Label(win,text='BOOK',font='Helvetica 30 bold')

    sid=Label(win,text='STUDENT ID')
    no=Label(win,text='BOOK NO')
    issue=Label(win,text='ISSUE DATE')
    exp=Label(win,text='EXPIRY DATE')
    global e1,b,b1
    e1=Entry(win,width=25)
    global e4
    e4=Entry(win,width=25)
    global com1y,com1m,com1d,com2y,com2m,com2d
    com1y=Combobox(win,value=y,width=5)
    com1m=Combobox(win,value=month,width=5)
    com1d=Combobox(win,value=d,width=5)
    com2y=Combobox(win,value=y,width=5)
    com2m=Combobox(win,value=month,width=5)
    com2d=Combobox(win,value=d,width=5)
    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    
    com2y.set(now.year)
    com2m.set(month[now.month-1])
    com2d.set(now.day)
    
    b=Button(win, height=2,width=21,text=' ISSUE BOOK ')
    b1=Button(win, height=2,width=21,text=' CLOSE ')
    name.place(x=55,y=30)
    branch.place(x=225,y=30)
    sid.place(x=70,y=130)
    no.place(x=70,y=170)
    issue.place(x=70,y=210)
    exp.place(x=70,y=240)
    e1.place(x=180,y=130)
    e4.place(x=180,y=170)
    com1y.place(x=180,y=210)
    com1m.place(x=230,y=210)
    com1d.place(x=280,y=210)
    com2y.place(x=180,y=240)
    com2m.place(x=230,y=240)
    com2d.place(x=280,y=240)
    b.place(x=178,y=270)
    b1.place(x=178,y=312)
    win.mainloop()
issuebook()