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
def admin():
    window.withdraw()
    global win,b1,b2,b3,b4,cur,con
    win=Tk()
    win.title('Admin')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    win.mainloop()


def closedb():
    global con,cur
    cur.close()
    con.close()        

def connectdb():
    global con,cur
    #Enter your username and password of MySQL
    con=p.connect(host="localhost",user="root",passwd="at123thapa")
    cur=con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS Library')
    cur.execute('USE Library')
    global enter
    if enter==1:
        l='CREATE TABLE IF NOT EXISTS Login(name varchar(20),userid varchar(10),branch varchar(20),mobile int(10))'
        b='CREATE TABLE IF NOT EXISTS Book(subject varchar(20),title varchar(20),author varchar(20),serial int(5))'
        i='CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(20),serial varchar(10),issue date,exp date)'
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter=enter+1
    query='SELECT * FROM Login'
    cur.execute(query)

