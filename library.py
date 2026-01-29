from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter import Tk, Frame, Listbox, Scrollbar,Button
import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1530x800+0+0") #window size width 1150 to height 800 and starting 0 and ending point 0

#========================================= Variables=============================================================================================================================

        self.member_var =  StringVar()
        self.prn_var =  StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.adress2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finallprice = StringVar()




        #Frame create and lebeling

        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg = "sky blue",fg ="Darkgreen",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=0,pady=0)
        lbltitle.pack(side=TOP,fill=X)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="sky blue")
        frame.place(x=0,y=130,width=1530,height = 400)

#=====================frame for library membership in Left=======================================================================================================================================
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION",bg = "sky blue",fg ="brown",bd=12,relief=RIDGE,font=("times new roman",16,"bold"),padx=0,pady=0)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember = Label(DataFrameLeft,bg='sky blue',fg='black',text="Member Type",font=("arial",13,"bold"),padx=0,pady=0)
        lblMember.grid(row=0,column=0,sticky=W)


        ComMember =ttk.Combobox(DataFrameLeft,font=("arial",15,),textvariable=self.member_var,width =22,state="readonly")
        ComMember["value"] = ("Admin","Students","Lecturer")
        ComMember.current(0)
        ComMember.grid(row=0,column=1)

        lblPRN_No = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN No:", padx=2, bg="sky blue")
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1,column = 1)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID No:", padx=2, pady=4, bg="sky blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="FirstName:", padx=2, pady=6, bg="sky blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="LastName:", padx=2, pady=6,bg="sky blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        lblLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.lastname_var, width=29)
        lblLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"),text="Address1:", padx=2, pady=6, bg="sky blue")
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address2:", padx=2, pady=2,bg="sky blue")
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.adress2_var, width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=4,bg="sky blue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=6, bg="sky blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Id:", padx=2, bg="sky blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=6,bg="sky blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuther = Label(DataFrameLeft, font=("arial", 12, "bold"), text= "Author: ", padx=2, pady=6, bg="sky blue")
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.author_var,width=29)
        txtAuther.grid(row=2, column=3)

        lblDataBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Data Borrowed:", padx=2, pady=6,bg="sky blue")
        lblDataBorrowed.grid(row=3, column=2, sticky=W)
        txtDataBorrowed = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.dateborrowed_var,width=29)
        txtDataBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6,bg="sky blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=6,bg="sky blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.daysonbook, width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6,bg="sky blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.lateratefine_var, width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverdate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6,bg="sky blue")
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.dateoverdue, width=29)
        txtDateOverdate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6,bg="sky blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.finallprice,width=29)
        txtActualPrice.grid(row=8, column=3)


        #====================== frame for Book details in Right ==========================================================================================================================================
        DataFrameRight = LabelFrame(frame, text="BOOK DETAILS", bg="sky blue", fg="brown", bd=12, relief=RIDGE, font=("times new roman", 16, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=870, y=5, width=580, height=350)


        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky ='ns')


        listBooks = ["Python Crash Course","Automate the Boring Stuff with Python","Fluent Python",
                   "Learning Python ",
                   "Effective JAVA: 90 Specific Ways to Write Better JAVA",
                   "HTML & CSS Cookbook",
                   "Think Data Science: How to Think Like a Computer Scientist",
                   "Python for Data Analysis",
                   "Learning Facebook Design & Patterns",
                   "Dive into Python 3 by Mark Pilgrim","Algorithmic", "Data", "Computer", "Programming", "Network",
                   "Artificial Intelligence", "Machine Learning", "Software", "Cybersecurity", "Operating System", "Database",
                   "Web", "Cloud", "Computer Vision", "Robotics", "Digital", "Blockchain", "IoT", "Big Data", "Human-Computer Interaction",
                   "Design", "Analysis", "Systems", "Engineering", "Security", "Development", "Architecture", "Computing", "Theory", "Applications",
                   "Technology", "Paradigms", "Optimization", "Tools", "Foundations", "Frameworks", "Protocols", "Principles", "Innovation", "Challenges"]

        def SelectBook(event=" "):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x=="Python Crash Course"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Crash Course")
                self.author_var.set("paul Berry")

                d1 = datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3= d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("100 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("789 tk")

            elif (x=="Automate the Boring Stuff with Python"):
                self.bookid_var.set("BKID5451")
                self.booktitle_var.set("Automate the Boring Stuff with Python")
                self.author_var.set("Lincon")

                d1 = datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3= d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("100 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("699 tk")

            elif (x=="Fluent Python"):
                self.bookid_var.set("BKID5353")
                self.booktitle_var.set("Fluent Python")
                self.author_var.set("peter lucy")

                d1 = datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3= d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("250 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("999 tk")

            elif (x == "Learning Python"):
                self.bookid_var.set("BKID5017")
                self.booktitle_var.set("Learning Python")
                self.author_var.set("George mickel")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("70 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("659 tk")

            elif (x == "Effective JAVA: 90 Specific Ways to Write Better JAVA"):
                self.bookid_var.set("BKID5119")
                self.booktitle_var.set("Effective JAVA: 90 Specific Ways to Write Better JAVA")
                self.author_var.set(" Rahul varma")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("70 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("350 tk")

            elif (x == "HTML & CSS Cookbook"):
                self.bookid_var.set("BKID79851")
                self.booktitle_var.set("HTML & CSS Cookbook")
                self.author_var.set("Subin Tamim")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("110 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("890 tk")

            elif (x == "Think Data Science: How to Think Like a Computer Scientist"):
                self.bookid_var.set("BKID29857")
                self.booktitle_var.set("Think Data Science: How to Think Like a Computer Scientist")
                self.author_var.set("Rabindranath Tagor")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("500 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("1250 tk")

            elif (x == "Python for Data Analysis"):
                self.bookid_var.set("BKID59817")
                self.booktitle_var.set("Python for Data Analysis")
                self.author_var.set("Mark Robinson ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("250 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("1380 tk")

            elif (x == "Learning Facebook Design & Patterns"):
                self.bookid_var.set("BKID99837")
                self.booktitle_var.set("Learning Facebook Design & Patterns")
                self.author_var.set("Mark jukarberg ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("50 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("755 tk")

            elif (x == "Dive into Python 3 by Mark Pilgrim"):
                self.bookid_var.set("BKID918300")
                self.booktitle_var.set("Dive into Python 3 by Mark Pilgrim")
                self.author_var.set("Mark Pilgrim ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("50 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("599 tk")

            elif (x == "Algorithmic"):
                self.bookid_var.set("BKID18310")
                self.booktitle_var.set("Algorithmic")
                self.author_var.set("Nazrul Islam")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("125 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("593 tk")

            elif (x == "Data"):
                self.bookid_var.set("BKID18319")
                self.booktitle_var.set("Data")
                self.author_var.set("Ashaf uddaula")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("50 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("200 tk")

            elif (x == "Artificial Intelligence"):
                self.bookid_var.set("BKID38399")
                self.booktitle_var.set("Artificial Intelligence")
                self.author_var.set("Mickle jackson")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("500 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("2000 tk")

            elif (x == "Machine Learning"):
                self.bookid_var.set("BKID38388")
                self.booktitle_var.set("Machine Learning")
                self.author_var.set("Virgil van Dijk")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("230 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("1834 tk")

            elif (x == "Computer Vision"):
                self.bookid_var.set("BKID110288")
                self.booktitle_var.set("Computer Vision")
                self.author_var.set("P.Luiz Rakin")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("230 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("1834 tk")

            elif (x == "Human-Computer Interaction"):
                self.bookid_var.set("BKID110578")
                self.booktitle_var.set("Human-Computer Interaction")
                self.author_var.set("P.Davis ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("200 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("2200 tk")

            elif (x == "Cybersecurity"):
                self.bookid_var.set("BKID696969")
                self.booktitle_var.set("Cybersecurity")
                self.author_var.set("Hennry peterson ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("150 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("1499 tk")

            elif (x == "Computer"):
                self.bookid_var.set("BKID13877")
                self.booktitle_var.set("Computer")
                self.author_var.set("Luis A. Abraham ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("110 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("1599 tk")

            elif (x == "Programming"):
                self.bookid_var.set("BKID67189")
                self.booktitle_var.set("Programming")
                self.author_var.set("Jack Buncker ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("80 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("820 tk")

            elif (x == "Network"):
                self.bookid_var.set("BKID5729")
                self.booktitle_var.set("Network")
                self.author_var.set("Ashaf uddaula ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("20 tk")
                self.dateoverdue.set("NO")
                self.finallprice.set("250 tk")



        listBox = Listbox(DataFrameRight,font=("arial", 12,'bold'),width=23,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)

        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview())

        for item in listBooks:
            listBox.insert(END,item)




#=============================Buttons Frame=======================================================================================================================================================
        FrameButton = Frame(self.root, bd=15, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=530, width=1530, height=65)

        btnAddData = Button(FrameButton, command=self.add_data, text='Add Data', font=("arial", 12, 'bold'), width=20,
                            bg='green', fg='white')
        btnAddData.grid(row=0, column=2, padx=5, sticky="nsew")  # Adjust padx and sticky parameters as needed

        btnShowDetails = Button(FrameButton, command=self.show_details, text='Show Details', font=("arial", 12, 'bold'),
                                width=20, bg='blue', fg='white')
        btnShowDetails.grid(row=0, column=4, padx=5, sticky="nsew")  # Adjust padx and sticky parameters as needed

        btnDelete = Button(FrameButton,command=self.removeData, text='Delete', font=("arial", 12, 'bold'), width=20, bg='red', fg='white')
        btnDelete.grid(row=0, column=6, padx=5, sticky="nsew")  # Adjust padx and sticky parameters as needed

        btnExit = Button(FrameButton, command=self.prog_exit, text='Exit', font=("arial", 12, 'bold'), width=20,
                         bg='Orange', fg='white')
        btnExit.grid(row=0, column=8, padx=5, sticky="nsew")  # Adjust padx and sticky parameters as needed

        #============================ Information Frame===================================================================================================================================================

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="sky blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=12, relief=RIDGE, bg="white")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, columns=("membertype", "prnno", "title", "firstname",
                                                                "lastname", "address1", "address2",
                                                                "postid", "mobile", "bookid", "booktitle", "author",
                                                                "dateborrowed", "datedue", "days",
                                                                "latereturnfine", "dateoverdue", "finalprice"),
        xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="ID")
        self.library_table.heading("prnno", text="Member Type")
        self.library_table.heading("title", text="PRN No")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile No")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days on books")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Overdue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table['show'] = 'headings'
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)




    def add_data(self):
        conn = mysql.connector.connect(host ="localhost",username = "root",password ='',database="library_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("""
            INSERT INTO library 
            (member_type, prn_no, id, first_name, last_name, address_1, address_2, post_id, mobile_no, book_id, 
            book_title, author, date_borrowed, date_due, days_on_books, late_return_fine, date_overdue, final_price) 
            VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.adress2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook.get(),
            self.lateratefine_var.get(),
            self.dateoverdue.get(),
            self.finallprice.get()
        ))
        conn.commit()

        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")
        
#Show details button work
    def show_details(self):
        conn = mysql.connector.connect(host="localhost", username="root", password='',
                                       database="library_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM library")
        rows = my_cursor.fetchall()

        # Clear existing data from the Treeview
        for record in self.library_table.get_children():
            self.library_table.delete(record)

        # Insert fetched data into the Treeview
        for row in rows:
            self.library_table.insert('', 'end', values=row)

        # Commit changes and close connection
        conn.commit()
        conn.close()
#Exist button work
    def prog_exit(self):
        self.root.destroy()

    def removeData(self):
        # Get the selected item from the TreeView
        selected_item = self.library_table.focus()

        # Check if any item is selected
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to delete.")
            return

        # Retrieve the values of the selected record
        selected_values = self.library_table.item(selected_item, "values")

        # If you need the ID specifically, you can retrieve it like this:
        selected_id = selected_values[0]

        try:
            # Connect to the MySQL database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="library_management_system"
            )

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Construct the DELETE query
            delete_query = "DELETE FROM library WHERE id = %s"

            # Execute the query with the selected ID
            cursor.execute(delete_query, (selected_id,))

            # Commit the changes to the database
            connection.commit()

            # Display a message confirming the deletion
            messagebox.showinfo("Success", "Record deleted successfully!")

            # Update the TreeView after deletion
            self.show_details()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error deleting record: {error}")

        finally:
            # Close the cursor and database connection
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop() #window open houar por jeno sathe sathe close na hoy fixed thake


