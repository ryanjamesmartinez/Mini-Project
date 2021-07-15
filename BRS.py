import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import datetime
from tkcalendar import DateEntry

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.rowconfigure(0, weight=1)
        
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, Register, Dashboard, Books, Genres, Order, History, Report, Borrowers):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Order)

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
        leftcolor = tk.Label(self,height = 600,width = 1350, bg="grey17")
        leftcolor.place(x=0,y=0)

        login = StringVar()
        password = StringVar()
        
        applogo = tk.Label(self, text="🕮", font=("Impact",200),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=540,y=25)
        apptitle = tk.Label(self, text="BOOK RENTAL SYSTEM", font=("Impact",30),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=505,y=330)
        
        def Database():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL)")
            conn.commit() 
            conn.close()
        
        def Login():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            if login.get == "" or password.get() == "":
                tkinter.messagebox.showerror("Book Rental System", "Please require the completed field")
            else:
                cur.execute("SELECT * FROM user WHERE username = ? and password = ?", (login.get(), password.get()))
                if cur.fetchone() is not None:
                    tkinter.messagebox.showinfo("Book Rental System", "Login Successfully")
                    controller.show_frame(Dashboard)
                    login.set('')
                    password.set('')
                else:
                    tkinter.messagebox.showerror("Book Rental System", "Invalid password or username")
            conn.commit() 
            conn.close()
                
        self.lbllogin = tk.Label(self, text="Username", bg="grey17", fg = "snow", font=("Century Gothic",15))
        self.lbllogin.place(x=628,y=450)
        
        self.entrylogin = Entry(self, font=("Poppins", 11), textvariable=login, bd=0,width=41)
        self.entrylogin.place(x=510,y=485)
        
        self.lblpass = tk.Label(self, text="Password", bg="grey17", fg = "snow", font=("Century Gothic",15))
        self.lblpass.place(x=630,y=520)
        
        self.entrypass = Entry(self, font=("Poppins", 11), textvariable=password, bd=0,width=41, show="*")
        self.entrypass.place(x=510,y=555)
          
        self.login = Button(self,font=("Century Gothic", 12,"underline"), text="Login", bd=0, bg="gray17", fg="snow",
                                    command=Login)
        self.login.config(cursor= "hand2")
        self.login.place(x=650,y=590)
        
        self.reg = Button(self,font=("Century Gothic", 12,"underline"), text="Register", bd=0, bg="gray17", fg="snow",
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
        leftcolor = tk.Label(self,height = 600,width = 1350, bg="grey17")
        leftcolor.place(x=0,y=0)

        
        login = StringVar()
        password = StringVar()
        role= StringVar()
        
        applogo = tk.Label(self, text="🕮", font=("Impact",200),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=540,y=25)
        apptitle = tk.Label(self, text="BOOK RENTAL SYSTEM", font=("Impact",30),bd=0,
                            bg="grey17",
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
               
        
        self.lbllogin = tk.Label(self, text="Username", bg="grey17", fg = "snow", font=("Century Gothic",15))
        self.lbllogin.place(x=628,y=390)
        
        self.entrylogin = Entry(self, font=("Poppins", 11), textvariable=login, bd=0,width=41)
        self.entrylogin.place(x=510,y=420)
        
        self.lblpass = tk.Label(self, text="Password", bg="grey17", fg = "snow", font=("Century Gothic",15))
        self.lblpass.place(x=630,y=455)
        
        self.entrypass = Entry(self, font=("Poppins", 11), textvariable=password, bd=0,width=41, show="*")
        self.entrypass.place(x=510,y=485)

        self.lblrole = tk.Label(self, text="Role:", bg="grey17", fg = "snow", font=("Century Gothic",15))
        self.lblrole.place(x=650,y=520)

        self.entryrole = ttk.Combobox(self, value=["Admin", "Staff"], font=("Poppins", 11),
                                             state="readonly", textvariable=role, width=39)
        self.entryrole.place(x=510,y=550)

        
          
        self.login = Button(self,font=("Century Gothic", 12,"underline"), text="Login", bd=0, bg="gray17", fg="snow",
                                    command=lambda: controller.show_frame(Login))
        self.login.config(cursor= "hand2")
        self.login.place(x=650,y=626)

        self.reg = Button(self,font=("Century Gothic", 12,"underline"), text="Register", bd=0, bg="gray17", fg="snow",
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
        
        totalbooks = tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "     Total Books\n", anchor=SW)
        totalbooks.place(x=205,y=125)
        bookicon = tk.Label(self,font=("Century Gothic", 49), bg="#375971", fg="snow", text= "📖", anchor=SW)
        bookicon.place(x=370,y=125)
        
        booksavailable= tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "     Books Available\n", anchor=SW)
        booksavailable.place(x=490,y=125)
        booksavailableicon = tk.Label(self,font=("Century Gothic", 49), bg="#375971", fg="snow", text= "📚", anchor=SW)
        booksavailableicon.place(x=655,y=125)
        
        totalborrower = tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "     Total Borrowers\n", anchor=SW)
        totalborrower.place(x=780,y=125)
        totalborrower = tk.Label(self,font=("Century Gothic", 49), bg="#375971", fg="snow", text= "👥", anchor=SW)
        totalborrower.place(x=935,y=125)
        
  
        totalreport = tk.Label(self,font=("Century Gothic", 15), padx=3, pady=7, height = 6, width = 21, 
                                    bg="#375971", fg="snow", text= "     Total Reports\n", anchor=SW)
        totalreport.place(x=1060,y=125)
        reporticon = tk.Label(self,font=("Century Gothic", 49), bg="#375971", fg="snow", text= "📣", anchor=SW)
        reporticon.place(x=1225,y=125)
        
        genres = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="Genres", anchor=N)
        genres.place(x=205,y=300)
        genresicon = tk.Label(self, font=("Century Gothic", 49), bg="#375971",fg="snow",text="📔")
        genresicon.place(x=215,y=310)
        
        issued = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="Issued", anchor=N)
        issued.place(x=490,y=300)
        issuedicon = tk.Label(self, font=("Century Gothic", 49), bg="#375971",fg="snow",text="📝")
        issuedicon.place(x=500,y=308)
        
        returned = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="       Returned", anchor=N)
        returned.place(x=780,y=300)
        like = tk.Label(self, font=("Century Gothic", 49), bg="#375971",fg="snow",text=" 👍")
        like.place(x=780,y=300)
        
        notreturned = tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="\tNot Returned", anchor=N)
        notreturned.place(x=1060,y=300)
        dislike = tk.Label(self, font=("Century Gothic", 49), bg="#375971",fg="snow",text=" 👎")
        dislike.place(x=1060,y=300)
        
        time =  tk.Label(self,font=("Century Gothic", 15),padx=3, pady=7, height = 4,width = 21,
                            bg="#375971",fg="snow",text="    Time", anchor=N)
        time.place(x=205,y=430)
        timeicon = tk.Label(self, font=("Century Gothic", 49), bg="#375971",fg="snow",text="⏲️")
        timeicon.place(x=220,y=435)
        
        label = tk.Label(self, text="Dashboard", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, text="🕮", font=("Impact",70),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=40,y=5)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=130)
        
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
            cur.execute("CREATE TABLE IF NOT EXISTS books (BookNumber VARCHAR(10) PRIMARY KEY, ISBN VARCHAR(16) NOT NULL, Title VARCHAR(50) NOT NULL, Author VARCHAR(100) NOT NULL, Genre VARCHAR(100) NOT NULL, Status VARCHAR(10) NOT NULL)") 
            cur.execute("CREATE TABLE IF NOT EXISTS booksavailable (BookNumber VARCHAR(10) PRIMARY KEY, ISBN VARCHAR(16) NOT NULL, Title VARCHAR(50) NOT NULL, Author VARCHAR(100) NOT NULL, Genre VARCHAR(100) NOT NULL)") 
            cur.execute("CREATE TABLE IF NOT EXISTS return (returnID INTEGER PRIMARY KEY AUTOINCREMENT, BookNumber VARCHAR(10), ISBN VARCHAR(16) NOT NULL, Title VARCHAR(50) NOT NULL, Author VARCHAR(100) NOT NULL, Genre VARCHAR(100) NOT NULL)")
            cur.execute("CREATE TABLE IF NOT EXISTS borrower (BorrowerIDNum VARCHAR(9) PRIMARY KEY, ValidID VARCHAR(100) NOT NULL, Name VARCHAR(50) NOT NULL, EmailAdd VARCHAR(50) NOT NULL, PhoneNum VARCHAR(11) NOT NULL)")           
            conn.commit() 
            conn.close()
        
        def connectGenre():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS genres (Genre VARCHAR(100) PRIMARY KEY NOT NULL)")
            conn.commit() 
            conn.close()
            
        def connectOrder():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS rent (RentOrderNo INTEGER PRIMARY KEY AUTOINCREMENT, BookNumber VARCHAR(10) NOT NULL, BorrowersID VARCHAR(9) NOT NULL, \
                        DateBorrowed DATE NOT NULL, DueDate DATE NOT NULL, ReturnDate DATE NOT NULL, \
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
            cur.execute("SELECT * FROM booksavailable")
            rows = cur.fetchall()
            tbooksavailable.set(len(rows))
            self.ttlbooksavailable = Label(self, font=("Impact", 40),textvariable = tbooksavailable, bg ="#375971", fg = "snow")
            self.ttlbooksavailable.place(x=595,y=150)
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
            self.tborrowers.place(x=880,y=150)
            self.after(1000,borrower)
            conn.commit()            
            conn.close()
        
        def genre():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM genres")
            rows = cur.fetchall()
            tgenre.set(len(rows))
            self.tgenre = Label(self, font=("Impact", 40),textvariable = tgenre, bg ="#375971", fg = "snow")
            self.tgenre.place(x=360,y=330)
            self.after(1000,genre)
            conn.commit()            
            conn.close()   
        
        def issued():
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM history")
            rows = cur.fetchall()
            tissued.set(len(rows))
            self.tissued = Label(self, font=("Impact", 40),textvariable = tissued, bg ="#375971", fg = "snow")
            self.tissued.place(x=650,y=330)
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
            self.ttlreturned.place(x=940,y=330)
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
            self.ttlnotreturned.place(x=1220,y=330)
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
            self.ttlreport.place(x=1160,y=150)
            self.after(1000,reports)
            conn.commit()            
            conn.close()

        lab = Label(self, font=("Century Gothic",20), bg="#375971",fg="snow")
        lab.place(x=320,y=465)

        def clock():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            lab.config(text=time)
            self.after(1000, clock) # run itself again after 1000 ms
        
        clock()

        def logout():
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                
                
                    
        ## Window Buttons
        
        button1 = tk.Button(self, text="⯀ DASHBOARD",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=25,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="⯀ BOOKS",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=12,y=280)
        button2.config(cursor= "hand2")
        
        button3 = tk.Button(self, text="⯀ GENRES",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="⯀ BORROWER",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button4.place(x=21,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="⯀ RENT   ",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button5.place(x=10,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="⯀ REPORT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button6.place(x=13,y=480)
        button6.config(cursor= "hand2")
        
        button7 =tk.Button(self, text="⯀ HISTORY",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button7.place(x=17,y=530)
        button7.config(cursor= "hand2")
        #90a3b0

        button8 = tk.Button(self, text="⯀ LOG-OUT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button8.place(x=11,y=580)
        button8.config(cursor= "hand2")

        connect()
        connectGenre()
        connectOrder()
        connectHistory()
        connectReport()
        books()
        booksavail()
        genre()
        issued()
        returned()
        notreturned()
        borrower()
        reports()

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
        
        
        label = tk.Label(self, text="Books", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, text="🕮", font=("Impact",70),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=40,y=5)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=130)
        
        BookNumber = StringVar()
        ISBN = StringVar()
        Title = StringVar()
        Author = StringVar()
        Genre = StringVar()
        Search = StringVar()
        SearchAvail = StringVar()
        Showby = StringVar()
        Status = StringVar()
        Searchby = StringVar()

        def addBook():
            if BookNumber.get() == "" or ISBN.get() == "" or Title.get() == "" or Author.get() == "" or Genre.get() == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                conn = sqlite3.connect("BRS.db")
                c = conn.cursor()         
                c.execute("INSERT INTO books(BookNumber, ISBN, Title, Author, Genre, Status) VALUES (?,?,?,?,?,'Available')",\
                          (BookNumber.get(),ISBN.get(),Title.get(),Author.get(), Genre.get()))
                c.execute("INSERT INTO booksavailable(BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
                          (BookNumber.get(),ISBN.get(),Title.get(),Author.get(), Genre.get()))
                conn.commit()           
                conn.close()
                clear()
                tkinter.messagebox.showinfo("Book Rental System", "Book added to database")
                displayBook()
            
        def returnbook():
            conn = sqlite3.connect("BRS.db")
            c = conn.cursor()  
            c.execute("SELECT * FROM books")
            c.execute("UPDATE books SET BookNumber = ?,ISBN = ?, Title = ?, Author = ? ,Genre = ?, Status = 'Available' WHERE BookNumber=?",\
                      (BookNumber.get(),ISBN.get(),Title.get(),Author.get(),Genre.get(),BookNumber.get()))
            c.execute("INSERT INTO booksavailable(BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
                      (BookNumber.get(),ISBN.get(),Title.get(),Author.get(), Genre.get()))
            c.execute("INSERT INTO return (BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
                      (BookNumber.get(),ISBN.get(),Title.get(),Author.get(), Genre.get()))
            conn.commit()  
            displayBook()
            conn.close()
            clear()
            tkinter.messagebox.showinfo("Book Rental System", "Book returned to database")
            
        def displayBook():
            self.booklist.delete(*self.booklist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur1 = conn.cursor()
            cur2 = conn.cursor() 
            cur1.execute("SELECT * FROM books")
            cur2.execute("SELECT * FROM rent")
            rows = cur1.fetchall()
            rows2 = cur2.fetchall()
            for row in rows:
                self.booklist.insert("", tk.END, text=row[0], values=row[0:])
            for book in rows:
                for rent in rows2:
                    if book[0]==rent[1]:
                        cur1.execute("UPDATE books SET BookNumber = ?,ISBN = ?, Title = ?, Author = ? ,Genre = ?, Status = 'Unavailable' WHERE BookNumber=?",\
                                     (book[0],book[1],book[2],book[3],book[4],book[0]))
                        conn.commit()
                    else:
                        pass
            conn.close()
        
        def updateBook():
            if BookNumber.get() == "" or ISBN.get() == "" or Title.get() == "" or Author.get() == "" or Genre.get() == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                for selected in self.booklist.selection():
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    #cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("UPDATE books SET BookNumber = ?,ISBN = ?, Title = ?, Author = ? ,Genre = ?, Status = ? WHERE BookNumber=?", \
                                (BookNumber.get(),ISBN.get(),Title.get(),Author.get(),Genre.get(),self.booklist.set(selected, '#6'), self.booklist.set(selected, '#1')))   
                    conn.commit()
                    tkinter.messagebox.showinfo("Books Rental System", "Book Updated Successfully")
                    displayBook()
                    clear()
                    conn.close()
                                   
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
            cur.execute("SELECT * FROM books")
            con.commit()
            self.booklist.delete(*self.booklist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if searchby == "Book Number":
                    if row[0].startswith(search):
                        self.booklist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "ISBN":
                    if row[1].startswith(search):
                        self.booklist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "Title":
                    if row[2].count(search):
                        self.booklist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby =="Author":
                    if row[3].count(search):
                        self.booklist.insert("", tk.END, text=row[0], values=row[0:])
                elif searchby == "Genre":
                    if row[4].count(search):
                        self.booklist.insert("", tk.END, text=row[0], values=row[0:])
                else:
                    if row[5].startswith(search):
                        self.booklist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
        
        def searchAvailBook():
            search = SearchAvail.get()                
            con = sqlite3.connect("BRS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM booksavailable WHERE BookNumber = ?",(search,))
            con.commit()
            self.booklist.delete(*self.booklist.get_children())
            rows = cur.fetchall()
            for row in rows:
                if row[0].startswith(search):
                    self.booklist.insert("", tk.END, text=row[0], values=row[0:])
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
            Genre.set('')
            
        def OnDoubleClick(event):
            item = self.Availablebooklist.selection()[0]
            values = self.Availablebooklist.item(item, "values")
            BookNumber.set(values[0])
            ISBN.set(values[1])
            Title.set(values[2])
            Author.set(values[3])
            Genre.set(values[4])
            
        def OnDoubleClick2(event):
            item = self.booklist.selection()[0]
            values = self.booklist.item(item, "values")
            BookNumber.set(values[0])
            ISBN.set(values[1])
            Title.set(values[2])
            Author.set(values[3])
            Genre.set(values[4])

        def logout():
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)

        ## Window Buttons
        
        button1 = tk.Button(self, text="⯀ DASHBOARD",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=25,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="⯀ BOOKS",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=12,y=280)
        button2.config(cursor= "hand2")
        
        button3 = tk.Button(self, text="⯀ GENRES",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="⯀ BORROWER",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button4.place(x=21,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="⯀ RENT   ",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button5.place(x=10,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="⯀ REPORT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button6.place(x=13,y=480)
        button6.config(cursor= "hand2")
        
        button7 =tk.Button(self, text="⯀ HISTORY",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button7.place(x=17,y=530)
        button7.config(cursor= "hand2")

        button8 = tk.Button(self, text="⯀ LOG-OUT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button8.place(x=11,y=580)
        button8.config(cursor= "hand2")

         
        booklist = tk.Label(self,height = 2,width = 108, bg="#89E894")
        
        self.booklist = ttk.Treeview(self,
                                        columns=("Book Number","ISBN", "Title", "Author", "Book Genre","Status"),
                                        height = 13)

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
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:", width = 72, padx=5, pady=5,bg="#90a3b0")
        self.lblsearchby.place(x=650,y=116)
        
        lblbooklist = tk.Label(self, font = ("Century Gothic",15), padx = 3 ,width =92, height = 1,text="List of All Books",anchor=W, bg="#375971", fg="snow")
        lblbooklist.place(x=200,y=151)
        
        self.lblBookISBN = Label(self, font=("Poppins", 12, "bold"), text="Book Number:", padx=5, pady=5)
        self.lblBookISBN.place(x=200,y=475)
        self.txtBookISBN = Entry(self, font=("Poppins", 13), textvariable=BookNumber, width=38)
        self.txtBookISBN.place(x=330,y=480)
        
        self.lblISBN = Label(self, font=("Poppins", 12, "bold"), text="ISBN:", padx=5, pady=5)
        self.lblISBN.place(x=200,y=515)
        self.txtISBN = Entry(self, font=("Poppins", 13), textvariable=ISBN, width=38)
        self.txtISBN.place(x=330,y=520)
        
        self.lblTitle = Label(self, font=("Poppins", 12, "bold"), text="Title:", padx=5, pady=5)
        self.lblTitle.place(x=200,y=555)
        self.txtTitle = Entry(self, font=("Poppins", 13), textvariable=Title, width=38)
        self.txtTitle.place(x=330,y=560)
        
        self.lblAuthor = Label(self, font=("Poppins", 12, "bold"), text="Author:", padx=5, pady=5)
        self.lblAuthor.place(x=200,y=595)
        self.txtAuthor = Entry(self, font=("Poppins", 13), textvariable=Author, width=38)
        self.txtAuthor.place(x=330,y=600)
        
        self.lblGenre = Label(self, font=("Poppins", 12, "bold"), text="Genre:", padx=5, pady=5)
        self.lblGenre.place(x=700,y=475)
        self.txtGenre= Entry(self, font=("Poppins", 13), textvariable=Genre, width=38)
        self.txtGenre.place(x=830,y=480)
        
        self.txtSearch = Entry(self, font=("Poppins", 13), textvariable=Search, width=40)
        self.txtSearch.place(x=900,y=120)

        self.btnSearchBy = ttk.Combobox(self, 
                                        state = "readonly", 
                                        font=('Century Gothic', 10), width=14, textvariable = Searchby)
        self.btnSearchBy['values'] = ("Book Number","ISBN", "Title", "Author", "Genre", "Status")
        self.btnSearchBy.place(x=778,y=120)
                
        
        #### Buttons 
        
        self.btnAddBook = Button(self, text="➕  ADD", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=addBook)
        self.btnAddBook.place(x=330,y=650)
        self.btnAddBook.config(cursor= "hand2")
        
        self.btnUpdateBook = Button(self, text="⟲  UPDATE", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=updateBook)
        self.btnUpdateBook.place(x=455,y=650)
        self.btnUpdateBook.config(cursor= "hand2")
        
        self.btnCLear = Button(self, text="CLEAR", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=clear)
        self.btnCLear.place(x=205,y=650)
        self.btnCLear.config(cursor= "hand2")
        
        self.btnSearchBook = Button(self,  text="🔍",font= ('Poppins', 13),  bd=0, 
                               command=searchBook, bg="#90a3b0")
        self.btnSearchBook.place(x=1280,y=116)
        self.btnSearchBook.config(cursor= "hand2")
        
        self.btnShowallBook = Button(self, text="SHOW ALL", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=showAll)
        self.btnShowallBook.place(x=200,y=118)
        self.btnShowallBook.config(cursor= "hand2")
             
        displayBook()

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
        
        label = tk.Label(self, text="Genre", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, text="🕮", font=("Impact",70),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=40,y=5)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=130)
        
        Search = StringVar()
        title = StringVar()
        author = StringVar()
        genre = StringVar()
                    
        def displayGenre():
            self.genrelist.delete(*self.genrelist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur1 = conn.cursor()
            cur.execute("SELECT * FROM books")
            
            list_of_genres = []
            list_of_genres2 = []
            unique_genre = []
            genres = cur.fetchall()
            
            for genre in genres:
               list_of_genres.append(genre[4]) 
               
            for genre in list_of_genres:
                list_of_genres2.append(genre.split(', '))
            
            for genre in list_of_genres2:
                for u_genre in genre:
                    if u_genre not in unique_genre:
                        unique_genre.append(u_genre)
                        try:
                            cur1.execute("INSERT INTO genres(Genre) VALUES (?)",(u_genre,))
                        except:
                            pass          
            cur1.execute("SELECT * FROM genres")    
            rows = cur1.fetchall()
            for row in rows:
                self.genrelist.insert("", tk.END, text=row[0], values=row[0:])
                
            conn.commit()    
            conn.close()
        
        def displayBooks():
            self.booklist.delete(*self.booklist.get_children())
            conn = sqlite3.connect("BRS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM books")
            rows = cur.fetchall()
            for row in rows:
                self.booklist.insert("", tk.END, text=row[0], values=row[0:])
                
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
            cur.execute("SELECT * FROM books") 
            con.commit()
            self.booklist.delete(*self.booklist.get_children())
            rows = cur.fetchall()   
            item = self.genrelist.selection()[0]
            values = self.genrelist.item(item, "values")  
            
            search = values[0]
            for row in rows:
                if row[4].count(search):
                    self.booklist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
            
        def OnDoubleClick2(event):
            item = self.booklist.selection()[0]
            values = self.booklist.item(item, "values")
            title.set(values[2])
            author.set(values[3])
            genre.set(values[4])
            
        def logout():
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
        
        ## Window Buttons
        
        button1 = tk.Button(self, text="⯀ DASHBOARD",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=25,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="⯀ BOOKS",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=12,y=280)
        button2.config(cursor= "hand2")
        
        button3 = tk.Button(self, text="⯀ GENRES",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Genres))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="⯀ BORROWER",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button4.place(x=21,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="⯀ RENT   ",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button5.place(x=10,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="⯀ REPORT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button6.place(x=13,y=480)
        button6.config(cursor= "hand2")
        
        button7 =tk.Button(self, text="⯀ HISTORY",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button7.place(x=17,y=530)
        button7.config(cursor= "hand2")

        button8 = tk.Button(self, text="⯀ LOG-OUT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button8.place(x=11,y=580)
        button8.config(cursor= "hand2")

        self.genrelist = ttk.Treeview(self,
                                        columns=("Genre"),
                                        height = 22)
        
        self.genrelist.heading("Genre", text="Genre",anchor=W)
        self.genrelist['show'] = 'headings'

        self.genrelist.column("Genre", width=300, anchor=W, stretch=False)
        
        self.genrelist.bind("<Double-1>",OnDoubleClick)
        
        self.genrelist.place(x=200,y=180)
        
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
        
        self.btnShowall = Button(self, text="SHOW ALL", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=showAll)
        self.btnShowall.place(x=200,y=118)
        self.btnShowall.config(cursor= "hand2")

        self.btnDeleteGenre = Button(self, text="➖  DELETE", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command = deleteGenre)
        self.btnDeleteGenre.place(x=320,y=118)
        self.btnDeleteGenre.config(cursor= "hand2")
        
        
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
        
        applogo = tk.Label(self, text="🕮", font=("Impact",70),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=40,y=5)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=130)
        
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
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)

        ## Window Buttons
        
        button1 = tk.Button(self, text="⯀ DASHBOARD",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=25,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="⯀ BOOKS",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=12,y=280)
        button2.config(cursor= "hand2")
        
        button3 = tk.Button(self, text="⯀ GENRES",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="⯀ BORROWER",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Borrowers))
        button4.place(x=21,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="⯀ RENT   ",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button5.place(x=10,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="⯀ REPORT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button6.place(x=13,y=480)
        button6.config(cursor= "hand2")
        
        button7 =tk.Button(self, text="⯀ HISTORY",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button7.place(x=17,y=530)
        button7.config(cursor= "hand2")

        button8 = tk.Button(self, text="⯀ LOG-OUT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button8.place(x=11,y=580)
        button8.config(cursor= "hand2")
         
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
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:", width = 72, padx=5, pady=5,bg="#90a3b0")
        self.lblsearchby.place(x=650,y=116)
        
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
        
        self.btnAddBook = Button(self, text="➕  ADD", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command=addBorrower)
        self.btnAddBook.place(x=330,y=650)
        self.btnAddBook.config(cursor= "hand2")
        
        self.btnUpdateBook = Button(self, text="⟲  UPDATE", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=updateBorrower)
        self.btnUpdateBook.place(x=455,y=650)
        self.btnUpdateBook.config(cursor= "hand2")
        
        
        self.btnDeleteBook = Button(self, text="➖  DELETE", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command=deleteBorrower)
        self.btnDeleteBook.place(x=585,y=650)
        self.btnDeleteBook.config(cursor= "hand2")
        
        self.btnCLear = Button(self, text="CLEAR", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command=clear)
        self.btnCLear.place(x=205,y=650)
        self.btnCLear.config(cursor= "hand2")
        
        
        self.btnShowallOrder = Button(self, text="SHOW ALL", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command = showAll)
        self.btnShowallOrder.place(x=200,y=118)
        self.btnShowallOrder.config(cursor= "hand2")
        
        self.btnSearchBook = Button(self, text="🔍", font=('Poppins', 13),  bd=0, bg="#90a3b0",
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
        
        label = tk.Label(self, text="Rent", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, text="🕮", font=("Impact",70),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=40,y=5)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=130)
        
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
                conn = sqlite3.connect("BRS.db")
                cur = conn.cursor()
                cur1 = conn.cursor()    
                cur2 = conn.cursor() 
                cur3 = conn.cursor()
                cur.execute("SELECT * FROM books")
                cur3.execute("SELECT * FROM borrower")
                books = cur.fetchall()
                for book in books:
                    if book[0] == BookNumber.get() and book[5] != 'Unavailable':
                        try:
                            cur1.execute("PRAGMA foreign_keys = ON")
                            cur1.execute("INSERT INTO rent (BookNumber, BorrowersID, DateBorrowed, DueDate, ReturnDate) VALUES (?,?,strftime('%m/%d/%Y'),?,?)",\
                                         (BookNumber.get(),BorrowersID.get(),DueDate.get(),ReturnDate.get()))
                            cur1.execute("INSERT INTO history(BookNumber, BorrowersID, DateBorrowed, DueDate, ReturnDate) VALUES (?,?,strftime('%m/%d/%Y'),?,?)",\
                                         (BookNumber.get(),BorrowersID.get(),DueDate.get(),ReturnDate.get())) 
                            cur.execute("UPDATE books SET BookNumber = ?, ISBN = ?, Title = ?, Author = ?, Genre = ?, Status = 'Unavailable' WHERE BookNumber = ?",
                                     (book[0],book[1],book[2],book[3],book[4],book[0]))
                            cur2.execute("SELECT * FROM booksavailable")
                            rows = cur2.fetchall()
                            booknum =BookNumber.get()
                            for row in rows:
                                cur2.execute("DELETE FROM booksavailable WHERE BookNumber = ?",(booknum,))    
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
            if  BookNumber.get() == "" or BorrowersID.get() == "" or DateBorrowed == "":
                tkinter.messagebox.showerror("Book Rental System","Please fill in the blank.")
            else:
                for selected in self.orderlist.selection():
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("UPDATE rent SET  BookNumber = ?, BorrowersID = ?,  DateBorrowed = ?, DueDate = ?, ReturnDate = ? WHERE RentOrderNo=?", \
                                (BookNumber.get(),BorrowersID.get(),DateBorrowed.get(),DueDate.get(),ReturnDate.get(), self.orderlist.set(selected, '#1')))   
                    conn.commit()
                    tkinter.messagebox.showinfo("Books Rental System", "Order Updated Successfully")
                    displayOrder()
                    clear()
                    conn.close()
                                   
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
                        cur2.execute("UPDATE books SET BookNumber = ?, ISBN = ?, Title = ?, Author = ?, Genre = ?, Status = 'Available' WHERE BookNumber = ?",
                                     (bookn,book[1],book[2],book[3],book[4],bookn))  
                        cur2.execute("INSERT INTO booksavailable (BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
                                     (bookn,book[1],book[2],book[3],book[4]))
                        cur2.execute("INSERT INTO return (BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
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
            ReturnDate.set(values[5])

        def logout():
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                
        con = sqlite3.connect("BRS.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM books")
        books = cur.fetchall()
        bookid = []
        for book in books:
            if str(book[5]) == 'Available':
                bookid.append(book[0])

        cur.execute("SELECT * FROM borrower")
        borrower=cur.fetchall()
        bIDNum =[]
        for b in borrower:
            bIDNum.append(b[0]) 
            
        
        ## Window Buttons
        
        button1 = tk.Button(self, text="⯀ DASHBOARD",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=25,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="⯀ BOOKS",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=12,y=280)
        button2.config(cursor= "hand2")
        
        button3 = tk.Button(self, text="⯀ GENRES",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="⯀ BORROWER",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button4.place(x=21,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="⯀ RENT   ",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Order))
        button5.place(x=10,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="⯀ REPORT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button6.place(x=13,y=480)
        button6.config(cursor= "hand2")
        
        button7 =tk.Button(self, text="⯀ HISTORY",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button7.place(x=17,y=530)
        button7.config(cursor= "hand2")

        button8 = tk.Button(self, text="⯀ LOG-OUT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button8.place(x=11,y=580)
        button8.config(cursor= "hand2")

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
        self.txtDueDate = DateEntry(self, font=("Poppins", 13), textvariable=DueDate, width=23, year=2021, month=7, day=7, bg="blue", fg="snow")
        self.txtDueDate.place(x=330,y=275)
             
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:", width = 58, padx=5, pady=5,bg="#90a3b0")
        self.lblsearchby.place(x=760,y=116)
        
        self.txtSearch = Entry(self, font=("Poppins", 13),  textvariable=Search,relief=FLAT, width=30)
        self.txtSearch.place(x=998,y=120)
        
        self.btnAddOrder = Button(self, text="➕  ADD ORDER", font=('Poppins', 11), height=1, width=17, bd=1, 
                               bg="#90a3b0", command = addOrder)
        self.btnAddOrder.place(x=380,y=450)
        self.btnAddOrder.config(cursor= "hand2")
        
        self.btnclear = Button(self, text="CLEAR", font=('Poppins', 11), height=1, width=17, bd=1, 
                               bg="#90a3b0", command = clear)
        self.btnclear.place(x=215,y=450)
        self.btnclear.config(cursor= "hand2")
        
        self.btnUpdateOrder = Button(self, text="⟲  UPDATE ORDER", font=('Poppins', 11), height=1, width=17, bd=1, 
                               bg="#90a3b0", command = updateOrder)
        self.btnUpdateOrder.place(x=215,y=500)
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
        
        self.btnSearchBook = Button(self, text="🔍", font=('Poppins', 13),  bd=0, bg="#90a3b0",
                               command=searchOrder)
        self.btnSearchBook.place(x=1250,y=116)
        self.btnSearchBook.config(cursor= "hand2")
        
        
        self.btnShowallBook = Button(self, text="SHOW ALL", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=showAll)
        self.btnShowallBook.place(x=600,y=118)
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
        
        
        label = tk.Label(self, text="Report", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, text="🕮", font=("Impact",70),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=40,y=5)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=130)
        
        
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
        cur.execute("SELECT * FROM books")
        bookid = []
        books = cur.fetchall()
        for book in books:
            if str(book[5]) == 'Unavailable':
                if book[5] not in bookid:
                    bookid.append(book[0])
        """
        cur.execute("SELECT * FROM rent")
        bIDNum =[]
        borrower=cur.fetchall()
        for b in borrower:
            if b[2] not in bIDNum:
                bIDNum.append(b[2])
        con.commit()
        """
        
        def addReport():
            if BNumber.get() == "" or RDate.get() == "":
                    tkinter.messagebox.showerror("Book Rental System", "Please fill in the box")
            else: 
                conn = sqlite3.connect("BRS.db")
                cur = conn.cursor()
                cur2 = conn.cursor()
                cur3 = conn.cursor()
                cur.execute("SELECT * FROM borrower")
                cur2.execute("SELECT * FROM books")
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
                                               (rent[2], Name,BNumber.get(), rent[3], rent[4],RDate.get()))
                                    for book in books:
                                        if str(BNumber.get()) == str(book[0]):
                                            cur2.execute("UPDATE books SET BookNumber = ?, ISBN = ?, Title = ?, Author = ?, Genre = ?, Status = 'Available' WHERE BookNumber = ?",
                                                         (BNumber.get(),book[1],book[2],book[3],book[4],BNumber.get()))  
                                            cur2.execute("INSERT INTO booksavailable (BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
                                                         (BNumber.get(),book[1],book[2],book[3],book[4]))
                                            cur2.execute("INSERT INTO return (BookNumber, ISBN, Title, Author, Genre) VALUES (?,?,?,?,?)",\
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
                for selected in self.orderlist.selection():
                    conn = sqlite3.connect("BRS.db")
                    cur = conn.cursor()
                    cur.execute("UPDATE report SET BIDNum = ?, Name = ?, BookNumber = ?,DateBorrowed = ?, DueDate = ?, ReturnDate = ? WHERE ReportOrderNo = ?", \
                                (BIDNum.get(), Name.get(),BNumber.get(), BDate.get(), DDate.get(),RDate.get(), self.orderlist.set(selected, '#1')))   
                    conn.commit()
                    tkinter.messagebox.showinfo("Books Rental System", "Book Updated Successfully")
                    displayReport()
                    clear()
                    conn.close()
                                   
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
            BIDNum.set(values[0])
            Name.set(values[1])
            BNumber.set(values[2])
            BDate.set(values[3])
            DDate.set(values[4])
            RDate.set(values[5])
            
        def logout():
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)

        ## Window Buttons
        
        button1 = tk.Button(self, text="⯀ DASHBOARD",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=25,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="⯀ BOOKS",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=12,y=280)
        button2.config(cursor= "hand2")
        
        button3 = tk.Button(self, text="⯀ GENRES",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="⯀ BORROWER",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button4.place(x=21,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="⯀ RENT   ",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button5.place(x=10,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="⯀ REPORT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(Report))
        button6.place(x=13,y=480)
        button6.config(cursor= "hand2")
        
        button7 =tk.Button(self, text="⯀ HISTORY",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(History))
        button7.place(x=17,y=530)
        button7.config(cursor= "hand2")

        button8 = tk.Button(self, text="⯀ LOG-OUT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button8.place(x=11,y=580)
        button8.config(cursor= "hand2")
        
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
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:", width = 72, padx=5, pady=5,bg="#90a3b0")
        self.lblsearchby.place(x=650,y=116)
        
        """
        self.lblBorrowerID = Label(self, font=("Poppins", 12, "bold"), text="Borrower's ID Num:", padx=5, pady=5)
        self.lblBorrowerID.place(x=200,y=475)
        self.txtBorrowerID = ttk.Combobox(self,
                                        values = bIDNum,
                                        state="readonly", font=("Poppins", 13), textvariable=BIDNum, width=38)
        self.txtBorrowerID.place(x=360,y=480)
        """
        
        self.lblBookNum = Label(self, font=("Poppins", 12, "bold"), text="Book Number:", padx=5, pady=5)
        self.lblBookNum.place(x=200,y=475)
        
        self.txtBookNum =ttk.Combobox(self,
                                        values = bookid,
                                        state="readonly", font=("Poppins", 13), textvariable=BNumber, width=38)
        self.txtBookNum.place(x=360,y=480)
        
        #self.lblBDate = Label(self, font=("Poppins", 12, "bold"), text="Borrow Date:", padx=5, pady=5)
        #self.lblBDate.place(x=750,y=415)
        #self.txtBDate = DateEntry(self, font=("Poppins", 13), textvariable=BDate, width=38,year=2021, month=7, day=7, bg="#375971", fg="snow")
        #self.txtBDate.place(x=890,y=420)
        
        #self.lblDDate = Label(self, font=("Poppins", 12, "bold"), text="Due Date:", padx=5, pady=5)
        #self.lblDDate.place(x=750,y=455)
        #self.txtDDate = DateEntry(self, font=("Poppins", 13), textvariable=DDate, width=38, year=2021, month=7, day=7, bg="#375971", fg="snow")
        #self.txtDDate.place(x=890,y=460)
        
        self.lblRDate = Label(self, font=("Poppins", 12, "bold"), text="Return Date:", padx=5, pady=5)
        self.lblRDate.place(x=750,y=475)
        self.txtRDate = DateEntry(self, font=("Poppins", 13), state="readonly", textvariable=RDate, width=42,year=2021, month=7, day=7, bg="#375971", fg="snow")
        self.txtRDate.place(x=890,y=480)
        
        self.txtSearch = Entry(self, font=("Poppins", 13), textvariable=Search,relief=FLAT, width=40)
        self.txtSearch.place(x=900,y=120)
        
        #### Buttons 
        
        self.btnAddBook = Button(self, text="➕  ADD", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command = addReport)
        self.btnAddBook.place(x=330,y=650)
        self.btnAddBook.config(cursor= "hand2")
        
        self.btnUpdateBook = Button(self, text="⟲  UPDATE", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command = updateReport)
        self.btnUpdateBook.place(x=455,y=650)
        self.btnUpdateBook.config(cursor= "hand2")
        
        self.btnDeleteBook = Button(self, text="➖  DELETE", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command = deleteReport)
        self.btnDeleteBook.place(x=585,y=650)
        self.btnDeleteBook.config(cursor= "hand2")
        
        self.btnclear = Button(self, text="CLEAR", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command = clear)
        self.btnclear.place(x=205,y=650)
        self.btnclear.config(cursor= "hand2")

        self.btnSearchBook = Button(self, text="🔍", font=('Poppins', 13),  bd=0, bg="#90a3b0",
                               command=searchReport)
        self.btnSearchBook.place(x=1270,y=116)
        self.btnSearchBook.config(cursor= "hand2")
        
        self.btnShowallOrder = Button(self, text="SHOW ALL", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0", command = showAll)
        self.btnShowallOrder.place(x=200,y=118)
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
        
        
        label = tk.Label(self, text="History", bg="#90a3b0", font=("Century Gothic", 20))
        label.place(x=200,y=55)
        
        applogo = tk.Label(self, text="🕮", font=("Impact",70),bd=0,
                            bg="grey17",
                            fg="snow",)
        applogo.place(x=40,y=5)
        apptitle = tk.Label(self, text="BOOK RENTAL\nSYSTEM", font=("Impact",19),bd=0,
                            bg="grey17",
                            fg="snow",)
        apptitle.place(x=25,y=130)
        
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
            iExit = tkinter.messagebox.askyesno("Book Rental Sysytem","Do you want to log-out?")
            if iExit > 0:
                controller.show_frame(Login)
                
            
        ## Window Buttons
        
        button1 = tk.Button(self, text="⯀ DASHBOARD",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Dashboard))
        button1.place(x=25,y=230)
        button1.config(cursor= "hand2")

        button2 = tk.Button(self, text="⯀ BOOKS",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Books))
        button2.place(x=12,y=280)
        button2.config(cursor= "hand2")
        
        button3 = tk.Button(self, text="⯀ GENRES",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Genres))
        button3.place(x=15,y=330)
        button3.config(cursor= "hand2")
        
        button4 = tk.Button(self, text="⯀ BORROWER",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Borrowers))
        button4.place(x=21,y=380)
        button4.config(cursor= "hand2")
        
        button5 = tk.Button(self, text="⯀ RENT   ",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Order))
        button5.place(x=10,y=430)
        button5.config(cursor= "hand2")
        
        button6 = tk.Button(self, text="⯀ REPORT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="snow",
                            command=lambda: controller.show_frame(Report))
        button6.place(x=13,y=480)
        button6.config(cursor= "hand2")
        
        button7 =tk.Button(self, text="⯀ HISTORY",font=("Century Gothic",13,"bold"),bd=0,
                            width = 10,
                            bg="grey17",
                            fg="#90a3b0",
                            command=lambda: controller.show_frame(History))
        button7.place(x=17,y=530)
        button7.config(cursor= "hand2")

        button8 = tk.Button(self, text="⯀ LOG-OUT",font=("Century Gothic",13,"bold"),bd=0,
                            width = 12,
                            bg="grey17",
                            fg="snow",
                            command=logout)
        button8.place(x=11,y=580)
        button8.config(cursor= "hand2")
        
        
        
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
        
        self.lblsearchby = Label(self, font=("Poppins", 12),anchor = W, text="SEARCH BY:", width = 72, padx=5, pady=5,bg="#90a3b0")
        self.lblsearchby.place(x=650,y=116)
        
        self.txtSearch = Entry(self, font=("Poppins", 13), textvariable=Search,relief=FLAT, width=40)
        self.txtSearch.place(x=900,y=120)
        
        #### Buttons
                
        self.btnShowallBook = Button(self, text="SHOW ALL", font=('Poppins', 11), height=1, width=10, bd=1, 
                               bg="#90a3b0",command=Refresh)
        self.btnShowallBook.place(x=200,y=118)
        self.btnShowallBook.config(cursor= "hand2")
        
        self.btnSearchBook = Button(self, text="🔍", font=('Poppins', 13),  bd=0, bg="#90a3b0",
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
app.mainloop()

