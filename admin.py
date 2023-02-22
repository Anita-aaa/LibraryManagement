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
def home():
    try:
        global window,b1,b2,e1,e2,con,cur,win
        window=Tk()
        window.title('Welcome')
        window.resizable(False,False)
        window.geometry("400x400+480+180")
        #wel=Label(window,text='LIBRARY',font='Helvetica 28 bold')
        #lib=Label(window,text='MANAGEMENT',font='Helvetica 28 bold')
        usid=Label(window,text='USER ID')
        paswrd=Label(window,text='PASSWORD')
        e1=Entry(window,width=22)
        e2=Entry(window,width=22)
        b1=Button(window,text=' LOGIN AS LIBRARIAN' ,height=2,width=20,command=loginlibr)
        b2=Button(window,text=' LOGIN AS ADMIN ', height=2,width=20,command=loginadmin)
        #wel.place(x=160,y=20)
        #lib.place(x=110,y=70)2222
        usid.place(x=70,y=100)
        paswrd.place(x=70,y=140)
        e1.place(x=180,y=100)
        e2.place(x=180,y=140)
        b1.place(x=175,y=180)
        b2.place(x=175,y=225)
        window.mainloop()
    except Exception:
        window.destroy()
enter=1
home()

