from tkinter import *

def deletebook():
    global win
    # win.destroy()
    win=Tk()
    win.title('Delete Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    usid=Label(win,text='Serial NO')
    paswrd=Label(win,text='PASSWORD')
    global e1
    e1=Entry(win)
    global e2,b2
    e2=Entry(win)
    b1=Button(win, height=2,width=17,text=' DELETE ')
    b2=Button(win, height=2,width=17,text=' CLOSE ')
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    win.mainloop()
deletebook()