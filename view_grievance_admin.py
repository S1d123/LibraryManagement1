import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import showerror

import pymysql

root = Tk()
root.geometry()
root.geometry('1350x710+0+10')
root.title('Library Management System')

bg = PhotoImage(file='bgpic1.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)
sid1 = StringVar()
f1 = Frame(root, height=500, width=650, bg='white', borderwidth=8, relief=SOLID)
f1.place(x=360, y=100)

Label1 = Label(f1, text='RAISED GRIEVANCES ', font=('goudy old style', 22, 'bold'), fg='black',
                            bg='gray98')
Label1.place(x=24, y=28)

my_tree = ttk.Treeview(f1)
my_tree['columns'] = ("Std_ID", "Std_Name", "Date","Comments")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Std_ID", anchor=W, width=70)
my_tree.column("Std_Name", anchor=CENTER, width=140)
my_tree.column("Date", anchor=W, width=100)
my_tree.column("Comments", anchor=W, width=250)
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Std_ID", text="Student_ID", anchor=W)
my_tree.heading("Std_Name", text="Student_Name", anchor=W)
my_tree.heading("Date", text="Date", anchor=W)
my_tree.heading("Comments", text="Comments", anchor=W)
style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",background="silver",fieldbackground="silver",foreground="black"
                    )
style.map('Treeview',background=[('selected','orange')])
my_tree.place(x=30, y=75)
con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
cur = con.cursor()
cur.execute("select * from grievance_user")
g = cur.fetchall()
if len(g) != 0:
    for row in g:
        my_tree.insert('', END, values=row)
con.commit()
con.close()

def back():
    root.destroy()
    import adminlogin3

b1 = Button(f1, text='Back', font='eras_medium_itc 14  bold', bg='orange', fg='black', width=10, bd=3,
            borderwidth=2, relief=SOLID, command=back).place(x=250, y=410)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()