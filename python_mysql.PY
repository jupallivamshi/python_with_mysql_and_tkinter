import sys
import mysql.connector
from tkinter import*
from tkinter import messagebox

am=mysql.connector.connect( host='localhost',user='root',password='root')
def table_creat():
    try:
        ms=am.cursor()
        ms.execute('create schema emp_database')
        ms.execute('create table emp_database.emp_data(eid int primary key, ename varchar(30) not null,salary float,phno bigint)')
        messagebox.showinfo("DataBase","database created sucess")

    except:
        messagebox.showwarning("table","database already exist")
def exit():
    sys.exit()

def create_data():
    eid=e1.get()
    ename=e2.get()
    salary=e3.get()
    phno=e4.get()
    if eid =='' or ename=='' or salary =='' or phno =='':
        messagebox.showwarning("empty error","all feilds required")
    ms=am.cursor()
    ms.execute('SELECT * FROM emp_database.emp_data where eid= ' + eid + ' ')
    mydata = ms.fetchall()
    value=None
    for data in mydata: 
        value=str(data[0])  
                 
    if eid == value:
            messagebox.showerror("Alert", "duplicate id ")
    else:    
        ms=am.cursor()
        query='insert into emp_database.emp_data values(%s,%s,%s,%s)'
        values=[eid,ename,salary,phno]        
        ms.execute(query,values)
        am.commit()
        messagebox.showinfo("Insert","your record inserted sucess")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
def retrive():
    eid=e1.get()
    if eid=='':
        messagebox.showwarning("empty error","id field are required")
    else:
        ms=am.cursor()
        ms.execute('SELECT * FROM emp_database.emp_data where eid= ' + eid + '')
        mydata = ms.fetchall()
        for data in mydata:
            dataa=data
            e2.insert(1,dataa[1])
            e3.insert(1,dataa[2])
            e4.insert(1,dataa[3])
            messagebox.showinfo("retrived","retrived sucess")

def update():
    eid=e1.get()
    ename=e2.get()
    salary=e3.get()
    phno=e4.get()
    ms=am.cursor()
    query="update emp_database.emp_data set=%s where=%s "
    values=[ename,eid]
    ms.execute(query,values)
    messagebox.showinfo("update","updated sucess")


                                    
def delete():
    eid=e1.get()
    ms=am.cursor()
    ms.execute('delete from emp_database.emp_data where eid='+eid+'')
    am.commit()
    messagebox.showinfo("Delete","Record deleted sucess")
    


def dele():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
                                 #>>>>>>>>>>>>>>>>>>>>>>> Creation of UI<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
vam=Tk()
vam.geometry("500x500")
vam.title("Vamshi Project")
Label(vam,text="eid").grid(row=0,column=0)
Label(vam,text="ename").grid(row=1,column=0)
Label(vam,text="salary").grid(row=2,column=0)
Label(vam,text="phone number").grid(row=3,column=0)
e1 = Entry(vam)
e1.grid(row=0,column=1)
e2=Entry(vam)
e2.grid(row=1,column=1)
e3=Entry(vam)
e3.grid(row=2,column=1)
e4=Entry(vam)
e4.grid(row=3,column=1)
b1=Button(vam,text="create",command=create_data, bg="#08ff08",activebackground="#228B22").place(x=50,y=150)
b2=Button(vam,text="retrive",bg="#87cefa",command=retrive).place(x=110,y=150)
b3=Button(vam,text="update",command=update, bg="#a5ceec").place(x=170,y=150)
b4=Button(vam,text="Delete",command=delete, bg="#ace5ee").place(x=230,y=150)
b5=Button(vam,text="Create database" ,bg="#ace5ee",command=table_creat).grid(row=5,column=4)
b6=Button(vam,text="Clear",command=dele).grid(row=5,column=2)
Button(vam,text="Exit",padx=20,pady=10,command=exit,bg="red").place(x=110,y=250)
vam.mainloop()

   

