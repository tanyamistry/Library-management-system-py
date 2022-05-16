from sqlite3 import DatabaseError
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime

from pandas import DataFrame
class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")

        #VARIABLE
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

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

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=21,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblprn=Label(DataFrameLeft,text="PRN No.",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblprn.grid(row=1,column=0,sticky=W)

        txtprn=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",12,"bold"),width=23)
        txtprn.grid(row=1,column=1,sticky=W)

        lblID=Label(DataFrameLeft,text="SAPID No.",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblID.grid(row=2,column=0,sticky=W)

        txtID=Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman",12,"bold"),width=23)
        txtID.grid(row=2,column=1,sticky=W)

        lblFn=Label(DataFrameLeft,text="First Name",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFn.grid(row=3,column=0,sticky=W)

        txtFn=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",12,"bold"),width=23)
        txtFn.grid(row=3,column=1,sticky=W)

        lblLn=Label(DataFrameLeft,text="Last Name",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLn.grid(row=4,column=0,sticky=W)

        txtLn=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("times new roman",12,"bold"),width=23)
        txtLn.grid(row=4,column=1,sticky=W)

        lbladdr1=Label(DataFrameLeft,text="Address Line1",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladdr1.grid(row=5,column=0,sticky=W)

        txtaddr1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("times new roman",12,"bold"),width=23)
        txtaddr1.grid(row=5,column=1,sticky=W)

        lbladdr2=Label(DataFrameLeft,text="Address Line2",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladdr2.grid(row=6,column=0,sticky=W)

        txtaddr2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("times new roman",12,"bold"),width=23)
        txtaddr2.grid(row=6,column=1,sticky=W)

        lblmob=Label(DataFrameLeft,text="Mobile",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmob.grid(row=7,column=0,sticky=W)

        txtmob=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",12,"bold"),width=23)
        txtmob.grid(row=7,column=1,sticky=W)

        lbl_bookid=Label(DataFrameLeft,text="Book ID:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_bookid.grid(row=0,column=2,sticky=W)

        txtbookid=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",12,"bold"),width=23)
        txtbookid.grid(row=0,column=3,sticky=W)

        lbl_booktitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_booktitle.grid(row=1,column=2,sticky=W)

        txtbooktitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman",12,"bold"),width=23)
        txtbooktitle.grid(row=1,column=3,sticky=W)

        lbl_author=Label(DataFrameLeft,text="Author Name:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_author.grid(row=2,column=2,sticky=W)

        txtauthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("times new roman",12,"bold"),width=23)
        txtauthor.grid(row=2,column=3,sticky=W)

        lbl_dateb=Label(DataFrameLeft,text="Date Borrowed:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_dateb.grid(row=3,column=2,sticky=W)

        txtdateb=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("times new roman",12,"bold"),width=23)
        txtdateb.grid(row=3,column=3,sticky=W)

        lbl_dd=Label(DataFrameLeft,text="Date Due:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_dd.grid(row=4,column=2,sticky=W)

        txtdd=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("times new roman",12,"bold"),width=23)
        txtdd.grid(row=4,column=3,sticky=W)

        lbl_late=Label(DataFrameLeft,text="Late Return Fine:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_late.grid(row=5,column=2,sticky=W)

        txtlate=Entry(DataFrameLeft,textvariable=self.lateratefine_var,font=("times new roman",12,"bold"),width=23)
        txtlate.grid(row=5,column=3,sticky=W)

        lbl_overdue=Label(DataFrameLeft,text="Date Overdue:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_overdue.grid(row=6,column=2,sticky=W)

        txtoverdue=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("times new roman",12,"bold"),width=23)
        txtoverdue.grid(row=6,column=3,sticky=W)

        lbl_price=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_price.grid(row=7,column=2,sticky=W)

        txtprice=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("times new roman",12,"bold"),width=23)
        txtprice.grid(row=7,column=3,sticky=W)

        #DATAFRAME RIGHT
        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=29,height=14,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScroll=Scrollbar(DataFrameRight)
        listScroll.grid(row=0,column=1,sticky="ns")

        listBook=['Head-First Python, 2nd edition','Learn Python the hard way','Automata Theory','Design and Analysis of Algorithms','Web Programming','Probability and Statistics','Computer Network','Advanced Data Structures','Discrete Mathematics']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head-First Python, 2nd edition"):
                self.bookid_var.set("BKID1230")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")

            elif (x=="Learn Python the hard way"):
                self.bookid_var.set("BKID56789")
                self.booktitle_var.set("Learn Python 3 the Hard Way")
                self.author_var.set("Zed Shaw")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=20)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 60")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1000")

            elif (x=="Automata Theory"):
                self.bookid_var.set("BKID58799")
                self.booktitle_var.set("Automata Theory and Applications")
                self.author_var.set("Peter Linz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1708")

            elif (x=="Design and Analysis of Algorithms"):
                self.bookid_var.set("BKID7895")
                self.booktitle_var.set("Design and Analysis of Algorithms")
                self.author_var.set("Micheal Cooper")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.800")

            elif (x=="Web Programming"):
                self.bookid_var.set("BKID1111")
                self.booktitle_var.set("Web Design With HTML")
                self.author_var.set("John Dean")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 70")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.2100")

            elif (x=="Probability and Statistics"):
                self.bookid_var.set("BKID58799")
                self.booktitle_var.set("Probability and Statistics")
                self.author_var.set("Rahul Bose")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=5)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 20")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif (x=="Computer Network"):
                self.bookid_var.set("BKID58799")
                self.booktitle_var.set("Fundamentals of Computer Networks")
                self.author_var.set("A. Anthony")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=80)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 200")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.3580")

            elif (x=="Advanced Data Structures"):
                self.bookid_var.set("BKID58799")
                self.booktitle_var.set("Advanced Data Structures and their Applications")
                self.author_var.set("Thomas Stop")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 10")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.902")

            elif (x=="Discrete Mathematics"):
                self.bookid_var.set("BKID58799")
                self.booktitle_var.set("Discrete Mathematics")
                self.author_var.set("Alisha Banz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.lateratefine_var.set("Rs. 15")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.355")

        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=14)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)

        listScroll.config(command=listBox.yview)
        for item in listBook:
            listBox.insert(END,item)


        #BUTTON FRAME
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=460,width=1280,height=70)

        btnAddData=Button(framebutton,command=self.add_data,text="Add Data",font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,text="Show Data",font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,text="Update",font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,text="Delete",font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(framebutton,text="Reset",font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,text="Exit",font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

         #DATABASE FRAME
        framedata=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framedata.place(x=0,y=530,width=1280,height=155)

        table_frame=Frame(framedata,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=2,width=1200,height=125)

        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(table_frame,columns=("membertype","prnno","title","firstname","lastname","address1",
                                                            "address2","mobile","bookid","booktitile","author","borrowdate",
                                                            "datedue","laterreturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN no.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Addesss 2")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitile",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("borrowdate",text="Date Borrowed")
        self.library_table.heading("datedue",text="Due date")
        self.library_table.heading("laterreturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=85)
        self.library_table.column("prnno",width=80)
        self.library_table.column("title",width=80)
        self.library_table.column("firstname",width=80)
        self.library_table.column("lastname",width=80)
        self.library_table.column("address1",width=80)
        self.library_table.column("address2",width=80)
        self.library_table.column("mobile",width=80)
        self.library_table.column("bookid",width=80)
        self.library_table.column("booktitile",width=85)
        self.library_table.column("author",width=80)
        self.library_table.column("borrowdate",width=85)
        self.library_table.column("datedue",width=80)
        self.library_table.column("laterreturnfine",width=95)
        self.library_table.column("dateoverdue",width=85)
        self.library_table.column("finalprice",width=85)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sheth@1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.member_var.get(),
                                                                                                        self.prn_var.get(),
                                                                                                        self.id_var.get(),
                                                                                                        self.firstname_var.get(),
                                                                                                        self.lastname_var.get(),
                                                                                                        self.address1_var.get(),
                                                                                                        self.address2_var.get(),
                                                                                                        self.mobile_var.get(),
                                                                                                        self.bookid_var.get(),
                                                                                                        self.booktitle_var.get(),
                                                                                                        self.author_var.get(),
                                                                                                        self.dateborrowed_var.get(),
                                                                                                        self.datedue_var.get(),
                                                                                                        self.lateratefine_var.get(),
                                                                                                        self.dateoverdue_var.get(),
                                                                                                        self.finalprice_var.get()
                                                                                                        ))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success","Member has been added successfully.")

if __name__ == "__main__":
    root= Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()