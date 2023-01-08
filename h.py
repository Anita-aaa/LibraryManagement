#data of library management system
from tkinter import*
root=Tk()

root.title("LIBRRY MANAGEMENT SYSTEM")
root.config(bg="yellow")
root.maxsize(width=800,height=620)
root.minsize(width=800,height=620)

def add():
    x=var.get()
    print(x)
    label1.config(text=x,bg="yellow")

'''btn=Button(root,text="LIBRARY MANAGEMENT SYSTEM",fg="black",bg="yellow",command=add)
btn.place(x=200,y=10)'''

#label
label=Label(root,text="LIBRARY MANAFEMENT SYSTEM",fg="black",bg="yellow")
label.place(x=280,y=10)
label1=Label(root,text="ENTER STUDENT",bg="yellow",fg="black")
label1.place(x=100,y=100)
label1=Entry(root,text="",width=50)
label2=Label(root,text="ENTER THE BOOK ID",bg="yellow",fg="black")
label2.place(x=80,y=150)
label2=Entry(root,text="",width=50)
label3=Label(root,text="INFORMATION DETAILS",bg="yellow",fg="black")
label3.place(x=300,y=270)


#entry
var=StringVar()
ent=Entry(root,bg="white",fg="black",textvariable=var,width=45)
ent.place(x=220,y=100)

var=StringVar()
ent=Entry(root,bg="white",fg="black",textvariable=var,width=45)
ent.place(x=220,y=150)

#btn1
btn=Button(root,text="Search",fg="black",bg="white",command=add,width=10)
btn.place(x=530,y=100)
btn=Button(root,text="Find",fg="black",bg="white",command=add,width=10)
btn.place(x=530,y=150)
btn=Button(root,text="LOGOUT",fg="black",bg="red",width=15,command=add)
btn.place(x=640,y=100)

#btn2
btn=Button(root,text="Search Student",fg="black",bg="white",width=15)
btn.place(x=90,y=220)
btn=Button(root,text="Search Book",fg="black",bg="white",width=15)
btn.place(x=240,y=220)
btn=Button(root,text="Issue Book",fg="black",bg="white",width=15)
btn.place(x=390,y=220)
btn=Button(root,text="Return Book",fg="black",bg="white",width=15)
btn.place(x=540,y=220)

#btn3
btn=Button(root,text="",fg="black",bg="white",width=85,height=20,command=add)
btn.place(x=90,y=305)

#btn4
btn=Button(root,text="ID",fg="black",bg="pink",width=8)
btn.place(x=90,y=305)
btn=Button(root,text="Student",fg="black",bg="pink",width=18)
btn.place(x=155,y=305)
btn=Button(root,text="Book",fg="black",bg="pink",width=18)
btn.place(x=290,y=305)
btn=Button(root,text="Issue Date",fg="black",bg="pink",width=18)
btn.place(x=425,y=305)
btn=Button(root,text="Return Date",fg="black",bg="pink",width=18)
btn.place(x=560,y=305)

root.mainloop()
