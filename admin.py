from tkinter import *
import pymysql as p

def loginlibr():
    global window
    connectdb()
    for i in range(cur.rowcount):
        data=cur.fetchone()
        if e1.get().strip()==str(data[1]) and e2.get().strip()==str(data[3]):
            closedb()
            libr()
            break
    else:
        window.withdraw()
        closedb()
        home()
def libr():
    global window
    window.withdraw()
    global win,b1,b2,b3,b4
    win=Tk()
    win.title('Library')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    win.mainloop()

def loginadmin():
    if e1.get()=='admin' and e2.get()=='admin':
        admin();
        