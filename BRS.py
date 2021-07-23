import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import datetime
from tkcalendar import Calendar, DateEntry
import tkcalendar
import os

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.rowconfigure(0, weight=1)
        
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, Register, Dashboard, Books, Authors, Genres, Borrowers, Order, History, Report):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, page_number):

        frame = self.frames[page_number]
        frame.tkraise()
        

class Login(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 1350, bg="#445a67")
        leftcolor.place(x=0,y=0)

        login = StringVar()
        password = StringVar()

        self.books = PhotoImage(file="books.png", master=self)
        
        applogo = tk.Label(self, image = self.books,bd=0,
                            bg="#445a67",)
        applogo.place(x=530,y=25)
        apptitle = tk.Label(self, text="BOOK RENTAL SYSTEM", font=("Impact",30),bd=0,
                            bg="#445a67",
                            fg="snow",)
        apptitle.place(x=505,y=330)
        
        def Database():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL)")
            cur.execute("CREATE TABLE IF NOT EXISTS online_user (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL)")
            conn.commit() 
            conn.close()
        
        def Login():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur1 = conn.cursor()
            cur1.execute("SELECT * FROM user")
            users = cur1.fetchall()
            if login.get == "" or password.get() == "":
                tkinter.messagebox.showerror("Book Rental System", "Please require the completed field")
            else:
                cur.execute("SELECT * FROM user WHERE username = ? and password = ?", (login.get(), password.get()))
                if cur.fetchone() is not None:
                    for user in users:
                        if login.get() == user[0]:
                            cur1.execute("INSERT INTO online_user(username, password, role) VALUES(?,?,?)",(login.get(),password.get(),user[2]))
                    tkinter.messagebox.showinfo("Book Rental System", "Login Successfully")
                    controller.show_frame(Dashboard)
                    login.set('')
                    password.set('')
                    
                else:
                    tkinter.messagebox.showerror("Book Rental System", "Invalid password or username")
                    
                
            conn.commit() 
            conn.close()
        
        self.lbllogin = tk.Label(self, text="Username", bg="#445a67", fg = "snow", font=("Century Gothic",15))
        self.lbllogin.place(x=628,y=450)
        
        self.entrylogin = Entry(self, font=("Poppins", 11), textvariable=login, bd=0,width=41)
        self.entrylogin.place(x=510,y=485)
        
        self.lblpass = tk.Label(self, text="Password", bg="#445a67", fg = "snow", font=("Century Gothic",15))
        self.lblpass.place(x=630,y=520)
        
        self.entrypass = Entry(self, font=("Poppins", 11), textvariable=password, bd=0,width=41, show="*")
        self.entrypass.place(x=510,y=555)
          
        self.login = Button(self,font=("Century Gothic", 12,"underline"), text="Login", bd=0, bg="#445a67", fg="snow",
                                    command=Login)
        self.login.config(cursor= "hand2")
        self.login.place(x=650,y=590)
        
        self.reg = Button(self,font=("Century Gothic", 12,"underline"), text="Register", bd=0, bg="#445a67", fg="snow",
                                    command=lambda: controller.show_frame(Register))
        self.reg.config(cursor= "hand2")
        self.reg.place(x=640,y=625)
        
        Database()

class Register(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 1350, bg="#445a67")
        leftcolor.place(x=0,y=0)

        
        login = StringVar()
        password = StringVar()
        role= StringVar()
        
        self.books = PhotoImage(file="books.png", master=self)
        
        applogo = tk.Label(self, image = self.books,bd=0,
                            bg="#445a67",)
        applogo.place(x=540,y=25)
        apptitle = tk.Label(self, text="BOOK RENTAL SYSTEM", font=("Impact",30),bd=0,
                            bg="#445a67",
                            fg="snow",)
        apptitle.place(x=505,y=330)
        
        def Database():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL)")
            conn.commit() 
            conn.close()
            
        def register():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            if  login.get() == "" or password.get() == "" or role.get() == "":
                tkinter.messagebox.showerror("Book Rental System", "Please require the completed field")
            else:
                cur.execute("SELECT * FROM user WHERE username = ?", (login.get(),))
                if cur.fetchone() is not None:
                    tkinter.messagebox.showerror("Book Rental System", "Username is already taken")
                else:
                    cur.execute("INSERT INTO user (username, password,role) VALUES(?, ?, ?)", \
                               (login.get(), password.get(), role.get()))
                    conn.commit()
                    login.set("")
                    password.set("")
                    role.set("")
                    tkinter.messagebox.showinfo("Book Rental System", "Successfully created")
            cur.close()
            conn.close()
               
        
        self.lbllogin = tk.Label(self, text="Username", bg="#445a67", fg = "snow", font=("Century Gothic",15))
        self.lbllogin.place(x=628,y=390)
        
        self.entrylogin = Entry(self, font=("Poppins", 11), textvariable=login, bd=0,width=41)
        self.entrylogin.place(x=510,y=420)
        
        self.lblpass = tk.Label(self, text="Password", bg="#445a67", fg = "snow", font=("Century Gothic",15))
        self.lblpass.place(x=630,y=455)
        
        self.entrypass = Entry(self, font=("Poppins", 11), textvariable=password, bd=0,width=41, show="*")
        self.entrypass.place(x=510,y=485)

        self.lblrole = tk.Label(self, text="Role:", bg="#445a67", fg = "snow", font=("Century Gothic",15))
        self.lblrole.place(x=650,y=520)

        self.entryrole = ttk.Combobox(self, value=["Admin", "Staff"], font=("Poppins", 11),
                                             state="readonly", textvariable=role, width=39)
        self.entryrole.place(x=510,y=550)

          
        self.login = Button(self,font=("Century Gothic", 12,"underline"), text="Login", bd=0, bg="#445a67", fg="snow",
                                    command=lambda: controller.show_frame(Login))
        self.login.config(cursor= "hand2")
        self.login.place(x=650,y=626)

        self.reg = Button(self,font=("Century Gothic", 12,"underline"), text="Register", bd=0, bg="#445a67", fg="snow",
                                    command=register)
        
        self.reg.config(cursor= "hand2")
        self.reg.place(x=640,y=590)

        Database()
        
class Dashboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
       
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        self.books1=PhotoImage(file="books1.png", master=self)
        self.totalbooks=PhotoImage(file="bookdash.png", master=self)
        self.availbooks=PhotoImage(file="availdash.png", master=self)
        self.borrower=PhotoImage(file="borrower.png", master=self)
        self.ret=PhotoImage(file="ret.png", master=self)
        self.notret=PhotoImage(file="notret.png", master=self)
        self.report=PhotoImage(file="report.png", master=self)
        self.issue=PhotoImage(file="issue.png", master=self)
        self.calen=PhotoImage(file="calendar.png", master=self)
        
        totalbooks = tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "     Total Books\n", anchor=SW)
        totalbooks.place(x=205,y=125)
        bookicon = tk.Label(self,image=self.availbooks, bd=0, bg="#375971")
        bookicon.place(x=360,y=145)
        
        booksavailable= tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "  Books Available\n", anchor=SW)
        booksavailable.place(x=490,y=125)
        booksavailableicon = tk.Label(self,image=self.totalbooks, bd=0, bg="#375971")
        booksavailableicon.place(x=655,y=145)
        
        totalborrower = tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "  Total Borrowers\n", anchor=SW)
        totalborrower.place(x=780,y=125)
        totalborrower = tk.Label(self, image=self.borrower, bd=0, bg="#395971")
        totalborrower.place(x=935,y=145)
        
  
        totalreport = tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "     Total Reports\n", anchor=SW)
        totalreport.place(x=1066,y=125)
        reporticon = tk.Label(self,image=self.report, bg="#375971", bd=0)
        reporticon.place(x=1210,y=145)
        
        issued = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="          Issued", anchor=N)
        issued.place(x=205,y=300)
        issuedicon = tk.Label(self, image=self.issue, bg="#375971",bd=0)
        issuedicon.place(x=215,y=308)
        
        returned = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="        Returned", anchor=N)
        returned.place(x=490,y=300)
        like = tk.Label(self, image=self.ret, bg="#375971",bd=0)
        like.place(x=500,y=320)
        
        notreturned = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="\tNot Returned", anchor=N)
        notreturned.place(x=780,y=300)
        dislike = tk.Label(self, image=self.notret, bg="#375971",bd=0)
        dislike.place(x=780,y=320)

        cdate = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="\tDate Today", anchor=N)
        cdate.place(x=1066,y=300)
        clendaricon = tk.Label(self, image=self.calen, bd=0, bg="#375971")
        clendaricon.place(x=1070,y=320)
        
        calendar =  tk.Label(self,font=("Century Gothic", 15),padx=2, pady=7, height = 10,width = 45,
                            bg="#375971",fg="snow",text="          Calendar", anchor=W)
        calendar.place(x=205,y=430)
        
        borrower =  tk.Label(self,font=("Century Gothic", 15),padx=2, pady=7, height = 10,width = 45,
                            bg="#375971",fg="snow",text=" ", anchor=W)
        borrower.place(x=780,y=430)
        
        label = tk.Label(self, text="Dashboard", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)
        
        tbooks = StringVar()
        tnotreturned = StringVar()
        history = StringVar()
        tbooksavailable = StringVar()
        tgenre = StringVar()
        tissued = StringVar()
        treturned = StringVar()
        treport = StringVar()
        tborrower = StringVar()
        
        def connect():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS books (BookNumber VARCHAR(10) PRIMARY KEY, ISBN VARCHAR(16) NOT NULL, Title VARCHAR(50) NOT NULL, Status VARCHAR(10) NOT NULL)") 
            cur.execute("CREATE TABLE IF NOT EXISTS return (returnID INTEGER PRIMARY KEY AUTOINCREMENT, BookNumber VARCHAR(10), ISBN VARCHAR(16) NOT NULL, Title VARCHAR(50) NOT NULL, Author VARCHAR(100) NOT NULL, Genre VARCHAR(100) NOT NULL)")
            cur.execute("CREATE TABLE IF NOT EXISTS borrower (BorrowerIDNum VARCHAR(9) PRIMARY KEY, ValidID VARCHAR(100) NOT NULL, Name VARCHAR(50) NOT NULL, EmailAdd VARCHAR(50) NOT NULL, PhoneNum VARCHAR(11) NOT NULL)")           
            conn.commit() 
            conn.close()
            
        def connectAuthor():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS authors (BookNumber VARCHAR(10) NOT NULL,\
                      	author  VARCHAR(100) NOT NULL,\
                    	PRIMARY KEY(BookNumber, author),\
                      	FOREIGN KEY(BookNumber) REFERENCES books(BookNumber) ON  UPDATE CASCADE)")
            conn.commit() 
            conn.close()
            
        def connectGenre():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS genres (BookNumber VARCHAR(10)  NOT NULL,\
                      	genre  VARCHAR(100) NOT NULL,\
                       	PRIMARY KEY(BookNumber, genre),\
                      	FOREIGN KEY(BookNumber) REFERENCES books(BookNumber) ON  UPDATE CASCADE)")
            conn.commit() 
            conn.close()
            
        def connectOrder():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS rent (RentOrderNo INTEGER PRIMARY KEY AUTOINCREMENT, BookNumber VARCHAR(10) NOT NULL, BorrowersID VARCHAR(9) NOT NULL, \
                        DateBorrowed DATE NOT NULL, DueDate DATE NOT NULL, \
                        FOREIGN KEY(BookNumber) REFERENCES books(BookNumber) ON UPDATE CASCADE,\
                        FOREIGN KEY(BorrowersID) REFERENCES borrower(BorrowerIDNum) ON UPDATE CASCADE)") 
            conn.commit() 
            conn.close()
            
        def connectHistory():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS history (RentOrderNo INTEGER PRIMARY KEY AUTOINCREMENT, BookNumber VARCHAR(10) NOT NULL, BorrowersID VARCHAR(9) NOT NULL, \
                         DateBorrowed DATE NOT NULL, DueDate DATE NOT NULL, ReturnDate DATE NOT NULL, \
                         FOREIGN KEY(BookNumber) REFERENCES books(BookNumber) ON UPDATE CASCADE, \
                         FOREIGN KEY(BorrowersID) REFERENCES borrower(BorrowerIDNum) ON UPDATE CASCADE)") 
            conn.commit() 
            conn.close()
            
        def connectReport():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS report (ReportOrderNo INTEGER PRIMARY KEY AUTOINCREMENT, BIDNum VARCHAR(9) NOT NULL, Name VARCHAR(50) NOT NULL, BookNumber VARCHAR(10) NOT NULL,\
                        DateBorrowed DATE NOT NULL, DueDate DATE NOT NULL, ReturnDate DATE NOT NULL, \
                        FOREIGN KEY(BIDNum) REFERENCES borrower(BorrowerIDNum) ON UPDATE CASCADE,\
                        FOREIGN KEY(BookNumber) REFERENCES books(BookNumber) ON UPDATE CASCADE)") 
            conn.commit() 
            conn.close()
        
        def books():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM books")
            rows = cur.fetchall()
            tbooks.set(len(rows))
            self.ttlbooks = Label(self, font=("Impact", 40),textvariable = tbooks, bg ="#375971", fg = "snow")
            self.ttlbooks.place(x=275,y=150)
            self.after(1000,books)
            conn.commit()            
            conn.close()
            
        def booksavail():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur2 = conn.cursor()
            cur.execute("SELECT * FROM books")
            cur2.execute("SELECT * FROM rent")
            rows = cur.fetchall()
            rows2 = cur2.fetchall()
            total = len(rows) - len(rows2)
            tbooksavailable.set(total)
            self.ttlbooksavailable = Label(self, font=("Impact", 40),textvariable = tbooksavailable, bg ="#375971", fg = "snow")
            self.ttlbooksavailable.place(x=565,y=150)
            self.after(1000,booksavail)
            conn.commit()            
            conn.close()
            
        def borrower():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM borrower")
            rows = cur.fetchall()
            tborrower.set(len(rows))
            self.tborrowers = Label(self, font=("Impact", 40),textvariable = tborrower, bg ="#375971", fg = "snow")
            self.tborrowers.place(x=850,y=150)
            self.after(1000,borrower)
            conn.commit()            
            conn.close()
        
        def issued():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM history")
            rows = cur.fetchall()
            tissued.set(len(rows))
            self.tissued = Label(self, font=("Impact", 40),textvariable = tissued, bg ="#375971", fg = "snow")
            self.tissued.place(x=360,y=330)
            self.after(1000,issued)
            conn.commit()            
            conn.close()
            
        def returned():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur1 = conn.cursor()
            cur.execute("SELECT * FROM rent")
            cur1.execute("SELECT * FROM return")
            rows = cur.fetchall()
            rows2 = cur1.fetchall()
            treturned.set(len(rows2))
            self.ttlreturned = Label(self, font=("Impact", 40),textvariable = treturned, bg ="#375971", fg = "snow")
            self.ttlreturned.place(x=650,y=330)
            self.after(1000,returned)
            conn.commit()            
            conn.close()
        
        def notreturned():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM rent")
            rows = cur.fetchall()
            tnotreturned.set(len(rows))
            self.ttlnotreturned = Label(self, font=("Impact", 40),textvariable = tnotreturned, bg ="#375971", fg = "snow")
            self.ttlnotreturned.place(x=940,y=330)
            self.after(1000,notreturned)
            conn.commit()            
            conn.close()
           
        def reports():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM report")
            rows = cur.fetchall()
            treport.set(len(rows))
            self.ttlreport = Label(self, font=("Impact", 40),textvariable = treport, bg ="#375971", fg = "snow")
            self.ttlreport.place(x=1150,y=150)
            self.after(1000,reports)
            conn.commit()            
            conn.close()

        lab = Label(self, font=("Century Gothic",15), bg="#375971",fg="snow")
        lab.place(x=1180,y=340)

        def clock():
            time = datetime.datetime.now().strftime("%b/ %d /%Y")
            lab.config(text=time)
            self.after(1000, clock)
            
        cal = Calendar(self, selectmode='day', year=2021, month=7, font=("Century Gothic",12),foreground ="black",\
                       background = "#ccbe96", headersbackground = "#eed799" , normalbackground = "white", weekendbackground="white",\
                       othermonthbackground="white", othermonthwebackground='white')
        
        def calendar():
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur1 = con.cursor()
            cur.execute("SELECT * FROM rent")
            cur1.execute("SELECT * FROM report")
            dates = cur.fetchall()    
            rdates = cur1.fetchall()
            due_date = {} 
            returned_date = {}
            
            for date in dates:
                due_date[date[4]] = ('date','due_date')
                
            for rdate in rdates:
                returned_date[rdate[6]] = ('date','returned_date')
                
            for k in due_date.keys():
                date=datetime.datetime.strptime(k,"%m/%d/%Y").date()
                cal.calevent_create(date, due_date[k][0], due_date[k][1])
             
            for r in returned_date.keys():
                date=datetime.datetime.strptime(r,"%m/%d/%Y").date()
                cal.calevent_create(date, returned_date[r][0], returned_date[r][1])
                
            cal.tag_config('due_date', background='red', foreground='white')
            cal.tag_config('returned_date', background='black', foreground='white')
            cal.place(x=435,y=438)
            
        def grabdate():
            date = cal.get_date()
            a = date.split("/") 
            m = ""
            d = ""
            y = ""
            if len(a[0]) == 1:
                m = "0" + str(a[0]) 
            else:
                m = a[0]
                
            if len(a[1]) == 1:
                d = "0" + str(a[1]) 
            else:
                d = a[1]
                    
            if len(a[2]) == 2:
                y = "20" + str(a[2]) 
            else:
                y = a[2] 
                
            dates = m+"/"+d+"/"+y
            
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur2 = conn.cursor()
            cur.execute("SELECT * FROM rent")
            cur2.execute("SELECT * FROM report")
            rows = cur.fetchall()
            reports = cur2.fetchall()
            booknum_list = []
            borrower_list = []
            duedate_list = []
            
            for row in rows:
                if row[4] == dates:
                    booknum_list.append(row[1])
                    borrower_list.append(row[2])
                    my_date.config(text=dates)
                    for i in borrower_list:    
                        my_borrower.config(text=borrower_list)
                    for i in booknum_list:
                        my_booknum.config(text=booknum_list)
                        
                    self.lblddate.place(x=2085,y=530) 
                    my_ddate.place(x=2085,y=570)
                    for i in duedate_list:
                        my_ddate.config(text=duedate_list)
                else:
                    pass
            
            for report in reports:
                if report[6] == dates:
                    borrower_list.append(report[1])
                    booknum_list.append(report[3])
                    duedate_list.append(report[5])
                    my_date.config(text=dates)
                    for i in borrower_list:    
                        my_borrower.config(text=borrower_list)
                    for i in booknum_list:
                        my_booknum.config(text=booknum_list)
                    
                    self.lblddate.place(x=1085,y=530) 
                    my_ddate.place(x=1100,y=570)
                    for i in duedate_list:
                        my_ddate.config(text=duedate_list)
                else:
                    pass
        
        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()
        
        my_button = Button(self, font=("Century Gothic",10,"underline"), text = "Select Date", bg ="#375971", fg = "snow", bd=0,command = grabdate)
        my_button.place(x=1010, y=650)
        my_button.config(cursor= "hand2")
        
        my_borrower = Label(self, font=("Century Gothic",13), width = 20, bg ="#375971", fg = "snow", text="")   
        my_borrower.place(x=815,y=480)
        
        my_booknum = Label(self, font=("Century Gothic",13), width = 20, bg ="#375971", fg = "snow", text="")   
        my_booknum.place(x=800,y=570)
        
        my_date = Label(self, font=("Century Gothic",13), width = 10, bg ="#375971", fg = "snow", text="")   
        my_date.place(x=1100,y=480)
        
        my_ddate = Label(self, font=("Century Gothic",13), width = 20, bg ="#375971", fg = "snow", text="")   
                        
        self.lblborrowerid = Label(self, font=("Century Gothic", 12), text="Borrower's ID:", bg ="#375971", fg = "snow", padx=5, pady=5)
        self.lblborrowerid.place(x=800,y=440)
        
        self.lblbooknum = Label(self, font=("Century Gothic", 12), text="Book Number:", bg ="#375971", fg = "snow", padx=5, pady=5)
        self.lblbooknum.place(x=800,y=530)
        
        self.lbldate = Label(self, font=("Century Gothic", 12), text="Date:", padx=5, bg ="#375971", fg = "snow", pady=5)
        self.lbldate.place(x=1085,y=440)    
        
        self.lblddate = Label(self, font=("Century Gothic", 12), text="Due Date:", padx=5, bg ="#375971", fg = "snow", pady=5)
        
        ## Window Buttons

        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")
        
        connect()
        connectAuthor()
        connectGenre()
        connectOrder()
        connectHistory()
        connectReport()
        books()
        booksavail()
        issued()
        returned()
        notreturned()
        clock()
        borrower()
        reports()
        calendar()

class Books(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        self.books1=PhotoImage(file="books1.png", master=self)
        
        label = tk.Label(self, text="Books", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)

        
        BookNumber = StringVar()
        ISBN = StringVar()
        Title = StringVar()
        Author1 = StringVar()
        Author2 = StringVar()
        Author3 = StringVar()
        Author4 = StringVar()
        Author = StringVar()
        Genre = StringVar()
        Genre2 = StringVar()
        Genre3 = StringVar()
        Genre4 = StringVar()
        Genre5 = StringVar()
        Genre6 = StringVar()
        Genre7 = StringVar()
        Genre8 = StringVar()
        Genre9 = StringVar()
        Genre10 = StringVar()
        Search = StringVar()
        SearchAvail = StringVar()
        Showby = StringVar()
        Status = StringVar()
        Searchby = StringVar()
        Sortby = StringVar()
        
        def addBook():
            def add():
                if BookNumber.get() == "" or ISBN.get() == "" or Title.get() == "" or Author.get() == "" or Genre.get() == "":
                    tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
                else:
                    self.Genres = [Genre.get(),Genre2.get(),Genre3.get(),Genre4.get(),Genre5.get(),Genre6.get(),Genre7.get(),\
                                   Genre8.get(),Genre9.get(),Genre10.get()]
                    self.Authors = [Author.get(),Author1.get(),Author2.get(), Author3.get(), Author4.get()]
                    conn = sqlite3.connect("BRS.db")
                    c = conn.cursor()
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM online_user")
                    c_user = cur.fetchall()
                    for role in c_user:
                        if role[2] == "Staff":
                            tkinter.messagebox.showerror("Book Rental System", "Only admin can add books")
                        else:
                            c.execute("INSERT INTO books(BookNumber, ISBN, Title, Status) VALUES (?,?,?,'Available')",\
                                      (BookNumber.get(),ISBN.get(),Title.get()))
                            for genre in self.Genres:
                                if genre != "":
                                     c.execute("INSERT INTO genres VALUES(?,?)",(BookNumber.get(), genre))
                            for author in self.Authors:
                                if author != "":
                                     c.execute("INSERT INTO authors VALUES (?,?)",(BookNumber.get(), author))
                            conn.commit()  
                            tkinter.messagebox.showinfo("Book Rental System", "Book added to database")
                            displayBook()
                            clear()
                            
                    conn.close()
                    self.addWindow.destroy()

            self.addWindow = Toplevel(bg='#f5f5f5')
            self.addWindow.geometry("1200x700")
            self.addWindow.resizable(0,0)
            self.addWindow.geometry("+{}+{}".format(positionRight+300, positionDown+0))

            uppercolor = tk.Label(self.addWindow,height = 3,width = 500, bg="#375971")
            uppercolor.place(x=0,y=0)
            loweruppercolor = tk.Label(self.addWindow,height = 3,width = 500, bg="#90a3b0")
            loweruppercolor.place(x=0,y=50)

            label = tk.Label(self.addWindow, text="BOOK INFORMATION", bg="#90a3b0", font=("Century Gothic", 20))
            label.place(x=10,y=55)

            
            self.lblBookNumber = Label(self.addWindow, font=("Poppins", 12, "bold"), text="Book Number:", bg='#f5f5f5', padx=5, pady=5)
            self.lblBookNumber.place(x=10,y=150)
            self.txtBookNumber = Entry(self.addWindow, font=("Poppins", 13), textvariable=BookNumber, width=43)
            self.txtBookNumber.place(x=50, y=190)
            
            self.lblISBN = Label(self.addWindow, font=("Poppins", 12, "bold"), text="ISBN:", bg='#f5f5f5', padx=5, pady=5)
            self.lblISBN.place(x=10,y=230)
            self.txtISBN = Entry(self.addWindow, font=("Poppins", 13), textvariable=ISBN, width=43)
            self.txtISBN.place(x=50, y=270)

            self.lblTitle = Label(self.addWindow, font=("Poppins", 12, "bold"), text="Title:", bg='#f5f5f5', padx=5, pady=5)
            self.lblTitle.place(x=10,y=310)
            self.txtTitle = Entry(self.addWindow, font=("Poppins", 13), textvariable=Title, width=43)
            self.txtTitle.place(x=50, y=350)

            self.lblAuthor = Label(self.addWindow, font=("Poppins", 12, "bold"), text="AUTHORS:", bg='#f5f5f5', padx=5, pady=5)
            self.lblAuthor.place(x=10,y=390)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author, width=43)
            self.txta1.place(x=50, y=430)
            
            self.txta2 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author1, width=43)
            self.txta2.place(x=50, y=470)

            self.txta3 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author2, width=43)
            self.txta3.place(x=50, y=510)
            
            self.txta4 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author3, width=43)
            self.txta4.place(x=50, y=550)

            self.txta5 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author4, width=43)
            self.txta5.place(x=50, y=590)
            
            
            self.lblGenre = Label(self.addWindow, font=("Poppins", 12, "bold"), text="GENRES:", bg='#f5f5f5', padx=5, pady=5)
            self.lblGenre.place(x=650,y=150)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre, width=43)
            self.txta1.place(x=700, y=190)
            
            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre2, width=43)
            self.txta1.place(x=700, y=230)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre3, width=43)
            self.txta1.place(x=700, y=270)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre4, width=43)
            self.txta1.place(x=700, y=310)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre5, width=43)
            self.txta1.place(x=700, y=350)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre6, width=43)
            self.txta1.place(x=700, y=390)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre7, width=43)
            self.txta1.place(x=700, y=430)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre8, width=43)
            self.txta1.place(x=700, y=470)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre9, width=43)
            self.txta1.place(x=700, y=510)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre10, width=43)
            self.txta1.place(x=700, y=550)

            self.Wadd=PhotoImage(file="add.png", master=self.addWindow)
            self.Wclear=PhotoImage(file="clear.png", master=self.addWindow)
            self.Wexit=PhotoImage(file="exit.png", master=self.addWindow)
            

            self.btnCLear = Button(self.addWindow, image=self.Wclear, bd=0 ,command=clear, bg="#f5f5f5")
            self.btnCLear.place(x=350,y=640)
            self.btnCLear.config(cursor= "hand2")
            
            self.btnAddBook = Button(self.addWindow, image=self.Wadd,  bd=0 ,command=add, bg="#f5f5f5")
            self.btnAddBook.place(x=500,y=640)
            self.btnAddBook.config(cursor= "hand2")

            self.btnAddBook = Button(self.addWindow, image=self.Wexit,  bd=0 ,command=iExit ,bg="#f5f5f5")
            self.btnAddBook.place(x=650,y=640)
            self.btnAddBook.config(cursor= "hand2")

        def displayBook():
            self.booklist.delete(*self.booklist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur1 = conn.cursor()
            cur2 = conn.cursor() 
            cur1.execute("SELECT * FROM books")
            cur2.execute("SELECT * FROM rent")
            rows = cur1.fetchall()
            rows2 = cur2.fetchall()
            
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber;")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            
            for book in rows:
                for rent in rows2:
                    if book[0]==rent[1]:
                        cur1.execute("UPDATE books SET BookNumber = ?,ISBN = ?, Title = ?, Status = 'Unavailable' WHERE BookNumber=?",\
                                     (book[0],book[1],book[2],book[0]))
                    else:
                        pass
            conn.commit()
            conn.close()
        
        def updateBook():
            x = self.booklist.focus()
            if x == "":
                tkinter.messagebox.showerror("Book Rental System", "Please select a record from the table.")
                return
            
            def update():
                if BookNumber.get() == "" or ISBN.get() == "" or Title.get() == "" or Author.get() == "" or Genre.get() == "":
                    tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
                else:
                    for selected in self.booklist.selection():
                        conn = sqlite3.connect("BRS.db")
                        cur = conn.cursor()
                        cur.execute("PRAGMA foreign_keys = ON")
                        cur.execute("UPDATE books SET BookNumber = ?,ISBN = ?, Title = ?, Status = ? WHERE BookNumber=?", \
                                    (BookNumber.get(),ISBN.get(),Title.get(),self.booklist.set(selected, '#6'), self.booklist.set(selected, '#1')))   
                        #cur.execute("UPDATE authors SET BookNumber = ?, Author = ? WHERE BookNumber=?", \
                                    #(BookNumber.get(),Author.get(),self.booklist.set(selected, '#1'))) 
                        #cur.execute("UPDATE genres SET BookNumber = ?, Genre = ? WHERE BookNumber=?", \
                                    #(BookNumber.get(),Genre.get(),self.booklist.set(selected, '#1')))
                        conn.commit()
                        tkinter.messagebox.showinfo("Books Rental System", "Book Updated Successfully")
                        displayBook()
                        clear()
                        conn.close()
                self.addWindow.destroy()

            self.addWindow = Toplevel(bg='#f5f5f5')
            self.addWindow.geometry("1200x700")
            self.addWindow.resizable(0,0)
            self.addWindow.geometry("+{}+{}".format(positionRight+300, positionDown+0))

            uppercolor = tk.Label(self.addWindow,height = 3,width = 500, bg="#375971")
            uppercolor.place(x=0,y=0)
            loweruppercolor = tk.Label(self.addWindow,height = 3,width = 500, bg="#90a3b0")
            loweruppercolor.place(x=0,y=50)

            label = tk.Label(self.addWindow, text="BOOK INFORMATION", bg="#90a3b0", font=("Century Gothic", 20))
            label.place(x=10,y=55)
            
            self.lblBookNumber = Label(self.addWindow, font=("Poppins", 12, "bold"), text="Book Number:", bg='#f5f5f5', padx=5, pady=5)
            self.lblBookNumber.place(x=10,y=150)
            self.txtBookNumber = Entry(self.addWindow, font=("Poppins", 13), textvariable=BookNumber, width=43)
            self.txtBookNumber.place(x=50, y=190)
            
            self.lblISBN = Label(self.addWindow, font=("Poppins", 12, "bold"), text="ISBN:", bg='#f5f5f5', padx=5, pady=5)
            self.lblISBN.place(x=10,y=230)
            self.txtISBN = Entry(self.addWindow, font=("Poppins", 13), textvariable=ISBN, width=43)
            self.txtISBN.place(x=50, y=270)

            self.lblTitle = Label(self.addWindow, font=("Poppins", 12, "bold"), text="Title:", bg='#f5f5f5', padx=5, pady=5)
            self.lblTitle.place(x=10,y=310)
            self.txtTitle = Entry(self.addWindow, font=("Poppins", 13), textvariable=Title, width=43)
            self.txtTitle.place(x=50, y=350)

            self.lblAuthor = Label(self.addWindow, font=("Poppins", 12, "bold"), text="AUTHORS:", bg='#f5f5f5', padx=5, pady=5)
            self.lblAuthor.place(x=10,y=390)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author, width=43)
            self.txta1.place(x=50, y=430)
            
            self.txta2 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author1, width=43)
            self.txta2.place(x=50, y=470)

            self.txta3 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author2, width=43)
            self.txta3.place(x=50, y=510)
            
            self.txta4 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author3, width=43)
            self.txta4.place(x=50, y=550)

            self.txta5 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Author4, width=43)
            self.txta5.place(x=50, y=590)
            
            
            self.lblGenre = Label(self.addWindow, font=("Poppins", 12, "bold"), text="GENRES:", bg='#f5f5f5', padx=5, pady=5)
            self.lblGenre.place(x=650,y=150)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre, width=43)
            self.txta1.place(x=700, y=190)
            
            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre2, width=43)
            self.txta1.place(x=700, y=230)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre3, width=43)
            self.txta1.place(x=700, y=270)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre4, width=43)
            self.txta1.place(x=700, y=310)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre5, width=43)
            self.txta1.place(x=700, y=350)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre6, width=43)
            self.txta1.place(x=700, y=390)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre7, width=43)
            self.txta1.place(x=700, y=430)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre8, width=43)
            self.txta1.place(x=700, y=470)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre9, width=43)
            self.txta1.place(x=700, y=510)

            self.txta1 = Entry(self.addWindow, font=("Poppins", 13), textvariable=Genre10, width=43)
            self.txta1.place(x=700, y=550)

            self.Wadd=PhotoImage(file="update.png", master=self.addWindow)
            self.Wclear=PhotoImage(file="clear.png", master=self.addWindow)
            self.Wexit=PhotoImage(file="exit.png", master=self.addWindow)
            
        
            self.btnCLear = Button(self.addWindow, image=self.Wclear, bd=0 ,command=clear,bg="#f5f5f5")
            self.btnCLear.place(x=350,y=640)
            self.btnCLear.config(cursor= "hand2")
            
            self.btnAddBook = Button(self.addWindow, image=self.Wadd,  bd=0 ,command=update ,bg="#f5f5f5")
            self.btnAddBook.place(x=500,y=640)
            self.btnAddBook.config(cursor= "hand2")

            self.btnAddBook = Button(self.addWindow, image=self.Wexit,  bd=0 ,command=iExit ,bg="#f5f5f5")
            self.btnAddBook.place(x=650,y=640)
            self.btnAddBook.config(cursor= "hand2")
            
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur1 = conn.cursor()
            
            values = self.booklist.item(x, "values")
            cur.execute("SELECT * FROM genres WHERE BookNumber = ?", (values[0],))
            genres = cur.fetchall()
            list_genres = []
            cur1.execute("SELECT * FROM authors WHERE BookNumber = ?", (values[0],))
            authors = cur1.fetchall()
            list_authors = [] 
            for genre in genres:
                list_genres.append(genre[1])
            for author in authors:
                list_authors.append(author[1])
            BookNumber.set(values[0])
            ISBN.set(values[1])
            Title.set(values[2])
            if list_authors[0] != "":
                Author.set(list_authors[0])
            else:
                pass
            try:
                if list_authors[1] is not None:
                    Author1.set(list_authors[1])
                else:
                    pass
            except:
                pass
            try:
                if list_authors[2] is not None:
                    Author2.set(list_authors[2])
                else:
                    pass
            except:
                pass
            try:
                if list_authors[3] is not None:
                    Author3.set(list_authors[3])
                else:
                    pass
            except:
                pass
            try:
                if list_authors[4] is not None:
                    Author4.set(list_authors[4])
                else:
                    pass
            except:
                pass
            
            if list_genres[0] != "":
                Genre.set(list_genres[0])
            else:
                pass
            try:
                if list_genres[1] is not None:
                    Genre2.set(list_genres[1])
                else:
                    pass
            except:
                pass

            try:
                if list_genres[2] is not None:
                    Genre3.set(list_genres[2])
                else:
                    pass
            except:
                pass
            try:
                if list_genres[3] is not None:
                    Genre4.set(list_genres[3])
                else:
                    pass
            except:
                pass
            
            try:
                if list_genres[4] is not None:
                    Genre5.set(list_genres[4])
                else:
                    pass
            except:
                pass
            try:
                if list_genres[5] is not None:
                    Genre6.set(list_genres[5])
                else:
                    pass
            except:
                pass
            try:
                if list_genres[6] is not None:
                    Genre7.set(list_genres[6])
                else:
                    pass
            except:
                pass
            try:
                if list_genres[7] is not None:
                    Genre8.set(list_genres[8])
                else:
                    pass
            except:
                pass
            try:
                if list_genres[8] is not None:
                    Genre9.set(list_genres[9])
                else:
                    pass
            except:
                pass
            try:
                if list_genres[9] is not None:
                    Genre10.set(list_genres[10])
                else:
                    pass
            except:
                pass
        
        def updateStatus():
            if BookNumber.get() == "" or ISBN.get() == "" or Title.get() == "" or Author.get() == "" or Genre.get() == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                conn = sqlite3.connect("BRS.db")
                cur = conn.cursor()
                cur1 = conn.cursor()
                cur2 = conn.cursor()
                cur1.execute("SELECT * FROM rent")
                cur2.execute("SELECT * FROM books")
                rents = cur1.fetchall()
                rentlist = []
                for rent in rents:
                    rentlist.append(rent[1])
                for selected in self.booklist.selection():
                    if BookNumber.get() not in rentlist:
                        #cur.execute("PRAGMA foreign_keys = ON")
                        cur.execute("UPDATE books SET BookNumber = ?,ISBN = ?, Title = ?, Status = 'Available' WHERE BookNumber=?", \
                                    (BookNumber.get(),ISBN.get(),Title.get(),self.booklist.set(selected, '#1')))  
                        conn.commit()
                        tkinter.messagebox.showinfo("Books Rental System", "Book Updated Successfully")
                        displayBook()
                        clear()
                        conn.close()
                    else:
                        pass
                            
        def deleteBook():   
            messageDelete = tkinter.messagebox.askyesno("Book Rental System", "Do you want to remove this book?")
            if messageDelete > 0:   
                try:
                    con = sqlite3.connect("BRS.db")
                    cur = con.cursor()
                    x = self.booklist.selection()[0]
                    id_no = self.booklist.item(x)["values"][0]
                    cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("DELETE FROM books WHERE BookNumber = ?",(id_no,))     
                    cur.execute("DELETE FROM authors WHERE BookNumber = ?",(id_no,))   
                    cur.execute("DELETE FROM genres WHERE BookNumber = ?",(id_no,))   
                    con.commit()
                    self.booklist.delete(x)
                    tkinter.messagebox.showinfo("Book Rental System", "Book deleted from database")
                    displayBook()
                    clear()
                    con.close()    
                except:
                    tkinter.messagebox.showinfo("Book Rental System", "Some people rented this book!")
                
        def searchBook():
            search = Search.get()
            searchby = Searchby.get()
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber;")
            con.commit()
            self.booklist.delete(*self.booklist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if searchby == "Book Number":
                    if row[0].startswith(search):
                        self.booklist.insert("", tk.END, text=row[0], values=(row[0],row[1],row[2],row[4],row[5],row[3]))
                elif searchby == "ISBN":
                    if row[1].startswith(search):
                        self.booklist.insert("", tk.END, text=row[0], values=(row[0],row[1],row[2],row[4],row[5],row[3]))
                elif searchby == "Title":
                    if row[2].count(search):
                        self.booklist.insert("", tk.END, text=row[0], values=(row[0],row[1],row[2],row[4],row[5],row[3]))
                elif searchby =="Author":
                    if row[4].count(search):
                        self.booklist.insert("", tk.END, text=row[0], values=(row[0],row[1],row[2],row[4],row[5],row[3]))
                elif searchby == "Genre":
                    if row[5].count(search):
                        self.booklist.insert("", tk.END, text=row[0], values=(row[0],row[1],row[2],row[4],row[5],row[3]))
                else:
                    if row[3].startswith(search):
                        self.booklist.insert("", tk.END, text=row[0], values=(row[0],row[1],row[2],row[4],row[5],row[3]))
            con.close()
        
        def showAll():
            displayBook()
            
        def showAllAvail():
            displayBook()
        
        def clear():
            BookNumber.set('')
            ISBN.set('')
            Title.set('')
            Author.set('')
            Author1.set('')
            Author2.set('')
            Author3.set('')
            Author4.set('')
            Genre.set('')
            Genre2.set('')
            Genre3.set('')
            Genre4.set('')
            Genre5.set('')
            Genre6.set('')
            Genre7.set('')
            Genre8.set('')
            Genre9.set('')
            
            
        def OnDoubleClick2(event):
            item = self.booklist.selection()[0]
            values = self.booklist.item(item, "values")
            BookNumber.set(values[0])
            ISBN.set(values[1])
            Title.set(values[2])
            Author.set(values[3])
            Genre.set(values[4])

        def sortBN():
            self.booklist.delete(*self.booklist.get_children())
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber\
                        ORDER BY books.BookNumber ASC")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            con.close()

        def sortISBN():
            self.booklist.delete(*self.booklist.get_children())
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber\
                        ORDER BY books.ISBN ASC")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            con.close()
            
        def sortTitle():
            self.booklist.delete(*self.booklist.get_children())
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber\
                        ORDER BY books.Title ASC")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            con.close()

        def sortAuthor():
            self.booklist.delete(*self.booklist.get_children())
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber\
                        ORDER BY authors.Author ASC")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            con.close()

        def sortGenre():
            self.booklist.delete(*self.booklist.get_children())
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber\
                        ORDER BY genres.Genre ASC")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            con.close()
            
        def sortStatus():
            self.booklist.delete(*self.booklist.get_children())
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber\
                        ORDER BY books.Status ASC")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            con.close()

        def iExit():
            self.addWindow.destroy()
    
            
        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()

        ## Window Buttons
        
        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")

         
        booklist = tk.Label(self,height = 2,width = 108, bg="#89E894")
        
        self.booklist = ttk.Treeview(self,
                                        columns=("Book Number","ISBN", "Title", "Author", "Book Genre","Status"),
                                        height = 23)

        self.booklist.heading("Book Number", text="Book Number", anchor=W)
        self.booklist.heading("ISBN", text="ISBN",anchor=W)
        self.booklist.heading("Title", text="Title",anchor=W)
        self.booklist.heading("Author", text="Author",anchor=W)
        self.booklist.heading("Book Genre", text="Book Genre",anchor=W)
        self.booklist.heading("Status", text="Status",anchor=W)
        self.booklist['show'] = 'headings'

        self.booklist.column("Book Number", width=100, anchor=W, stretch=False)
        self.booklist.column("ISBN", width=120, stretch=False)
        self.booklist.column("Title", width=380, stretch=False)
        self.booklist.column("Author", width=170, anchor=W, stretch=False)
        self.booklist.column("Book Genre", width=260, anchor=W, stretch=False)
        self.booklist.column("Status", width=80, anchor=W, stretch=False)
        
        self.booklist.bind("<Double-1>",OnDoubleClick2)
        
        self.booklist.place(x=200,y=180)
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:")
        self.lblsearchby.place(x=750,y=116)
        
        lblbooklist = tk.Label(self, font = ("Century Gothic",15), padx = 3 ,width =92, height = 1,text="List of All Books",anchor=W, bg="#375971", fg="snow")
        lblbooklist.place(x=200,y=151)
        
        self.txtSearch = Entry(self, font=("Poppins", 13), textvariable=Search, width=30)
        self.txtSearch.place(x=1000,y=120)

        self.btnSearchBy = ttk.Combobox(self, 
                                        state = "readonly", 
                                        font=('Century Gothic', 10), width=14, textvariable = Searchby)
        self.btnSearchBy['values'] = ("Book Number","ISBN", "Title", "Author", "Genre", "Status")
        self.btnSearchBy.place(x=858,y=120)
                
        #### Buttons

        self.add=PhotoImage(file="add.png", master=self)
        self.update=PhotoImage(file="update.png", master=self)
        self.delete=PhotoImage(file="delete.png", master=self)
        self.clear=PhotoImage(file="clear.png", master=self)
        self.show=PhotoImage(file="show.png", master=self)
        self.search=PhotoImage(file="search.png", master=self)
        self.updatestat=PhotoImage(file="updatestat.png", master=self)
        
        self.AddBook = Button(self, image=self.add,  bd=0 ,command=addBook)
        self.AddBook.place(x=320,y=108)
        self.AddBook.config(cursor= "hand2")
        
        self.btnUpdateBook = Button(self, image=self.update,  bd=0,command=updateBook)
        self.btnUpdateBook.place(x=425,y=108)
        self.btnUpdateBook.config(cursor= "hand2")
        
        self.btnUpdateStatus = Button(self, image=self.updatestat, bd=0,command=updateStatus)
        self.btnUpdateStatus.place(x=550,y=108)
        self.btnUpdateStatus.config(cursor= "hand2")
        
        self.btnShowall = Button(self,image=self.show, bd=0, command = showAll)
        self.btnShowall.place(x=200,y=108)
        self.btnShowall.config(cursor= "hand2")
        
        self.btnSearchBook = Button(self, image=self.search, bd=0,
                               command=searchBook)
        self.btnSearchBook.place(x=1270,y=116)
        self.btnSearchBook.config(cursor= "hand2")

        self.btnBN = Button(self, text="Book Number", font=('Poppins', 9), height=1, width=13, bd=0, 
                               bg="#90a3b0",command=sortBN)
        self.btnBN.place(x=200,y=180)
        self.btnBN.config(cursor= "hand2")

        self.btnISBN = Button(self, text="ISBN", font=('Poppins', 9), height=1, width=16, bd=0, 
                               bg="#90a3b0",command=sortISBN)
        self.btnISBN.place(x=298,y=180)
        self.btnISBN.config(cursor= "hand2")

        self.btnTitle = Button(self, text="Title", font=('Poppins', 9), height=1, width=54, bd=0, 
                               bg="#90a3b0",command=sortTitle)
        self.btnTitle.place(x=417,y=180)
        self.btnTitle.config(cursor= "hand2")

        self.btnAuthor = Button(self, text="Author", font=('Poppins', 9), height=1, width=23, bd=0, 
                               bg="#90a3b0",command=sortAuthor)
        self.btnAuthor.place(x=802,y=180)
        self.btnAuthor.config(cursor= "hand2")

        self.btnGenre = Button(self, text="Book Genre", font=('Poppins', 9), height=1, width=36, bd=0, 
                               bg="#90a3b0",command=sortGenre)
        self.btnGenre.place(x=970,y=180)
        self.btnGenre.config(cursor= "hand2")

        self.btnStatus = Button(self, text="Status", font=('Poppins', 9), height=1, width=11, bd=0, 
                               bg="#90a3b0",command=sortStatus)
        self.btnStatus.place(x=1229,y=180)
        self.btnStatus.config(cursor= "hand2")
             
        displayBook()

class Authors(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        label = tk.Label(self, text="Author", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        self.books1=PhotoImage(file="books1.png", master=self)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)
        
        Search = StringVar()
        title = StringVar()
        author = StringVar()
        genre = StringVar()
        booknum=StringVar()
        a1=StringVar()

        def addAuthor():
            def add():
                if booknum.get() == "" or a1.get() == "":
                    tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
                else:
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO authors VALUES(?,?)", (booknum.get(), a1.get()))
                    tkinter.messagebox.showinfo("Book Rental System","Author added successfully.")
                    conn.commit()
                    conn.close()
                    self.addWindow.destroy()

            self.addWindow = Toplevel(bg="#f5f5f5")
            self.addWindow.geometry("473x340")
            self.addWindow.resizable(0,0)
            self.addWindow.geometry("+{}+{}".format(positionRight+640, positionDown+260))

            uppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#375971")
            uppercolor.place(x=0,y=0)
            loweruppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#90a3b0")
            loweruppercolor.place(x=0,y=35)
            label = tk.Label(self.addWindow, text="AUTHOR", bg="#90a3b0", font=("Century Gothic", 17))
            label.place(x=10,y=37)

            self.BookNumber=Label(self.addWindow, text="Book Number:", font=("Poppins", 12, "bold"), padx=5, pady=5,bg="#f5f5f5" )
            self.BookNumber.place(x=10, y=100)
            self.BookNumEntry=Entry(self.addWindow, font=("Poppins", 12), textvariable=booknum, width=40)
            self.BookNumEntry.place(x=50, y=140)

            self.Author=Label(self.addWindow, text="Author:", font=("Poppins", 12, "bold"), padx=5, pady=5, bg="#f5f5f5")
            self.Author.place(x=10, y=180)
            self.Author1=Entry(self.addWindow, font=("Poppins", 12), textvariable=a1, width=40)
            self.Author1.place(x=50, y=220)

            self.add=PhotoImage(file="add.png", master=self.addWindow)
            self.clear=PhotoImage(file="clear.png", master=self.addWindow)
            self.exit=PhotoImage(file="exit.png", master=self.addWindow)

            self.btnclear = Button(self.addWindow, image = self.clear, bd=0,command=clear, bg="#f5f5f5")
            self.btnclear.place(x=50,y=270)
            self.btnclear.config(cursor= "hand2")

            self.btnadd = Button(self.addWindow, image = self.add, bd=0,command=add, bg="#f5f5f5")
            self.btnadd.place(x=200,y=270)
            self.btnadd.config(cursor= "hand2")

            self.btnexit = Button(self.addWindow, image = self.exit, bd=0,command=iExit, bg="#f5f5f5")
            self.btnexit.place(x=320,y=270)
            self.btnexit.config(cursor= "hand2")
            
        def delAuthor():
            def delete():
                if booknum.get() == "" or a1.get() == "":
                    tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
                else:
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    cur.execute("DELETE FROM authors WHERE BookNumber = ? AND Author = ?", (booknum.get(), a1.get()))
                    tkinter.messagebox.showinfo("Book Rental System","Author deleted successfully.")
                    conn.commit()
                    conn.close()
                    self.addWindow.destroy()

            self.addWindow = Toplevel(bg="#f5f5f5")
            self.addWindow.geometry("473x340")
            self.addWindow.resizable(0,0)
            self.addWindow.geometry("+{}+{}".format(positionRight+640, positionDown+260))

            uppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#375971")
            uppercolor.place(x=0,y=0)
            loweruppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#90a3b0")
            loweruppercolor.place(x=0,y=35)
            label = tk.Label(self.addWindow, text="AUTHOR", bg="#90a3b0", font=("Century Gothic", 17))
            label.place(x=10,y=37)

            self.BookNumber=Label(self.addWindow, text="Book Number:", font=("Poppins", 12, "bold"), padx=5, pady=5,bg="#f5f5f5" )
            self.BookNumber.place(x=10, y=100)
            self.BookNumEntry=Entry(self.addWindow, font=("Poppins", 12), textvariable=booknum, width=40)
            self.BookNumEntry.place(x=50, y=140)

            self.Author=Label(self.addWindow, text="Author:", font=("Poppins", 12, "bold"), padx=5, pady=5, bg="#f5f5f5")
            self.Author.place(x=10, y=180)
            self.Author1=Entry(self.addWindow, font=("Poppins", 12), textvariable=a1, width=40)
            self.Author1.place(x=50, y=220)

            self.delete=PhotoImage(file="delete.png", master=self.addWindow)
            self.clear=PhotoImage(file="clear.png", master=self.addWindow)
            self.exit=PhotoImage(file="exit.png", master=self.addWindow)

            self.btnclear = Button(self.addWindow, image = self.clear, bd=0,command=clear, bg="#f5f5f5")
            self.btnclear.place(x=50,y=270)
            self.btnclear.config(cursor= "hand2")

            self.btndelete = Button(self.addWindow, image = self.delete, bd=0,command=delete, bg="#f5f5f5")
            self.btndelete.place(x=180,y=270)
            self.btndelete.config(cursor= "hand2")

            self.btnexit = Button(self.addWindow, image = self.exit, bd=0,command=iExit, bg="#f5f5f5")
            self.btnexit.place(x=320,y=270)
            self.btnexit.config(cursor= "hand2")

            
        def displayAuthor():
            self.authorlist.delete(*self.authorlist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM authors")
            authors = cur.fetchall()
            list_of_authors = []
            for author in authors:
                if author[1] not in list_of_authors:
                    list_of_authors.append(author[1])   
            for row in list_of_authors:
                self.authorlist.insert("", tk.END, text=row[0], values=(row[::],))  
                
            conn.commit()    
            conn.close()
            
        def displayBooks():
            self.booklist.delete(*self.booklist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber;")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
                
        def showAll():
            displayAuthor()
            displayBooks()
        
        def searchAuthor():
            search = Search.get()                
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM authors")
            con.commit()
            self.authorlist.delete(*self.authorlist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if row[0].startswith(search):
                    self.authorlist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
            
        def OnDoubleClick(event):
            search = Search.get()
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber;")
            con.commit()
            self.booklist.delete(*self.booklist.get_children())
            item = self.authorlist.selection()[0]
            values = self.authorlist.item(item, "values")  
            
            search = values[0]
            
            books = cur.fetchall()
            for book in books:
                if book[4].count(search):
                    self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
            con.close()
            
        def OnDoubleClick2(event):
            item = self.booklist.selection()[0]
            values = self.booklist.item(item, "values")
            title.set(values[2])
            author.set(values[3])
            genre.set(values[4])

        def clear():
            booknum.set('')
            a1.set('')

        def iExit():
            self.addWindow.destroy()
            
        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()
        
        ## Window Buttons
        
        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")

        self.authorlist = ttk.Treeview(self,
                                        columns=("Author"),
                                        height = 22)
        
        self.authorlist.heading("Author", text="Author",anchor=W)
        self.authorlist['show'] = 'headings'

        self.authorlist.column("Author", width=300, anchor=W, stretch=False)
        
        self.authorlist.bind("<Double-1>",OnDoubleClick)
        
        self.authorlist.place(x=200,y=180)
        
        self.booklist = ttk.Treeview(self,
                                        columns=("Book Number","ISBN", "Title", "Author", "Book Genre","Status"),
                                        height = 10)

        self.booklist.heading("Book Number", text="Book Number", anchor=W)
        self.booklist.heading("ISBN", text="ISBN",anchor=W)
        self.booklist.heading("Title", text="Title",anchor=W)
        self.booklist.heading("Author", text="Author",anchor=W)
        self.booklist.heading("Book Genre", text="Book Genre",anchor=W)
        self.booklist.heading("Status", text="Status",anchor=W)
        self.booklist['show'] = 'headings'

        self.booklist.column("Book Number", width=90, anchor=W, stretch=False)
        self.booklist.column("ISBN", width=90, stretch=False)
        self.booklist.column("Title", width=230, stretch=False)
        self.booklist.column("Author", width=100, anchor=W, stretch=False)
        self.booklist.column("Book Genre", width=200, anchor=W, stretch=False)
        self.booklist.column("Status", width=80, anchor=W, stretch=False)
        
        self.booklist.bind("<Double-1>",OnDoubleClick2)
    
        self.booklist.place(x=530,y=180)
        
        
        lblorderlist = tk.Label(self, font = ("Century Gothic",15), padx=6,width = 24, height = 1,text="Author",anchor=W, bg="#375971", fg="snow")
        lblorderlist.place(x=200,y=151)
        
        lblbooklist = tk.Label(self, font = ("Century Gothic",15), padx = 5 ,width =65, height = 1,text="List of All Books",anchor=W, bg="#375971", fg="snow")
        lblbooklist.place(x=530,y=151)
        
        self.lbltitle = Label(self, font=("Poppins", 12, "bold"), text="Title:", padx=5, pady=5)
        self.lbltitle.place(x=530,y=420)
        self.txttitle = Entry(self, font=("Poppins", 13), textvariable=title, width=38, bd=0, bg ="gray94")
        self.txttitle.place(x=620,y=455)
        
        self.lblauthor = Label(self, font=("Poppins", 12, "bold"), text="Author/s:", padx=5, pady=5)
        self.lblauthor.place(x=530,y=480)
        self.txtauthor = Entry(self, font=("Poppins", 13), textvariable=author, width=38, bd=0, bg ="gray94")
        self.txtauthor.place(x=620,y=515)
        
        self.lblgenre = Label(self, font=("Poppins", 12, "bold"), text="Genre/s:", padx=5, pady=5)
        self.lblgenre.place(x=530,y=540)
        self.txtgenre = Entry(self, font=("Poppins", 13), textvariable=genre, width=78, bd=0, bg ="gray94")
        self.txtgenre.place(x=620,y=575)

        self.show=PhotoImage(file="show.png", master=self)
        self.addauthor=PhotoImage(file="add.png", master=self)
        self.delauthor=PhotoImage(file="delete.png", master=self)
        
        self.btnShowall = Button(self, image = self.show, bd=0,command=showAll)
        self.btnShowall.place(x=200,y=110)
        self.btnShowall.config(cursor= "hand2")

        self.btnadd = Button(self, image = self.addauthor, bd=0,command=addAuthor)
        self.btnadd.place(x=350,y=110)
        self.btnadd.config(cursor= "hand2")
        
        self.btndelete = Button(self, image = self.delauthor, bd=0,command=delAuthor)
        self.btndelete.place(x=450,y=110)
        self.btndelete.config(cursor= "hand2")
     
        displayAuthor()
        displayBooks()

class Genres(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        self.books1=PhotoImage(file="books1.png", master=self)
        
        label = tk.Label(self, text="Genres", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)
        
        Search = StringVar()
        title = StringVar()
        author = StringVar()
        genre = StringVar()
        booknum=StringVar()
        g1=StringVar()

        def addGenre():
            def add():
                if booknum.get() == "" or g1.get() == "":
                    tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
                else:
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO genres VALUES(?,?)", (booknum.get(), g1.get()))
                    tkinter.messagebox.showinfo("Book Rental System","Genre added successfully.")
                    conn.commit()
                    conn.close()
                    self.addWindow.destroy()

            self.addWindow = Toplevel(bg="#f5f5f5")
            self.addWindow.geometry("473x340")
            self.addWindow.resizable(0,0)
            self.addWindow.geometry("+{}+{}".format(positionRight+660, positionDown+260))

            uppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#375971")
            uppercolor.place(x=0,y=0)
            loweruppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#90a3b0")
            loweruppercolor.place(x=0,y=35)
            label = tk.Label(self.addWindow, text="GENRE", bg="#90a3b0", font=("Century Gothic", 17))
            label.place(x=10,y=37)

            self.BookNumber=Label(self.addWindow, text="Book Number:", font=("Poppins", 12, "bold"), padx=5, pady=5,bg="#f5f5f5" )
            self.BookNumber.place(x=10, y=100)
            self.BookNumEntry=Entry(self.addWindow, font=("Poppins", 12), textvariable=booknum, width=40)
            self.BookNumEntry.place(x=50, y=140)

            self.Genre=Label(self.addWindow, text="Genre:", font=("Poppins", 12, "bold"), padx=5, pady=5, bg="#f5f5f5")
            self.Genre.place(x=10, y=180)
            self.Genre1=Entry(self.addWindow, font=("Poppins", 12), textvariable=g1, width=40)
            self.Genre1.place(x=50, y=220)

            self.add=PhotoImage(file="add.png", master=self.addWindow)
            self.clear=PhotoImage(file="clear.png", master=self.addWindow)
            self.exit=PhotoImage(file="exit.png", master=self.addWindow)

            self.btnclear = Button(self.addWindow, image = self.clear, bd=0,command=clear, bg="#f5f5f5")
            self.btnclear.place(x=50,y=270)
            self.btnclear.config(cursor= "hand2")

            self.btnadd = Button(self.addWindow, image = self.add, bd=0,command=add, bg="#f5f5f5")
            self.btnadd.place(x=200,y=270)
            self.btnadd.config(cursor= "hand2")

            self.btnexit = Button(self.addWindow, image = self.exit, bd=0,command=iExit, bg="#f5f5f5")
            self.btnexit.place(x=350,y=270)
            self.btnexit.config(cursor= "hand2")

        def delGenre():
            def delete():
                if booknum.get() == "" or g1.get() == "":
                    tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
                else:
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    cur.execute("DELETE FROM genres WHERE BookNumber = ? AND Genre = ?", (booknum.get(), g1.get()))
                    tkinter.messagebox.showinfo("Book Rental System","Genre deleted successfully.")
                    conn.commit()
                    conn.close()
                    self.addWindow.destroy()

            self.addWindow = Toplevel(bg="#f5f5f5")
            self.addWindow.geometry("473x340")
            self.addWindow.resizable(0,0)
            self.addWindow.geometry("+{}+{}".format(positionRight+640, positionDown+260))

            uppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#375971")
            uppercolor.place(x=0,y=0)
            loweruppercolor = tk.Label(self.addWindow,height = 2,width = 1500, bg="#90a3b0")
            loweruppercolor.place(x=0,y=35)
            label = tk.Label(self.addWindow, text="AUTHOR", bg="#90a3b0", font=("Century Gothic", 17))
            label.place(x=10,y=37)

            self.BookNumber=Label(self.addWindow, text="Book Number:", font=("Poppins", 12, "bold"), padx=5, pady=5,bg="#f5f5f5" )
            self.BookNumber.place(x=10, y=100)
            self.BookNumEntry=Entry(self.addWindow, font=("Poppins", 12), textvariable=booknum, width=40)
            self.BookNumEntry.place(x=50, y=140)

            self.Genre=Label(self.addWindow, text="Genre:", font=("Poppins", 12, "bold"), padx=5, pady=5, bg="#f5f5f5")
            self.Genre.place(x=10, y=180)
            self.Genre1=Entry(self.addWindow, font=("Poppins", 12), textvariable=g1, width=40)
            self.Genre1.place(x=50, y=220)

            self.delete=PhotoImage(file="delete.png", master=self.addWindow)
            self.clear=PhotoImage(file="clear.png", master=self.addWindow)
            self.exit=PhotoImage(file="exit.png", master=self.addWindow)

            self.btnclear = Button(self.addWindow, image = self.clear, bd=0,command=clear, bg="#f5f5f5")
            self.btnclear.place(x=50,y=270)
            self.btnclear.config(cursor= "hand2")

            self.btndelete = Button(self.addWindow, image = self.delete, bd=0,command=delete, bg="#f5f5f5")
            self.btndelete.place(x=180,y=270)
            self.btndelete.config(cursor= "hand2")

            self.btnexit = Button(self.addWindow, image = self.exit, bd=0,command=iExit, bg="#f5f5f5")
            self.btnexit.place(x=320,y=270)
            self.btnexit.config(cursor= "hand2")
    
        def displayGenre():
            self.genrelist.delete(*self.genrelist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur1 = conn.cursor()
            cur.execute("SELECT * FROM genres")
            genres = cur.fetchall()
            list_of_genres = []
            for genre in genres:
                if genre[1] not in list_of_genres:
                    list_of_genres.append(genre[1])      
            for row in list_of_genres:
                self.genrelist.insert("", tk.END, text=row[0], values=(row[::],))
                
            conn.commit()    
            conn.close()
        
        def displayBooks():
            self.booklist.delete(*self.booklist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber;")
            books = cur.fetchall()
            for book in books:
                self.booklist.insert("", tk.END, text=book[0], values=(book[0],book[1],book[2],book[4],book[5],book[3]))
                
        def showAll():
            displayGenre()
            displayBooks()

        def deleteGenre():
            try:
                messageDelete = tkinter.messagebox.askyesno("Book Rental System", "Do you want to delete this genre?")
                if messageDelete > 0:  
                    con = sqlite3.connect("BRS.db")
                    cur = con.cursor()
                    x = self.genrelist.selection()[0]
                    id_no = self.genrelist.item(x)["values"][0]
                    cur.execute("DELETE FROM genres WHERE Genre = ?",(id_no,))  
                    con.commit()
                    self.genrelist.delete(x)
                    tkinter.messagebox.showinfo("Book Rental System", "Genre deleted")
                    displayGenre()
                    con.close()                   
            except:
                tkinter.messagebox.showerror("Book Rental System", "There are books that are still in this Genre")
        
        def searchGenre():
            search = Search.get()                
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM genres")
            con.commit()
            self.genrelist.delete(*self.genrelist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if row[0].startswith(search):
                    self.genrelist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
            
        def OnDoubleClick(event):
            search = Search.get()
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber;")
            con.commit()
            self.booklist.delete(*self.booklist.get_children())
            rows = cur.fetchall()   
            item = self.genrelist.selection()[0]
            values = self.genrelist.item(item, "values")  
            
            search = values[0]
            for row in rows:
                if row[5].count(search):
                    self.booklist.insert("", tk.END, text=row[0], values=(row[0],row[1],row[2],row[4],row[5],row[3]))
            con.close()
            
        def OnDoubleClick2(event):
            item = self.booklist.selection()[0]
            values = self.booklist.item(item, "values")
            title.set(values[2])
            author.set(values[3])
            genre.set(values[4])

        def clear():
            booknum.set('')
            g1.set('')

        def iExit():
            self.addWindow.destroy()
            
        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()
        
        ## Window Buttons
        
        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")

        self.genrelist = ttk.Treeview(self,columns=("Genre"),
                                        height = 22)
        
        self.genrelist.heading("Genre", text="Genre",anchor=W)
        self.genrelist['show'] = 'headings'

        self.genrelist.column("Genre", width=300, anchor=W, stretch=False)
        
        self.genrelist.bind("<Double-1>",OnDoubleClick)
        
        self.genrelist.place(x=200,y=180)
        
        self.booklist = ttk.Treeview(self, columns=("Book Number","ISBN", "Title", "Author", "Book Genre","Status"),
                                        height = 10)

        self.booklist.heading("Book Number", text="Book Number", anchor=W)
        self.booklist.heading("ISBN", text="ISBN",anchor=W)
        self.booklist.heading("Title", text="Title",anchor=W)
        self.booklist.heading("Author", text="Author",anchor=W)
        self.booklist.heading("Book Genre", text="Book Genre",anchor=W)
        self.booklist.heading("Status", text="Status",anchor=W)
        self.booklist['show'] = 'headings'

        self.booklist.column("Book Number", width=90, anchor=W, stretch=False)
        self.booklist.column("ISBN", width=90, stretch=False)
        self.booklist.column("Title", width=230, stretch=False)
        self.booklist.column("Author", width=100, anchor=W, stretch=False)
        self.booklist.column("Book Genre", width=200, anchor=W, stretch=False)
        self.booklist.column("Status", width=80, anchor=W, stretch=False)
        
        self.booklist.bind("<Double-1>",OnDoubleClick2)
    
        self.booklist.place(x=530,y=180)
        
        lblorderlist = tk.Label(self, font = ("Century Gothic",15), padx=6,width = 24, height = 1,text="Genres",anchor=W, bg="#375971", fg="snow")
        lblorderlist.place(x=200,y=151)
        
        lblbooklist = tk.Label(self, font = ("Century Gothic",15), padx = 5 ,width =65, height = 1,text="List of All Books",anchor=W, bg="#375971", fg="snow")
        lblbooklist.place(x=530,y=151)
        
        self.lbltitle = Label(self, font=("Poppins", 12, "bold"), text="Title:", padx=5, pady=5)
        self.lbltitle.place(x=530,y=420)
        self.txttitle = Entry(self, font=("Poppins", 13), textvariable=title, width=38, bd=0, bg ="gray94")
        self.txttitle.place(x=620,y=455)
        
        self.lblauthor = Label(self, font=("Poppins", 12, "bold"), text="Author/s:", padx=5, pady=5)
        self.lblauthor.place(x=530,y=480)
        self.txtauthor = Entry(self, font=("Poppins", 13), textvariable=author, width=38, bd=0, bg ="gray94")
        self.txtauthor.place(x=620,y=515)
        
        self.lblgenre = Label(self, font=("Poppins", 12, "bold"), text="Genre/s:", padx=5, pady=5)
        self.lblgenre.place(x=530,y=540)
        self.txtgenre = Entry(self, font=("Poppins", 13), textvariable=genre, width=78, bd=0, bg ="gray94")
        self.txtgenre.place(x=620,y=575)
        
        self.show=PhotoImage(file="show.png", master=self)
        self.deletegenre=PhotoImage(file="delete.png", master=self)
        self.addgenre=PhotoImage(file="add.png", master=self)
        
        self.btnShowall = Button(self, image = self.show, bd=0,command=showAll)
        self.btnShowall.place(x=200,y=110)
        self.btnShowall.config(cursor= "hand2")

        self.btnadd = Button(self, image = self.addgenre, bd=0,command=addGenre)
        self.btnadd.place(x=350,y=110)
        self.btnadd.config(cursor= "hand2")
        
        self.btndelete = Button(self, image = self.deletegenre, bd=0,command=delGenre)
        self.btndelete.place(x=450,y=110)
        self.btndelete.config(cursor= "hand2")
        
        displayGenre()
        displayBooks()

class Borrowers(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        
        label = tk.Label(self, text="Borrower", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        self.books1=PhotoImage(file="books1.png", master=self)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)
        
        BorrowerIDNum = StringVar()
        ValidID = StringVar()
        Name = StringVar()
        EmailAdd = StringVar()
        PhoneNum = StringVar()
        Search = StringVar()
        SearchBy = StringVar()
        SearchAvail = StringVar()
        Showby = StringVar()
        Status = StringVar()

        ##Functions
        def addBorrower():
            if BorrowerIDNum.get() == "" or ValidID.get() == "" or Name.get() == "" or EmailAdd.get() == "" or PhoneNum.get() == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                conn = sqlite3.connect("BRS.db")
                c = conn.cursor()
                c2 = conn.cursor()
                c2.execute("SELECT * FROM borrower")
                borrowers = c2.fetchall()
                list_of_valid_ids = []
                for borrower in borrowers:
                    list_of_valid_ids.append(borrower[1])
                    
                if ValidID.get() not in list_of_valid_ids:
                    try:      
                        c.execute("INSERT INTO borrower(BorrowerIDNum, ValidID, Name, EmailAdd, PhoneNum) VALUES (?,?,?,?,?)",\
                                  (BorrowerIDNum.get(),ValidID.get(),Name.get(),EmailAdd.get(), PhoneNum.get()))
                        conn.commit()           
                        conn.close()
                        clear()
                        tkinter.messagebox.showinfo("Book Rental System", "Borrower has been recorded")
                        displayBorrower()
                    except:
                        tkinter.messagebox.showerror("Book Rental System", "Borrower already recorded")
                else:
                    tkinter.messagebox.showerror("Book Rental System", "Valid ID already recorded")
                
        def displayBorrower():
            self.borrower.delete(*self.borrower.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM borrower")
            rows = cur.fetchall()
            for row in rows:
                self.borrower.insert("", tk.END, text=row[0], values=row[0:])
            conn.close()
            
        def showAll():
            displayBorrower()

        def clear():
            BorrowerIDNum.set('')
            ValidID.set('')
            Name.set('')
            EmailAdd.set('')
            PhoneNum.set('')
            
        def updateBorrower():
            if BorrowerIDNum.get() == "" or ValidID.get() == "" or Name.get() == "" or EmailAdd.get() == "" or PhoneNum.get() == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                for selected in self.borrower.selection():
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    #cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("UPDATE borrower SET BorrowerIDNum = ?,ValidID = ?, Name = ?, EmailAdd = ? ,PhoneNum = ? WHERE BorrowerIDNum=?", \
                                (BorrowerIDNum.get(),ValidID.get(),Name.get(),EmailAdd.get(),PhoneNum.get(), self.borrower.set(selected, '#1')))   
                    conn.commit()
                    tkinter.messagebox.showinfo("Books Rental System", "Book Updated Successfully")
                    displayBorrower()
                    clear()
                    conn.close()
                 
        def OnDoubleClick(event):
            item = self.borrower.selection()[0]
            values = self.borrower.item(item, "values")  
            BorrowerIDNum.set(values[0])
            ValidID.set(values[1])
            Name.set(values[2])
            EmailAdd.set(values[3])
            PhoneNum.set(values[4])

        def deleteBorrower():   
            messageDelete = tkinter.messagebox.askyesno("Book Rental System", "Do you want to remove this book?")
            if messageDelete > 0:   
                con = sqlite3.connect("BRS.db")
                cur = con.cursor()
                x = self.borrower.selection()[0]
                id_no = self.borrower.item(x)["values"][0]
                #cur.execute("PRAGMA foreign_keys = ON")
                cur.execute("DELETE FROM borrower WHERE BorrowerIDNum = ?",(id_no,))                    
                con.commit()
                self.borrower.delete(x)
                tkinter.messagebox.showinfo("Book Rental System", "Borrower has been deleted")
                displayBorrower()
                clear()
                con.close()
                
        def searchBorrower():
            search = Search.get() 
            searchby = SearchBy.get()              
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM borrower")
            con.commit()
            self.borrower.delete(*self.borrower.get_children())
            rows = cur.fetchall()
            for row in rows:
                if searchby == "Borrower's ID":
                    if row[0].count(search):
                        self.borrower.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "Valid ID":
                    if row[1].count(search):
                        self.borrower.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Name':
                    if row[2].startswith(search):
                        self.borrower.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "Email Add":
                    if row[3].count(search):
                        self.borrower.insert("", tk.END, text=row[0], values=row[0:])
                else:
                    if row[4].count(search):
                        self.borrower.insert("", tk.END, text=row[0], values=row[0:])
            con.close()

        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()

        ## Window Buttons
        
        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")
         
        booklist = tk.Label(self,height = 2,width = 108, bg="#89E894")
        
        self.borrower = ttk.Treeview(self,
                                        columns=("Borrower's ID","Valid ID", "Name", "Email Add", "Phone Number"),
                                        height = 13)

        self.borrower.heading("Borrower's ID", text="Borrower's ID", anchor=W)
        self.borrower.heading("Valid ID", text="Valid ID",anchor=W)
        self.borrower.heading("Name", text="Name",anchor=W)
        self.borrower.heading("Email Add", text="Email Add",anchor=W)
        self.borrower.heading("Phone Number", text="Phone Number",anchor=W)
        self.borrower['show'] = 'headings'

        self.borrower.column("Borrower's ID", width=200, anchor=W, stretch=False)
        self.borrower.column("Valid ID", width=150, stretch=False)
        self.borrower.column("Name", width=380, stretch=False)
        self.borrower.column("Email Add", width=200, anchor=W, stretch=False)
        self.borrower.column("Phone Number", width=180, anchor=W, stretch=False)
        
        
        self.borrower.bind("<Double-1>",OnDoubleClick)
        
        self.borrower.place(x=200,y=180)
        
        lblborrower = tk.Label(self, font = ("Century Gothic",15), padx = 3 ,width =92, height = 1,text="List of Borrowers",anchor=W, bg="#375971", fg="snow")
        lblborrower.place(x=200,y=151)
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:")
        self.lblsearchby.place(x=660,y=119)
        
        self.lblBBID = Label(self, font=("Poppins", 12, "bold"), text="Borrower ID Num:", padx=5, pady=5)
        self.lblBBID.place(x=200,y=475)
        self.txtBBID = Entry(self, font=("Poppins", 13), textvariable=BorrowerIDNum, width=38)
        self.txtBBID.place(x=360,y=480)
        
        self.lblName = Label(self, font=("Poppins", 12, "bold"), text="Name:", padx=5, pady=5)
        self.lblName.place(x=200,y=515)
        self.txtName = Entry(self, font=("Poppins", 13), textvariable=Name, width=38)
        self.txtName.place(x=360,y=520)
        
        self.lblVID = Label(self, font=("Poppins", 12, "bold"), text="Valid ID", padx=5, pady=5)
        self.lblVID.place(x=200,y=555)
        self.txtVID = Entry(self, font=("Poppins", 13), textvariable=ValidID, width=38)
        self.txtVID.place(x=360,y=560)
        
        self.lblEMA = Label(self, font=("Poppins", 12, "bold"), text="Email Add", padx=5, pady=5)
        self.lblEMA.place(x=200,y=595)
        self.txtEMA = Entry(self, font=("Poppins", 13), textvariable=EmailAdd, width=38)
        self.txtEMA.place(x=360,y=600)
        
        self.lblPN = Label(self, font=("Poppins", 12, "bold"), text="Phone Number", padx=5, pady=5)
        self.lblPN.place(x=750,y=475)
        self.txtPN= Entry(self, font=("Poppins", 13), textvariable=PhoneNum, width=38)
        self.txtPN.place(x=890,y=480)
        
        self.txtSearch = Entry(self, font=("Poppins", 13), textvariable=Search,relief=FLAT, width=40)
        self.txtSearch.place(x=900,y=120)
        
        #### Buttons 
        
        self.add=PhotoImage(file="add.png", master=self)
        self.update=PhotoImage(file="update.png", master=self)
        self.delete=PhotoImage(file="delete.png", master=self)
        self.clear=PhotoImage(file="clear.png", master=self)
        self.show=PhotoImage(file="show.png", master=self)
        self.search=PhotoImage(file="search.png", master=self)

        self.btnCLear = Button(self, image=self.clear, bd=0, command=clear)
        self.btnCLear.place(x=205,y=640)
        self.btnCLear.config(cursor= "hand2")
        
        self.btnAddBook = Button(self, image=self.add,  bd=0,  command=addBorrower)
        self.btnAddBook.place(x=320,y=640)
        self.btnAddBook.config(cursor= "hand2")
        
        self.btnUpdateBook = Button(self, image=self.update,  bd=0, command=updateBorrower)
        self.btnUpdateBook.place(x=425,y=640)
        self.btnUpdateBook.config(cursor= "hand2")
        
        self.btnDeleteBook = Button(self,image = self.delete, bd =0, command=deleteBorrower)
        self.btnDeleteBook.place(x=550,y=640)
        self.btnDeleteBook.config(cursor= "hand2")
        
        self.btnShowallOrder = Button(self,image=self.show, bd=0, command = showAll)
        self.btnShowallOrder.place(x=200,y=108)
        self.btnShowallOrder.config(cursor= "hand2")
        
        self.btnSearchBook = Button(self, image=self.search, bd=0,
                               command=searchBorrower)
        self.btnSearchBook.place(x=1270,y=116)
        self.btnSearchBook.config(cursor= "hand2")

        self.btnSearchBy = ttk.Combobox(self, 
                                        state = "readonly", 
                                        font=('Century Gothic', 10), width=14, textvariable = SearchBy)
        self.btnSearchBy['values'] = ("Borrower's ID","Valid ID", "Name", "Email Add", "Phone Number")
        self.btnSearchBy.place(x=778,y=120)
        

        displayBorrower()
               
class Order(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        self.books1=PhotoImage(file="books1.png", master=self)
        
        label = tk.Label(self, text="Rent", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)
        
        RentOrderNo = StringVar()
        BookNumber = StringVar()
        BorrowersID = StringVar()
        DateBorrowed = StringVar()
        DueDate = StringVar()
        ReturnDate = StringVar()
        Search = StringVar()
        SearchBy = StringVar()
                    
       
        def addOrder():
            if  BookNumber.get() == "" or BorrowersID.get() == "" or  DueDate.get() == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                date = DueDate.get()
                a = date.split("/") 
                m = ""
                d = ""
                y = ""
                if len(a[0]) == 1:
                    m = "0" + str(a[0]) 
                else:
                    m = a[0]
                    
                if len(a[1]) == 1:
                    d = "0" + str(a[1]) 
                else:
                    d = a[1]
                    
                if len(a[2]) == 2:
                    y = "20" + str(a[2]) 
                else:
                    y = a[2] 
                
                dates = m+"/"+d+"/"+y
                
                conn = sqlite3.connect("BRS.db")
                c = conn.cursor()
                cur = conn.cursor()
                cur1 = conn.cursor()    
                cur2 = conn.cursor() 
                cur.execute("SELECT books.*, GROUP_CONCAT(authors.Author,'|'), GROUP_CONCAT(genres.Genre, '|') FROM books\
                            INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                            INNER JOIN genres ON authors.BookNumber = genres.BookNumber\
                            GROUP BY authors.Author, genres.Genre;")
                cur2.execute("SELECT * FROM borrower")
                books = cur.fetchall()
                for book in books:
                    if book[0] == BookNumber.get() and book[5] != 'Unavailable':
                        try:
                            c.execute("PRAGMA foreign_keys = ON")
                            cur1.execute("PRAGMA foreign_keys = ON")
                            c.execute("INSERT INTO rent (BookNumber, BorrowersID, DateBorrowed, DueDate) VALUES (?,?,strftime('%m/%d/%Y'),?)",\
                                         (BookNumber.get(),BorrowersID.get(),dates))
                            cur1.execute("INSERT INTO history(BookNumber, BorrowersID, DateBorrowed, DueDate, ReturnDate) VALUES (?,?,strftime('%m/%d/%Y'),?,?)",\
                                         (BookNumber.get(),BorrowersID.get(),dates,ReturnDate.get())) 
                            cur.execute("UPDATE books SET BookNumber = ?, ISBN = ?, Title = ?, Status = 'Unavailable' WHERE BookNumber = ?",
                                     (book[0],book[1],book[2],book[0]))
                            conn.commit() 
                            clear()
                            tkinter.messagebox.showinfo("Book Rental System", "Order added to database")
                            displayOrder()
                        except:
                            tkinter.messagebox.showerror("Book Rental System", "Borrwer's ID not exist")
                            
                    elif book[0] == BookNumber.get() and book[5] == 'Unavailable':
                        tkinter.messagebox.showerror("Book Rental System", "Book Unavailable")   
                        pass
                    else:
                        pass
                          
                conn.close()
                    
        def displayOrder():
            self.orderlist.delete(*self.orderlist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM rent")
            rows = cur.fetchall()
            for row in rows:
                self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
            conn.close()
        
        def updateOrder():
            if  BookNumber.get() == "" or BorrowersID.get() == "" or DueDate == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                date = DueDate.get()
                a = date.split("/") 
                m = ""
                d = ""
                y = ""
                if len(a[0]) == 1:
                    m = "0" + str(a[0]) 
                else:
                    m = a[0]
                    
                if len(a[1]) == 1:
                    d = "0" + str(a[1]) 
                else:
                    d = a[1]
                    
                if len(a[2]) == 2:
                    y = "20" + str(a[2]) 
                else:
                    y = a[2] 
                
                dates = m+"/"+d+"/"+y
                conn = sqlite3.connect("BRS.db")
                c = conn.cursor()
                cur = conn.cursor()
                cur1 = conn.cursor()
                cur2 = conn.cursor()
                cur1.execute("SELECT books.*, GROUP_CONCAT(rent.BookNumber,'|') FROM books\
                             INNER JOIN rent ON books.BookNumber = rent.BookNumber \
                             GROUP BY rent.BookNumber;")
                cur2.execute("SELECT * FROM rent")
                books = cur1.fetchall()
                rents = cur2.fetchall()
                for selected in self.orderlist.selection():
                    cur.execute("PRAGMA foreign_keys = ON")
                    c.execute("UPDATE rent SET  BookNumber = ?, BorrowersID = ?,  DateBorrowed = ?, DueDate = ? WHERE RentOrderNo=?", \
                                (BookNumber.get(),BorrowersID.get(),DateBorrowed.get(),dates,  self.orderlist.set(selected, '#1'))) 
                    cur.execute("UPDATE history SET BookNumber = ?, BorrowersID = ?,  DateBorrowed = ?, DueDate = ?, ReturnDate = ? WHERE RentOrderNo=?",\
                                (BookNumber.get(),BorrowersID.get(),DateBorrowed.get(),dates,ReturnDate.get(), self.orderlist.set(selected, '#1')))                      
                    tkinter.messagebox.showinfo("Books Rental System", "Order Updated Successfully")
                    displayOrder()
                    clear()     
                
                conn.commit()
                                   
        def deleteOrder():   
            messageDelete = tkinter.messagebox.askyesno("Book Rental System", "Do you want to remove this transaction?")
            if messageDelete > 0:  
                con = sqlite3.connect("BRS.db")
                cur = con.cursor()
                cur2 = con.cursor()
                x = self.orderlist.selection()[0]
                id_no = self.orderlist.item(x)["values"][0]
                y = self.orderlist.selection()[0]
                bookn = self.orderlist.item(y)["values"][1]
                cur.execute("DELETE FROM rent WHERE RentOrderNo = ?",(id_no,))     
                cur2.execute("SELECT * FROM books")
                books = cur2.fetchall()
                
                for book in books:
                    if str(bookn) == str(book[0]):
                        cur2.execute("UPDATE books SET BookNumber = ?, ISBN = ?, Title = ?, Status = 'Available' WHERE BookNumber = ?",
                                     (BookNumber.get(),book[1],book[2]),BookNumber.get())  
                        cur.execute("INSERT INTO return (BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
                                     (bookn,book[1],book[2],book[3],book[4]))
                    else:
                        pass
                
                con.commit()
                self.orderlist.delete(x)
                tkinter.messagebox.showinfo("Book Rental System", "Transaction deleted from database")
                displayOrder()
                con.close()
                        
        def searchOrder():
            search = Search.get() 
            searchby = SearchBy.get()          
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM rent")
            con.commit()
            self.orderlist.delete(*self.orderlist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if searchby == 'Rent Order':
                    if str(row[0]).count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Book ID':
                    if row[1].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "Borrower's ID":
                    if row[2].startswith(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Date Borrowed':
                    if row[3].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                else:
                    if row[4].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
 
        def showAll():
            displayOrder()
        
        def clear():
            RentOrderNo.set('')
            BookNumber.set('')
            BorrowersID.set('')
            DateBorrowed.set('')
            DueDate.set('')
            ReturnDate.set('')
            
        def OnDoubleClick(event):
            item = self.orderlist.selection()[0]
            values = self.orderlist.item(item, "values")  
            RentOrderNo.set(values[0])
            BookNumber.set(values[1])
            BorrowersID.set(values[2])
            DateBorrowed.set(values[3])
            DueDate.set(values[4])

        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()
                
        con = sqlite3.connect("BRS.db")
        cur = con.cursor()
        cur1 = con.cursor()
        cur.execute("SELECT books.*, GROUP_CONCAT(authors.Author,'|'), GROUP_CONCAT(genres.Genre, '|') FROM books\
                    INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                    INNER JOIN genres ON authors.BookNumber = genres.BookNumber\
                    GROUP BY authors.Author, genres.Genre;")
        books = cur.fetchall()
        bookid = []
        for book in books:
            if book[3] == 'Available':
                if book[0] not in bookid:
                    bookid.append(book[0])

        cur1.execute("SELECT * FROM borrower")
        borrower=cur1.fetchall()
        bIDNum =[]
        for b in borrower:
            if b[0] not in bIDNum:
                bIDNum.append(b[0]) 
            
        
        ## Window Buttons
        
        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")

        self.orderlist = ttk.Treeview(self,
                                        columns=("Rent Order No.","Book ID","Borrower's ID", "Date Borrowed","Due Date"),
                                        height = 22)
        
        self.orderlist.heading("Rent Order No.", text="Rent Order No.",anchor=W)
        self.orderlist.heading("Book ID", text="Book ID",anchor=W) 
        self.orderlist.heading("Borrower's ID", text="Borrower's ID", anchor=W)
        self.orderlist.heading("Date Borrowed", text="Date Borrowed", anchor=W)
        self.orderlist.heading("Due Date", text="Due Date", anchor=W)
        self.orderlist['show'] = 'headings'

        self.orderlist.column("Rent Order No.", width=110, anchor=W, stretch=False)
        self.orderlist.column("Book ID", width=170, anchor=W, stretch=False)
        self.orderlist.column("Borrower's ID", width=170, stretch=False)
        self.orderlist.column("Date Borrowed", width=120, stretch=False)
        self.orderlist.column("Due Date", width=120, stretch=False)
        
        self.orderlist.bind("<Double-1>",OnDoubleClick)
        
        self.orderlist.place(x=600,y=180)

        lblorderlist = tk.Label(self, font = ("Century Gothic",15), padx=3,width = 57, height = 1,text="List of Rents",anchor=W, bg="#375971", fg="snow")
        lblorderlist.place(x=600,y=151)
        
        self.lblIDNumber = Label(self, font=("Poppins", 12, "bold"), text="Book Number:", padx=5, pady=5)
        self.lblIDNumber.place(x=200,y=200)

        self.txtIDNumber = ttk.Combobox(self,
                                        values = bookid,
                                        state="readonly", font=("Poppins", 13), textvariable=BookNumber,
                                        width=23)
        self.txtIDNumber.place(x=330,y=205)
        
        
        self.lblISBN = Label(self, font=("Poppins", 12, "bold"), text="Borrower's ID:", padx=5, pady=5)
        self.lblISBN.place(x=200,y=235)
        self.txtISBN = ttk.Combobox(self,
                                        values = bIDNum,
                                        state="readonly", font=("Poppins", 13), textvariable=BorrowersID,
                                        width=23)
        self.txtISBN.place(x=330,y=240)
        
        self.lblDueDate = Label(self, font=("Poppins", 12, "bold"), text="Due Date:", padx=5, pady=5)
        self.lblDueDate.place(x=200,y=270)
        self.txtDueDate = DateEntry(self, font=("Poppins", 13), textvariable=DueDate, width=23, year=2021, month=7, day=21, foreground ="black",\
                       background = "#78a2cc", headersbackground = "#a4c3d2" , normalbackground = "white", weekendbackground="white",\
                       othermonthbackground="white", othermonthwebackground='white')
        self.txtDueDate.place(x=330,y=275)
             
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:", )
        self.lblsearchby.place(x=760,y=119)
        
        self.txtSearch = Entry(self, font=("Poppins", 13),  textvariable=Search,relief=FLAT, width=30)
        self.txtSearch.place(x=998,y=120)
        
        self.add=PhotoImage(file="add.png", master=self)
        self.update=PhotoImage(file="update.png", master=self)
        self.delete=PhotoImage(file="delete.png", master=self)
        self.clear=PhotoImage(file="clear.png", master=self)
        self.show=PhotoImage(file="show.png", master=self)
        self.search=PhotoImage(file="search.png", master=self)

        self.btnclear = Button(self,image=self.clear, bd=0, command = clear)
        self.btnclear.place(x=190,y=450)
        self.btnclear.config(cursor= "hand2")
        
        self.btnAddOrder = Button(self, image=self.add, bd=0, command = addOrder)
        self.btnAddOrder.place(x=310,y=450)
        self.btnAddOrder.config(cursor= "hand2")
        
        self.btnUpdateOrder = Button(self, image=self.update, bd=0, command = updateOrder)
        self.btnUpdateOrder.place(x=410,y=450)
        self.btnUpdateOrder.config(cursor= "hand2")
        
        #self.btnRemoveOrder = Button(self, text="➖  REMOVE ORDER", font=('Poppins', 11), height=1, width=17, bd=1, 
                               #bg="#90a3b0", command = deleteOrder)
        #self.btnRemoveOrder.place(x=380,y=500)
        #self.btnRemoveOrder.config(cursor= "hand2")
        
        self.btnSearchBy = ttk.Combobox(self, 
                                        state = "readonly", 
                                        font=('Century Gothic', 10), width=14, textvariable = SearchBy)
        self.btnSearchBy['values'] = ('Rent Order','Book ID',"Borrower's ID", 'Date Borrowed','Due Date')
        self.btnSearchBy.place(x=876,y=120)
        
        self.btnSearchBook = Button(self, image=self.search, bd=0,
                               command=searchOrder)
        self.btnSearchBook.place(x=1270,y=118)
        self.btnSearchBook.config(cursor= "hand2")
        
        
        self.btnShowallBook = Button(self, image=self.show, bd=0,command=showAll)
        self.btnShowallBook.place(x=600,y=108)
        self.btnShowallBook.config(cursor= "hand2")
                   
        displayOrder()
               
class Report(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        
        self.books1=PhotoImage(file="books1.png", master=self)
        
        label = tk.Label(self, text="Report", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)

        row = StringVar()
        BIDNum = StringVar()
        Name = StringVar()
        BNumber = StringVar()
        Search = StringVar()
        BDate = StringVar()
        DDate = StringVar()
        RDate = StringVar()
        SearchBy = StringVar()
        
        con = sqlite3.connect("BRS.db")
        cur = con.cursor()
        cur.execute("SELECT books.*, GROUP_CONCAT(authors.Author,'|'), GROUP_CONCAT(genres.Genre, '|') FROM books\
                    INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                    INNER JOIN genres ON authors.BookNumber = genres.BookNumber\
                    GROUP BY authors.Author, genres.Genre;")
        bookid = []
        books = cur.fetchall()
        for book in books:
            if book[3] == 'Unavailable':
                if book[0] not in bookid:
                    bookid.append(book[0])
            
        
        def addReport():
            if BNumber.get() == "" or RDate.get() == "":
                    tkinter.messagebox.showerror("Book Rental System", "Please fill in the box")
            else: 
                date = RDate.get()
                a = date.split("/") 
                m = ""
                d = ""
                y = ""
                if len(a[0]) == 1:
                    m = "0" + str(a[0]) 
                else:
                    m = a[0]
                    
                if len(a[1]) == 1:
                    d = "0" + str(a[1]) 
                else:
                    d = a[1]
                    
                if len(a[2]) == 2:
                    y = "20" + str(a[2]) 
                else:
                    y = a[2] 
                
                dates = m+"/"+d+"/"+y
                conn = sqlite3.connect("BRS.db")
                cur = conn.cursor()
                cur2 = conn.cursor()
                cur3 = conn.cursor()
                cur4 = conn.cursor()
                cur.execute("SELECT * FROM borrower")
                cur2.execute("SELECT books.*, GROUP_CONCAT(DISTINCT (authors.Author)), GROUP_CONCAT(DISTINCT (genres.Genre)) FROM books\
                        INNER JOIN authors ON books.BookNumber = authors.BookNumber \
                        INNER JOIN genres ON authors.BookNumber = genres.BookNumber \
                        GROUP BY books.BookNumber;")
                cur3.execute("SELECT * FROM rent")
                borname = cur.fetchall()
                books = cur2.fetchall()
                rents = cur3.fetchall()
                Name = ""
                for rent in rents:
                    for borrower in borname:
                        if BNumber.get() == rent[1]:
                            try:
                                cur.execute("PRAGMA foreign_keys = ON")
                                if rent[2] == borrower[0]:
                                    Name = borrower[2]
                                    cur.execute("DELETE FROM rent WHERE RentOrderNo = ?",(rent[0],))   
                                    cur.execute("INSERT INTO report (BIDNum, Name, BookNumber, DateBorrowed, DueDate, ReturnDate) VALUES (?,?,?,?,?,?)",\
                                               (rent[2], Name,BNumber.get(), rent[3], rent[4],dates))
                                    for book in books:
                                        if str(BNumber.get()) == str(book[0]):
                                            cur2.execute("UPDATE books SET BookNumber = ?, ISBN = ?, Title = ?, Status = 'Available' WHERE BookNumber = ?",
                                                         (BNumber.get(),book[1],book[2],BNumber.get()))  
                                            cur4.execute("INSERT INTO return (BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
                                                         (BNumber.get(),book[1],book[2],book[3],book[4]))
                                        else:
                                            pass
                                    
                                    conn.commit()           
                                    conn.close()
                                    clear()
                                    tkinter.messagebox.showinfo("Book Rental System", "Added to Report")
                                    displayReport()
                            except:
                                tkinter.messagebox.showerror("Book Rental System", "Book ID or Borrower's ID does not exists")
                    
        def displayReport():
            self.orderlist.delete(*self.orderlist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM report")
            rows = cur.fetchall()
            for row in rows:
                self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
            conn.close()
        
        def updateReport():
            if BNumber.get() == "" or RDate.get() == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                date = RDate.get()
                a = date.split("/") 
                m = ""
                d = ""
                y = ""
                if len(a[0]) == 1:
                    m = "0" + str(a[0]) 
                else:
                    m = a[0]
                    
                if len(a[1]) == 1:
                    d = "0" + str(a[1]) 
                else:
                    d = a[1]
                    
                if len(a[2]) == 2:
                    y = "20" + str(a[2]) 
                else:
                    y = a[2] 
                
                dates = m+"/"+d+"/"+y
                conn = sqlite3.connect("BRS.db")
                cur = conn.cursor()
                cur2 = conn.cursor()
                cur2.execute("SELECT * from report")
                reports = cur2.fetchall()
                for report in reports:
                    if str(row.get()) == str(report[0]):
                        if str(BNumber.get()) == str(report[3]):
                            try:
                                cur.execute("PRAGMA foreign_keys = ON")
                                for selected in self.orderlist.selection():
                                    cur.execute("UPDATE report SET BIDNum = ?, Name = ?, BookNumber = ?, DateBorrowed = ?, DueDate = ?, ReturnDate = ? WHERE ReportOrderNo = ?", \
                                                (self.orderlist.set(selected, '#2'), 
                                                 self.orderlist.set(selected, '#3'),
                                                 BNumber.get(), 
                                                 self.orderlist.set(selected, '#5'), 
                                                 self.orderlist.set(selected, '#6'),
                                                 dates, 
                                                 self.orderlist.set(selected, '#1')))   
                                    conn.commit()
                                    tkinter.messagebox.showinfo("Books Rental System", "Report Updated Successfully")
                                    displayReport()
                                    clear()
                                    conn.close()
                            except:
                                tkinter.messagebox.showerror("Book Rental System", "Update Failed")
                                   
        def deleteReport():   
            messageDelete = tkinter.messagebox.askyesno("Book Rental System", "Do you want to remove this transaction?")
            if messageDelete > 0:   
                con = sqlite3.connect("BRS.db")
                cur = con.cursor()
                x = self.orderlist.selection()[0]
                id_no = self.orderlist.item(x)["values"][0]
                cur.execute("DELETE FROM report WHERE ReportOrderNo = ?",(id_no,)) 
                con.commit()
                self.orderlist.delete(x)
                tkinter.messagebox.showinfo("Book Rental System", "Transaction deleted from database")
                displayReport()
                con.close()   
                        
        def searchReport():
            search = Search.get()  
            searchby = SearchBy.get()              
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM report")
            con.commit()
            self.orderlist.delete(*self.orderlist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if searchby == 'Rent Order':
                    if str(row[0]).count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "Borrower's ID":
                    if row[1].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Name':
                    if row[2].startswith(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Book Number':
                    if row[3].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Borrowed Date':
                    if row[4].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Due Date':
                    if row[5].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                else:
                    if row[6].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
 
        def showAll():
            displayReport()
        
        def clear():
            BIDNum.set('')
            Name.set('')
            BNumber.set('')
            BDate.set('')
            DDate.set('')
            RDate.set('')
            
        def OnDoubleClick(event):
            item = self.orderlist.selection()[0]
            values = self.orderlist.item(item, "values")
            row.set(values[0])
            BNumber.set(values[3])
            RDate.set(values[6])
            
        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()

        ## Window Buttons
        
        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")
        
        self.txtDDate = Entry(self, font=("Poppins", 13), textvariable=row, width=10, bg="#375971", fg="snow")
        self.txtDDate.place(x=890,y=200)
        
        self.orderlist = ttk.Treeview(self,
                                        columns=("Rent Order No.","Borrower's ID","Name","Book Number","Borrow Date", "Due Date","Return Date"),
                                        height = 13)
        
        self.orderlist.heading("Rent Order No.", text="Rent Order No.",anchor=W)
        self.orderlist.heading("Borrower's ID", text="Borrower's ID",anchor=W)
        self.orderlist.heading("Name", text="Name",anchor=W) 
        self.orderlist.heading("Book Number", text="Book Number", anchor=W)
        self.orderlist.heading("Borrow Date", text="Borrow Date", anchor=W)   
        self.orderlist.heading("Due Date", text="Due Date", anchor=W)
        self.orderlist.heading("Return Date", text="Return Date", anchor=W)
        self.orderlist['show'] = 'headings'

        self.orderlist.column("Rent Order No.", width=100, anchor=W, stretch=False)
        self.orderlist.column("Borrower's ID", width=115, anchor=W, stretch=False)
        self.orderlist.column("Name", width=400, anchor=W, stretch=False)
        self.orderlist.column("Book Number", width=150, stretch=False)
        self.orderlist.column("Borrow Date", width=115, anchor=W, stretch=False)
        self.orderlist.column("Due Date", width=115, stretch=False)
        self.orderlist.column("Return Date", width=115, stretch=False)
        
        
        self.orderlist.bind("<Double-1>",OnDoubleClick)
        
        self.orderlist.place(x=200,y=180)
        
        lblorderlist = tk.Label(self, font = ("Century Gothic",15), padx=3,width = 92, height = 1,text="Report List", anchor=W, bg="#375971", fg="snow")
        lblorderlist.place(x=200,y=151)
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:")
        self.lblsearchby.place(x=660,y=119)
       
        self.lblBookNum = Label(self, font=("Poppins", 12, "bold"), text="Book Number:", padx=5, pady=5)
        self.lblBookNum.place(x=200,y=475)
        
        self.txtBookNum =ttk.Combobox(self,
                                        values = bookid,
                                        state="readonly", font=("Poppins", 13), textvariable=BNumber, width=38)
        self.txtBookNum.place(x=360,y=480)
        
        self.lblRDate = Label(self, font=("Poppins", 12, "bold"), text="Return Date:", padx=5, pady=5)
        self.lblRDate.place(x=750,y=475)
        self.txtRDate = DateEntry(self, font=("Poppins", 12), state="readonly", textvariable=RDate, width=42,year=2021, month=7, day=21, foreground ="black",\
                       background = "#78a2cc", headersbackground = "#a4c3d2" , normalbackground = "white", weekendbackground="white",\
                       othermonthbackground="white", othermonthwebackground='white')
        self.txtRDate.place(x=890,y=480)
        
        self.txtSearch = Entry(self, font=("Poppins", 13), textvariable=Search,relief=FLAT, width=40)
        self.txtSearch.place(x=900,y=120)
        
        
        
        #### Buttons 
        
        self.add=PhotoImage(file="add.png", master=self)
        self.update=PhotoImage(file="update.png", master=self)
        self.delete=PhotoImage(file="delete.png", master=self)
        self.clear=PhotoImage(file="clear.png", master=self)
        self.search=PhotoImage(file="search.png", master=self)
        self.show=PhotoImage(file="show.png", master=self)
        
        self.btnclear = Button(self, image=self.clear, bd=0, command = clear)
        self.btnclear.place(x=205,y=640)
        self.btnclear.config(cursor= "hand2")
        
        self.btnAddBook = Button(self, image=self.add, bd=0, command = addReport)
        self.btnAddBook.place(x=320,y=640)
        self.btnAddBook.config(cursor= "hand2")
        
        self.btnUpdateBook = Button(self, image=self.update, bd=0, command = updateReport)
        self.btnUpdateBook.place(x=425,y=640)
        self.btnUpdateBook.config(cursor= "hand2")
        
        self.btnDeleteBook = Button(self, image=self.delete, bd=0, command = deleteReport)
        self.btnDeleteBook.place(x=550,y=640)
        self.btnDeleteBook.config(cursor= "hand2")

        self.btnSearchBook = Button(self, image=self.search, bd=0,
                               command=searchReport)
        self.btnSearchBook.place(x=1270,y=116)
        self.btnSearchBook.config(cursor= "hand2")
        
        self.btnShowallOrder = Button(self, image=self.show,bd=0, command = showAll)
        self.btnShowallOrder.place(x=200,y=108)
        self.btnShowallOrder.config(cursor= "hand2")
        
        self.btnSearchBy = ttk.Combobox(self, 
                                        state = "readonly", 
                                        font=('Century Gothic', 10), width=14, textvariable = SearchBy)
        self.btnSearchBy['values'] = ("Rent Order","Borrower's ID","Name","Book Number","Borrowed Date", "Due Date","Return Date")
        self.btnSearchBy.place(x=778,y=120)
  
        displayReport()

class History(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Book Rental System")
        
        uppercolor = tk.Label(self,height = 3,width = 1500, bg="#375971")
        uppercolor.place(x=0,y=0)
        loweruppercolor = tk.Label(self,height = 3,width = 1500, bg="#90a3b0")
        loweruppercolor.place(x=0,y=50)
        leftcolor = tk.Label(self,height = 600,width = 25, bg="grey17")
        leftcolor.place(x=0,y=0)
        
        
        self.books1=PhotoImage(file="books1.png", master=self)
        
        label = tk.Label(self, text="History", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, image=self.books1,bd=0,
                            bg="grey17")
        applogo.place(x=23,y=15)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=140)
        
        Search = StringVar() 
        SearchBy = StringVar()

        def displayHistory():
            self.orderlist.delete(*self.orderlist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM history")
            rows = cur.fetchall()
            for row in rows:
                self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
            conn.close()   
        
        def searchHistory():
            search = Search.get()  
            searchby = SearchBy.get()              
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM history")
            con.commit()
            self.orderlist.delete(*self.orderlist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if searchby == 'Rent Order':
                    if str(row[0]).count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Book ID':
                    if row[1].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "Borrower's ID":
                    if row[2].startswith(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == 'Date Borrowed':
                    if row[3].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
                else:
                    if row[4].count(search):
                        self.orderlist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
            
        def Refresh():
            displayHistory()

        def logout():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM online_user")
            c_user = cur.fetchall()
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                for user in c_user:
                    cur.execute("DELETE FROM online_user WHERE username = ?",(user[0],))
            conn.commit()
            conn.close()
            self.destroy()
            
        ## Window Buttons
        
        self.dash=PhotoImage(file="home.png", master=self)
        self.bookb=PhotoImage(file="b.png", master=self)
        self.author=PhotoImage(file="author.png", master=self)
        self.genre=PhotoImage(file="genre.png", master=self)
        self.repo=PhotoImage(file="repo.png", master=self)
        self.borrow=PhotoImage(file="borrow.png", master=self)
        self.histo=PhotoImage(file="histo.png", master=self)
        self.logout=PhotoImage(file="logout.png", master=self)
        self.rent=PhotoImage(file="rent.png", master=self)
        
        button1 = tk.Button(self, text="  DASHBOARD",font=("Century Gothic",13,"bold"),image=self.dash, bd=0,
                            compound="left", #width = 12
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=15,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="  BOOKS",font=("Century Gothic",13,"bold"), image=self.bookb, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=15,y=280)
        button2.config(cursor= "hand2")

        button3 = tk.Button(self, text="  AUTHOR",font=("Century Gothic",13,"bold"), image=self.author, bd=0,
                            compound ="left", #width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Authors))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="  GENRE",font=("Century Gothic",13,"bold"), image=self.genre, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button4.place(x=15,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="  BORROWER",font=("Century Gothic",13,"bold"),image=self.borrow, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button5.place(x=15,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="  RENT",font=("Century Gothic",13,"bold"),image=self.rent, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button6.place(x=15,y=480)
        button6.config(cursor= "hand2")
        
        button7 = tk.Button(self, text="  REPORT",font=("Century Gothic",13,"bold"),image=self.repo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button7.place(x=15,y=530)
        button7.config(cursor= "hand2")
        
        button8 =tk.Button(self, text="  HISTORY",font=("Century Gothic",13,"bold"),image=self.histo, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(History))
        button8.place(x=15,y=580)
        button8.config(cursor= "hand2")

        button9 = tk.Button(self, text="  LOG-OUT",font=("Century Gothic",13,"bold"),image=self.logout, bd=0,
                            compound ="left",
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button9.place(x=15,y=630)
        button9.config(cursor= "hand2")
        
        self.orderlist = ttk.Treeview(self,
                                        columns=("Rent Order ID","Book ID","Borrower's ID","Date Borrowed","Due Date"),
                                        height = 22)
        
        self.orderlist.heading("Rent Order ID", text="Rent Order ID",anchor=W)
        self.orderlist.heading("Book ID", text="Book ID",anchor=W) 
        self.orderlist.heading("Borrower's ID", text="Borrower's ID", anchor=W)
        self.orderlist.heading("Date Borrowed", text="Date Borrowed", anchor=W)
        self.orderlist.heading("Due Date", text="Due Date", anchor=W)
        self.orderlist['show'] = 'headings'

        self.orderlist.column("Rent Order ID", width=150, anchor=W, stretch=False)
        self.orderlist.column("Book ID", width=300, anchor=W, stretch=False)
        self.orderlist.column("Borrower's ID", width=220, stretch=False)
        self.orderlist.column("Date Borrowed", width=220, stretch=False)
        self.orderlist.column("Due Date", width=220, stretch=False)
        
        self.orderlist.place(x=200,y=180)
        
        lblorderlist = tk.Label(self, font = ("Century Gothic",15), padx=3,width = 92, height = 1,text="List of All Transaction", anchor=W, bg="#375971", fg="snow")
        lblorderlist.place(x=200,y=151)
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:")
        self.lblsearchby.place(x=660,y=119)
        
        self.txtSearch = Entry(self, font=("Poppins", 13), textvariable=Search,relief=FLAT, width=40)
        self.txtSearch.place(x=900,y=120)
        
        #### Buttons
                
        self.show=PhotoImage(file="show.png", master=self)
        self.search=PhotoImage(file="search.png", master=self)
                
        self.btnShowallBook = Button(self, image=self.show, bd=0,command=Refresh)
        self.btnShowallBook.place(x=200,y=108)
        self.btnShowallBook.config(cursor= "hand2")
        
        self.btnSearchBook = Button(self, image=self.search, bd=0,
                               command=searchHistory)
        self.btnSearchBook.place(x=1270,y=116)
        self.btnSearchBook.config(cursor= "hand2")
        
        self.btnSearchBy = ttk.Combobox(self, 
                                        state = "readonly", 
                                        font=('Century Gothic', 10), width=14, textvariable = SearchBy)
        self.btnSearchBy['values'] = ("Rent Order","Book ID","Borrower's ID","Date Borrowed","Due Date")
        self.btnSearchBy.place(x=778,y=120)
        
        displayHistory()         

app = App()
app.geometry("1360x700")
positionRight = int((app.winfo_screenwidth()/2 - 900))
positionDown = int((app.winfo_screenheight()/2 - 389))
app.mainloop()

