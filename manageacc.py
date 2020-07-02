# https://ttkwidgets.readthedocs.io/en/latest/examples/Calendar.html
from tkinter import *
from tkinter import ttk
import sqlite3
from placeholder import *
from exp import *
from tkcalendar import DateEntry
from datetime import date
import re
# def raise_frame(frame):
#     frame.tkraise()
def unpack(frame,win):
    frame.destroy()
    win.pack()
def createtable1(total_rows,total_columns,lst,curs): 
          
    rt=Tk()
        
    
    for i in range(total_rows+1): 
        for j in range(total_columns): 
            if (i==0):
                e = Entry(rt, width=20, fg='red', font=('Arial',16,'bold')) 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
            else:
                e = Entry(rt, width=20, fg='blue', 
                           font=('Arial',16,'bold')) 
                 
                e.grid(row=i, column=j) 
                e.insert(END, lst[i][j])                    
    curs.execute('''select sum(debit),sum(credit) from( select sum(debit.amount) as debit,sum(credit.amount)as credit from debit   join credit using(name) group by name)''')
    lst1=curs.fetchall()
    totdeb="Total debit is "+str(lst1[0][0])
    totcre="Total credit is "+str(lst1[0][1])
    acdeb="Total Actual Debit is "+str(lst1[0][0]-lst1[0][1])
    ltd=Label(rt,text=totdeb,font=('Arial',16,'bold')).grid(row=total_rows+2, column=0,columnspan=total_columns)
    ltd=Label(rt,text=totcre,font=('Arial',16,'bold')).grid(row=total_rows+3, column=0,columnspan=total_columns)           
    ltd=Label(rt,text=acdeb,font=('Arial',16,'bold')).grid(row=total_rows+4, column=0,columnspan=total_columns)           
    rt.mainloop()
def createtable2(curs, e1): 
          
    rt=Tk()
    curs.execute('select * from debit where name=(?)',(e1.get(),))
    # curs.execute('select * from debit')
    lst=curs.fetchall()
    print(lst)
    total_rows=len(lst)
    total_columns=5
    l1=lst.insert(0,("ID","Name","debit amount", "Comments","Date"))
    for i in range(total_rows+1): 
        for j in range(total_columns): 
            if (i==0):
                e = Entry(rt, width=20, fg='red', font=('Arial',16,'bold')) 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
            else:
                e = Entry(rt, width=20, fg='blue', 
                           font=('Arial',16,'bold')) 
                 
                e.grid(row=i, column=j) 
                e.insert(END, str(lst[i][j]))                    
    curs.execute('select sum(amount) from debit where name=(?)',(e1.get(),))
    lst1=curs.fetchall()
    totdeb="Total debit is "+str(lst1[0][0])
    ltd=Label(rt,text=totdeb,font=('Arial',16,'bold')).grid(row=total_rows+2, column=0,columnspan=total_columns)
    rt.mainloop()
def createtable3(curs, e1): 
          
    rt=Tk()
    curs.execute('select debit.name,amount,comments,date,type from debit join accounts using(name) where type=(?)',(e1.get(),))
    # curs.execute('select * from debit')
    lst=curs.fetchall()
    print(lst)
    total_rows=len(lst)
    total_columns=5
    l1=lst.insert(0,("Name","debit amount", "Comments","Date","Type"))
    for i in range(total_rows+1): 
        for j in range(total_columns): 
            if (i==0):
                e = Entry(rt, width=20, fg='red', font=('Arial',16,'bold')) 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
            else:
                e = Entry(rt, width=20, fg='blue', 
                           font=('Arial',16,'bold')) 
                 
                e.grid(row=i, column=j) 
                e.insert(END, str(lst[i][j]))                    
    curs.execute('select sum(amount) from accounts join debit using(name) where type=(?)',(e1.get(),))
    lst1=curs.fetchall()
    totdeb="Total debit is "+str(lst1[0][0])
    ltd=Label(rt,text=totdeb,font=('Arial',16,'bold')).grid(row=total_rows+2, column=0,columnspan=total_columns)
    rt.mainloop()
def createtable4(curs, e1): 
          
    rt1=Tk()
    curs.execute('select * from credit where name=(?)',(e1.get(),))
    # curs.execute('select * from debit')
    lst=curs.fetchall()
    print(lst)
    total_rows=len(lst)
    total_columns=5
    l1=lst.insert(0,("ID","Name","credit amount", "Comments","Date"))
    for i in range(total_rows+1): 
        for j in range(total_columns): 
            if (i==0):
                e = Entry(rt1, width=20, fg='red', font=('Arial',16,'bold')) 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
            else:
                e = Entry(rt1, width=20, fg='blue', 
                           font=('Arial',16,'bold')) 
                 
                e.grid(row=i, column=j) 
                e.insert(END, str(lst[i][j]))                    
    curs.execute('select sum(amount) from credit where name=(?)',(e1.get(),))
    lst1=curs.fetchall()
    totdeb="Total credit is "+str(lst1[0][0])
    ltd=Label(rt1,text=totdeb,font=('Arial',16,'bold')).grid(row=total_rows+2, column=0,columnspan=total_columns)
    rt1.mainloop()
def createtable5(curs, e1): 
          
    rt1=Tk()
    curs.execute('select credit.name,amount,comments,date,type from credit join accounts using(name) where type=(?)',(e1.get(),))
    # curs.execute('select * from debit')
    lst=curs.fetchall()
    print(lst)
    total_rows=len(lst)
    total_columns=5
    l1=lst.insert(0,("Name","debit amount", "Comments","Date","Type"))
    for i in range(total_rows+1): 
        for j in range(total_columns): 
            if (i==0):
                e = Entry(rt1, width=20, fg='red', font=('Arial',16,'bold')) 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
            else:
                e = Entry(rt1, width=20, fg='blue', 
                           font=('Arial',16,'bold')) 
                 
                e.grid(row=i, column=j) 
                e.insert(END, str(lst[i][j]))                    
    curs.execute('select sum(amount) from accounts join credit using(name) where type=(?)',(e1.get(),))
    lst1=curs.fetchall()
    totdeb="Total credit is "+str(lst1[0][0])
    ltd=Label(rt1,text=totdeb,font=('Arial',16,'bold')).grid(row=total_rows+2, column=0,columnspan=total_columns)
    rt1.mainloop()
def inserttoacc(frame,e1,e2,e3,e4,lb1):
    if(e1.get()==""):
        # lb2.destroy()
        lb1.config(text="Enter Name" ,fg="red")
    elif(e4.get()==""):
        # lb1.destroy()
        lb1.config(text="Enter Type of Account", fg="red")
    else:
        # lb.pack()s
        conn = sqlite3.connect('manageaccountsdb')
        curs = conn.cursor()
        q1=curs.execute('Select count(*) from accounts where name=(?)',((e1.get()).lower(),))
        a=q1.fetchall()
        if(int(a[0][0])==0):
            curs.execute('insert into accounts values(?,?,?,?)',(e1.get().lower(),e2.get(), (e3.get()), e4.get()))
            curs.execute('insert into debit(name, amount, Date) values(?,?,?)',(e1.get(),0,date.today()))
            curs.execute('insert into credit(name, amount, Date) values(?,?,?)',(e1.get(),0,date.today()))
            conn .commit()
            lb2.config(text="Account added Successfully" ,fg="green")
            unpack(frame,win)
        else:
            lb1.config(text="Name Already Exists, Enter new Name", fg="red")
        
        # lb.destroy()
def deleteacc(frame1, entry,ld1):
    # ld2=Label(win)
    # ld2.pack(side=BOTTOM)
    if(entry.get()==""):
        # lb2.destroy()
        ld1.config(text="Enter Name" ,fg="red")
    else:
        conn = sqlite3.connect('manageaccountsdb')
        curs = conn.cursor()
        q1=curs.execute('Select count(*) from accounts where name=(?)',((entry.get()).lower(),))
        a=q1.fetchall()
        if(int(a[0][0])==1):
            curs.execute('delete from accounts where name=(?)',((entry.get()).lower(),))
            lb2.config(text="Account deleted Successfully" ,fg="green")
            unpack(frame1,win)
        else:
            ld1.config(text="Account does not Exists", fg="red")
            ld1.pack(padx=10, pady=10,expand=YES)

        conn.commit()
def debitttoacc(frame2,e1,e2,e3,e4,lb1):
    # lb2=Label(win)
    # lb2.pack(side=BOTTOM)
    if(e1.get()==""):
        # lb2.destroy()
        lb1.config(text="Enter Name" ,fg="red")
    elif(e2.get()==""):
        # if not re.match("[0-9]*", str(e2.get())):
        lb1.config(text="Enter correct amount", fg="red")
    elif(e3.get()==""):
        # lb1.destroy()
        lb1.config(text="Enter Comment", fg="red")
    else:
        lb1.config(text="")
        conn = sqlite3.connect('manageaccountsdb')
        curs = conn.cursor()
        q1=curs.execute('Select count(*) from accounts where name=(?)',((e1.get()).lower(),))
        a=q1.fetchall()
        if(int(a[0][0])==1):
            curs.execute('insert into debit(name, amount, Comments, Date) values(?,?,?,?)',(e1.get(),e2.get(), (e3.get()), e4.get()))
            s="debit to "+e1.get()+" account is Successful"
            lb2.config(text=s ,fg="green")
            unpack(frame2,win)
        else:
            lb1.config(text="Account does not Exists", fg="red")
            lb1.pack(padx=10, pady=10,expand=YES)

        conn.commit()
def creditttoacc(frame2,e1,e2,e3,e4,lb1):
    
    # lb2.pack(side=BOTTOM)
    if(e1.get()==""):
        # lb2.destroy()
        lb1.config(text="Enter Name" ,fg="red")
    elif(e2.get()==""):
        # if not re.match("[0-9]*", str(e2.get())):
        lb1.config(text="Enter correct amount", fg="red")
    elif(e3.get()==""):
        # lb1.destroy()
        lb1.config(text="Enter Comment", fg="red")
    else:
        lb1.config(text="")
        conn = sqlite3.connect('manageaccountsdb')
        curs = conn.cursor()
        q1=curs.execute('Select count(*) from accounts where name=(?)',((e1.get()).lower(),))
        a=q1.fetchall()
        if(int(a[0][0])==1):
            curs.execute('insert into credit(name, amount, Comments, Date) values(?,?,?,?)',(e1.get(),e2.get(), (e3.get()), e4.get()))
            s="Credit from "+e1.get()+" account is Successful"
            lb2.config(text=s ,fg="green")
            unpack(frame2,win)
        else:
            lb1.config(text="Account does not Exists", fg="red")
            lb1.pack(padx=10, pady=10,expand=YES)

        conn.commit()
# def show dxebname(dframe)
def showdebitaccs(frame4):
    frame4.pack_forget()
    dframe=Frame(root)
    dframe.pack()
    Button(dframe, text='Go back', command=lambda: unpack(dframe,frame4), bg='black', fg='white').pack(padx=10, pady=5,expand=YES)
    conn = sqlite3.connect('manageaccountsdb')
    curs = conn.cursor()
    curs.execute("select name from accounts")
    name=[rec[0] for rec in curs.fetchall()]
    name.insert(0,"Enter Name to be searched")
    print(name)
    e1 = AutocompleteCombobox(dframe)
    e1.set_completion_list(name)
    e1.pack()
    e1.focus_set()
    e1.current(0)
    
    
    Button(dframe, text='debit report by name', command=lambda: createtable2(curs,e1)).pack(padx=10, pady=5,expand=YES)
    curs.execute("select distinct(type) from accounts")
    names=[rec[0] for rec in curs.fetchall()]
    names.insert(0,"Enter type")
    e2 = AutocompleteCombobox(dframe)
    e2.set_completion_list(names)
    e2.pack()
    e2.focus_set()
    e2.current(0)
    print(names)
    Button(dframe, text='debit report by account type', command=lambda: createtable3(curs,e2)).pack(padx=10, pady=5,expand=YES)
    # Button(dframe, text='debit  report by Between Dates', command=lambda: unpack(dframe,frame4)).pack(padx=10, pady=5,expand=YES)
def showcreditaccs(frame4):
    frame4.pack_forget()
    cframe=Frame(root)
    cframe.pack()
    Button(cframe, text='Go back', command=lambda: unpack(cframe,frame4), bg='black', fg='white').pack(padx=10, pady=5,expand=YES)
    conn = sqlite3.connect('manageaccountsdb')
    curs = conn.cursor()
    curs.execute("select name from accounts")
    name=[rec[0] for rec in curs.fetchall()]
    name.insert(0,"Enter Name to be searched")
    print(name)
    e1 = AutocompleteCombobox(cframe)
    e1.set_completion_list(name)
    e1.pack()
    e1.focus_set()
    e1.current(0)
    
    
    Button(cframe, text='credit report by name', command=lambda: createtable4(curs,e1)).pack(padx=10, pady=5,expand=YES)
    curs.execute("select distinct(type) from accounts")
    names=[rec[0] for rec in curs.fetchall()]
    names.insert(0,"Enter type")
    e2 = AutocompleteCombobox(cframe)
    e2.set_completion_list(names)
    e2.pack()
    e2.focus_set()
    e2.current(0)
    print(names)
    Button(cframe, text='debit report by account type', command=lambda: createtable4(curs,e2)).pack(padx=10, pady=5,expand=YES)
    
        
def debit():
    win.pack_forget()
    frame2=Frame(root)
    frame2.pack()
    Button(frame2, text='Go back', command=lambda: unpack(frame2,win), bg='black', fg='white').pack(padx=10, pady=5,expand=YES)
    l1=Label(frame2, text="Enter Name: ").pack()
    conn = sqlite3.connect('manageaccountsdb')
    curs = conn.cursor()
    curs.execute('select name from accounts')
    names = [rec[0] for rec in curs.fetchall()]
    entry = AutocompleteCombobox(frame2)
    entry.set_completion_list(names)
    entry.pack()
    entry.focus_set()
    conn.commit()
    l2=Label(frame2, text="Enter Amount to be Debited: ").pack()
    e2=EntryWithPlaceholder(frame2, "")
    e2.pack(padx=10, pady=5,expand=YES)
    l3=Label(frame2, text="Comments: ").pack()
    e3=EntryWithPlaceholder(frame2, "")
    e3.pack(padx=10, pady=5,expand=YES)
    lb3=Label(frame2, text="Enter Date")
    lb3.pack(padx=10,expand=YES)
    cal = DateEntry(frame2, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='dd/mm/yy')
    cal.pack()
    ldeb=Label(frame2)
    ldeb.pack()
    Button(frame2, text='Submit', command=lambda: debitttoacc(frame2,entry,e2,e3,cal,ldeb)).pack(padx=10, pady=10,expand=YES)
    
def credit():
    win.pack_forget()
    frame3=Frame(root)
    frame3.pack()
    Button(frame3, text='Go back', command=lambda: unpack(frame3,win), bg='black', fg='white').pack(padx=10, pady=5,expand=YES)
    l1=Label(frame3, text="Enter Name: ").pack()
    conn = sqlite3.connect('manageaccountsdb')
    curs = conn.cursor()
    curs.execute('select name from accounts')
    names = [rec[0] for rec in curs.fetchall()]
    entry = AutocompleteCombobox(frame3)
    entry.set_completion_list(names)
    entry.pack()
    entry.focus_set()
    conn.commit()
    l2=Label(frame3, text="Enter Amount: to be Creditted ").pack()
    e2=EntryWithPlaceholder(frame3, "")
    e2.pack(padx=10, pady=5,expand=YES)
    l3=Label(frame3, text="Comments: ").pack()
    e3=EntryWithPlaceholder(frame3, "")
    e3.pack(padx=10, pady=5,expand=YES)
    lb3=Label(frame3, text="Enter Date")
    lb3.pack(padx=10,expand=YES)
    cal = DateEntry(frame3, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='dd/mm/yy')
    cal.pack()
    ldeb=Label(frame3)
    ldeb.pack()
    Button(frame3, text='Submit', command=lambda: creditttoacc(frame3,entry,e2,e3,cal,ldeb)).pack(padx=10, pady=10,expand=YES)
def showacc():
    win.pack_forget()
    frame4=Frame(root)
    frame4.pack()
    Button(frame4, text='Go back', command=lambda: unpack(frame4,win), bg='black', fg='white').pack(padx=10, pady=5,expand=YES)
    # Label(frame4, text='show all accounts').pack()
    conn = sqlite3.connect('manageaccountsdb')
    curs = conn.cursor()
    curs.execute('''select debit.name,sum(debit.amount),sum(credit.amount),sum(debit.amount)-sum(credit.amount) from debit   join credit using(name) group by debit.name''')
    # curs.execute('select * from debit')
    lst=curs.fetchall()
    tr=len(lst)
    tc=4
    l1=lst.insert(0,("Name","debit amount", "credit amount","Actual Debit"))
    # print(lst)    
    bs1=Button(frame4, text="Show debit and credit Accounts", command=lambda: createtable1(tr,tc,lst,curs)).pack(padx=10, pady=5,expand=YES)
    
    bs2=Button(frame4, text="Show debit", command=lambda: showdebitaccs(frame4)).pack(padx=10, pady=5,expand=YES)
    bs2=Button(frame4, text="Show credit", command=lambda: showcreditaccs(frame4)).pack(padx=10, pady=5,expand=YES)
    conn.commit()
def addacc():
    
    
    # droot.title("Add New Account")
    # raise_frame(frame)
    win.pack_forget()
    frame=Frame(root)
    frame.pack()
    Button(frame, text='Go back', command=lambda: unpack(frame,win), bg='black', fg='white').pack(padx=10, pady=5,expand=YES)
    l1=Label(frame, text="Enter Name: ").pack()
    e1=EntryWithPlaceholder(frame, "")
    e1.pack(padx=10, pady=5,expand=YES)
    
    l2=Label(frame, text="Enter Address: ").pack()
    e2=EntryWithPlaceholder(frame, "")
    e2.pack(padx=10, pady=5,expand=YES)
    l3=Label(frame, text="Enter Phone Number: ").pack()
    e3=EntryWithPlaceholder(frame, "")
    e3.pack(padx=10, pady=5,expand=YES)
    lb3=Label(frame, text="Enter Type Of Account")
    lb3.pack(padx=10,expand=YES)
    e4 = AutocompleteCombobox(frame)
    e4.set_completion_list(('Staff', 'Personal', 'Investment'))
    e4.pack(expand=YES)

    # e4.focus_set()
    lb1=Label(frame)
    lb1.pack()
    Button(frame, text='Submit', command=lambda: inserttoacc(frame,e1,e2,e3,e4,lb1)).pack(padx=10, pady=10,expand=YES)
    # frame.bind('<Return>', inserttoacc(frame,e1,e2,e3,e4))
    # e2=Entry(frame, text="Address").pack(padx=10, pady=10)e1=EntryWithPlaceholder(frame, "Type Name Here").pack()e1=EntryWithPlaceholder(frame, "Type Name Here").pack()
    # , font=("Courier", 20))
    # droot.mainloop()
def detacc():
    win.pack_forget()
    frame1=Frame(root)
    frame1.pack()
    Button(frame1, text='Go back', command=lambda: unpack(frame1,win), bg='black', fg='white').pack(padx=10, pady=5,expand=YES)
    
    Label(frame1, text='Enter Account Name to be Deleted').pack(padx=10, pady=5,expand=YES)
    # Entry(frame1).pack(padx=10, pady=5,expand=YES)
    conn = sqlite3.connect('manageaccountsdb')
    curs = conn.cursor()
    curs.execute('select name from accounts')
    names = [rec[0] for rec in curs.fetchall()]
    # print(names)
    entry = AutocompleteCombobox(frame1)
    entry.set_completion_list(names)
    entry.pack()
    entry.focus_set()
    conn.commit()
    ld1=Label(frame1)
    Button(frame1, text='Delete', command=lambda: deleteacc(frame1,entry,ld1)).pack(padx=10, pady=10,expand=YES)
    Button(frame1, text='Delete', command=lambda: deletedeb(frame1,entry,ld1)).pack(padx=10, pady=10,expand=YES)
    
    
root=Tk()
global rt
global rt1
root.title("Manage Accounts")
root.geometry("400x400")
frame=Frame(root)
# frame.pack()
win = Frame(root)
win.pack()
# win.grid(row=0, column=0, sticky='news')

# Label(win, text='Hello GUI world!').pack(side=TOP)
btd=Button(win ,text="DEBIT", command=debit)
btd.pack(padx=5,pady=5)
btc=Button(win ,text="CREDIT", command=credit).pack( padx=5,pady=5)
bts=Button(win ,text="SHOW ACCOUNTS", command=showacc).pack(padx=5,pady=5)
btaddacc=Button(win ,text="ADD ACCOUNT", command=addacc).pack(padx=5,pady=5)

btdelacc=Button(win ,text="DELETE ACCOUNT", command=detacc).pack(padx=5,pady=5)
global lb2
lb2=Label(win)
lb2.pack()
root.mainloop()
