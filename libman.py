from sqlite3 import DatabaseError
from tkinter import *
from tkinter import ttk

from pandas import DataFrame
class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")


        lbltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=15,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        #BOOK DETAILS FRAME
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=90,width=1280,height=370)

        DataFrameLeft=LabelFrame(frame,text="Library Membership information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=650,height=330)
        DataFrameRight=LabelFrame(frame,text="Book details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=670,y=5,width=540,height=330)
        
        lblmember=Label(DataFrameLeft,text="Member type",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=21,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblprn=Label(DataFrameLeft,text="PRN No.",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblprn.grid(row=1,column=0,sticky=W)

        txtprn=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtprn.grid(row=1,column=1,sticky=W)

        lblID=Label(DataFrameLeft,text="SAPID No.",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblID.grid(row=2,column=0,sticky=W)

        txtID=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtID.grid(row=2,column=1,sticky=W)

        lblFn=Label(DataFrameLeft,text="First Name",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFn.grid(row=3,column=0,sticky=W)

        txtFn=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtFn.grid(row=3,column=1,sticky=W)

        lblLn=Label(DataFrameLeft,text="Last Name",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLn.grid(row=4,column=0,sticky=W)

        txtLn=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtLn.grid(row=4,column=1,sticky=W)

        lbladdr1=Label(DataFrameLeft,text="Address Line1",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladdr1.grid(row=5,column=0,sticky=W)

        txtaddr1=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtaddr1.grid(row=5,column=1,sticky=W)

        lbladdr2=Label(DataFrameLeft,text="Address Line2",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladdr2.grid(row=6,column=0,sticky=W)

        txtaddr2=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtaddr2.grid(row=6,column=1,sticky=W)

        lblmob=Label(DataFrameLeft,text="Mobile",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmob.grid(row=7,column=0,sticky=W)

        txtmob=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtmob.grid(row=7,column=1,sticky=W)

        lbl_bookid=Label(DataFrameLeft,text="Book ID:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_bookid.grid(row=0,column=2,sticky=W)

        txtbookid=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtbookid.grid(row=0,column=3,sticky=W)

        lbl_booktitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_booktitle.grid(row=1,column=2,sticky=W)

        txtbooktitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtbooktitle.grid(row=1,column=3,sticky=W)

        lbl_author=Label(DataFrameLeft,text="Author Name:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_author.grid(row=2,column=2,sticky=W)

        txtauthor=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtauthor.grid(row=2,column=3,sticky=W)

        lbl_dateb=Label(DataFrameLeft,text="Data Borrowed:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_dateb.grid(row=3,column=2,sticky=W)

        txtdateb=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtdateb.grid(row=3,column=3,sticky=W)

        lbl_dd=Label(DataFrameLeft,text="Date Due:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_dd.grid(row=4,column=2,sticky=W)

        txtdd=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtdd.grid(row=4,column=3,sticky=W)

        lbl_late=Label(DataFrameLeft,text="Late Return Fine:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_late.grid(row=5,column=2,sticky=W)

        txtlate=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtlate.grid(row=5,column=3,sticky=W)

        lbl_overdue=Label(DataFrameLeft,text="Date Overdue:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_overdue.grid(row=6,column=2,sticky=W)

        txtoverdue=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtoverdue.grid(row=6,column=3,sticky=W)

        lbl_price=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_price.grid(row=7,column=2,sticky=W)

        txtprice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=23)
        txtprice.grid(row=7,column=3,sticky=W)

        #DATAFRAME RIGHT
        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=29,height=14,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScroll=Scrollbar(DataFrameRight)
        listScroll.grid(row=0,column=1,sticky="ns")

        listBook=['Head first book','Learn Python the hard way','Automata Theory','Design and Analysis of Algorithms','Web Programming','Universal Human Values','Probability and Statistics','Computer Network','Advanced Data Structures','Data Mining','Engineering design','Graphic design','Database Management System','Operating Systems','Discrete Mathematics','Environmental Studies']
        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=14)
        listBox.grid(row=0,column=0,padx=4)

        listScroll.config(command=listBox.yview)
        for item in listBook:
            listBox.insert(END,item)


        #BUTTON FRAME
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=460,width=1280,height=70)

         #DATABASE FRAME
        framedata=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framedata.place(x=0,y=530,width=1280,height=155)


if __name__ == "__main__":
    root= Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()