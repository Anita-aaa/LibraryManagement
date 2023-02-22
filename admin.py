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