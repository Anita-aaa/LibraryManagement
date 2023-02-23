from tkinter import *


b1,b2,b3,b4,cur,con,e1,e2,e3,e4,e5,i,ps=None,None,None,None,None,None,None,None,None,None,None,None,None
window,win=None,None

def addbook():
    global win
    win=Tk()
    win.title('Add Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    sub=Label(win,text='SUBJECT')
    tit=Label(win,text='TITLE')
    auth=Label(win,text='AUTHOR')
    ser=Label(win,text='SERIAL NO')
    global e1,b,b1
    e1=Entry(win,width=25)
    global e2
    e2=Entry(win,width=25)
    global e3
    e3=Entry(win,width=25)
    global e4
    e4=Entry(win,width=25)
    b=Button(win, height=2,width=21,text=' ADD BOOK TO DB ')
    b1=Button(win, height=2,width=21,text=' CLOSE ')
    sub.place(x=70,y=50)
    tit.place(x=70,y=90)
    auth.place(x=70,y=130)
    ser.place(x=70,y=170)
    e1.place(x=180,y=50)
    e2.place(x=180,y=90)
    e3.place(x=180,y=130)
    e4.place(x=180,y=170)
    b.place(x=180,y=210)
    b1.place(x=180,y=252)
    win.mainloop()
addbook()