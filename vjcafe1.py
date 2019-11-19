
from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
import sqlite3
from validate_email import validate_email
import smtplib

with sqlite3.connect('database.db') as db:
    c = db.cursor()
try:
    c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX  NOT NULL,email TEX NOT NULL);')
except:
    pass
db.commit()
db.close()




class main:
    def __init__(self, master):

        self.master = master

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # self.n_reg=StringVar()
        self.n_email = StringVar()
        self.n_email = StringVar()
        #======All images===========
        self.bg_icon=Image.open("bg.png")
        self.bg_icon=self.bg_icon.resize((2000, 1000))
        self.bg_icon=ImageTk.PhotoImage(self.bg_icon)

        self.logo_icon= Image.open("user.png")
        self.logo_icon = self.logo_icon.resize((450,250))
        self.logo_icon = ImageTk.PhotoImage(self.logo_icon)
        self.user_icon = Image.open("username.jpg")
        self.user_icon = self.user_icon.resize((100,50))
        self.user_icon = ImageTk.PhotoImage(self.user_icon)
        self.pass_icon = Image.open("passicon.png")
        self.pass_icon = self.pass_icon.resize((100,50))
        self.pass_icon = ImageTk.PhotoImage(self.pass_icon)
        self.widgets()

    def login(self):

        with sqlite3.connect('database.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            global username1, password1
            username1=self.username.get()
            password1=self.password.get()
            #print(str(username1), str(password1) )
            self.SaleWindow = Toplevel(self.master)
            self.app = Billing(self.SaleWindow)
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):

        with sqlite3.connect('database.db') as db:
            c = db.cursor()

        if self.n_username.get() != ' ' and self.n_password.get() != ' ' and self.n_email.get() != ' ':
            find_user = ('SELECT * FROM user WHERE username = ?')
            c.execute(find_user, [(self.n_username.get())])

            if c.fetchall():
                ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
            else:
                insert = 'INSERT INTO user(username,password,email) VALUES(?,?,?)'
                c.execute(insert, [(self.n_username.get()), (self.n_password.get()), (self.n_email.get())])
                db.commit()

                ms.showinfo('Success!', 'Account Created!')
                self.log()

        else:
            ms.showerror('Error!', 'Please Enter the details.')

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        print("line1")
        self.n_password.set('')
        print("line2")
        self.logf.pack_forget()
        print("line3")
        #self.head['text'] = 'Create Account'
        self.crf.pack()
        print("line4")

    def widgets(self):
        bg_lbl = Label(self.master, image=self.bg_icon).pack()
        self.head=Label(self.master, text="WELCOME TO VJ CAFE", font=("times new roman" , 40, "bold"),fg="red" , bd=10,relief=FLAT).pack()
        #self.head(x=0, y=0, relwidth=1)


        self.logf = Frame(self.master,bg="white")
        self.logf.place(x=500, y=200)


        # PhotoImage(self.logf,file = 'lpu_logo.png')




        logolbl = Label(self.logf, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)

        lbluser = Label(self.logf, text="Username", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white").grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(self.logf, bd="5", textvariable=self.username, relief=GROOVE, font=(" ", 15))
        txtuser.grid(row=1, column=1, padx=20)

        lblpass = Label(self.logf, text="Password", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(self.logf, bd="5", textvariable=self.password, relief=GROOVE, font=(" ", 15)).grid(row=2,
                                                                                                          column=1,
                                                                                                          padx=20)
        btn_log = Button(self.logf, text="LOGIN", width=15, font=("times new roman", 14, "bold"), bg="blue",
                         fg="white",activebackground="red", command=self.login).grid(row=3, column=0)
        btn_create = Button(self.logf, text="NEW USER", width=15, font=("times new roman", 14, "bold"), bg="blue",
                         fg="white",activebackground="red", command=self.cr).grid(row=3, column=1)



        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=3, font=('', 15)).grid(row=0, column=1)

        Label(self.crf, text='Password: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=3, font=('', 15), show='*').grid(row=1, column=1)

        """Label(self.crf,text = 'Reg No.: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_reg,bd = 3,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Gender: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        var = IntVar()
        R1 = Radiobutton(self.crf, text="Male", variable=var, value=1).grid(sticky=W)
        
        R2 = Radiobutton(self.crf, text="Female", variable=var, value=2 ).grid(row=4,column=1)"""


        Label(self.crf, text='Email Id: ', font=('', 15), pady=5, padx=5).grid(row=5,column=0)
        Entry(self.crf, textvariable=self.n_email, bd=3, font=('', 15)).grid(row=5, column=1)

        Button(self.crf, text='Create Account', background='lightgrey', bd=2, font=('', 13), padx=6, pady=6,
               command=self.new_user).grid(row=11, column=0)
        Button(self.crf, text='Go to Login', background='lightgrey', bd=2, font=('', 13), padx=6, pady=6,
               command=self.log).grid(row=11, column=1)

        self.crff = Frame(self.master, padx=10, pady=10)

""""""""" Label(self.crff,text = 'Consignment No: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crff,bd = 3,font = ('',15)).grid(row=0,column=1)
        Label(self.crff,text = 'email no:',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crff,bd = 3,textvariable = self.email11,font = ('',15)).grid(row=1,column=1)
        Button(self.crff,text = 'Track',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.consignment).grid(row=4,column=0)

        self.consi = Frame(self.master,padx =10,pady = 10)

        Label(self.consi,text = ' Product ID:',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Label(self.consi,text =random.randint(565154,99994216) ,font = ('',13),pady=5,padx=5).grid(row=0,column=1)
        L = ['Bag','Colgate','shoe','Redme 2','Jeans','Parrot','Mac','Ipad','Pen','Book','shirt']
        f=random.randint(0,10)
        Label(self.consi,text = 'Product name: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Label(self.consi,text =L[f] ,font = ('',13),pady=5,padx=5).grid(row=1,column=1)
        Label(self.consi,text = 'Product Status: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Label(self.consi,text ='Pending' ,font = ('',13),pady=5,padx=5).grid(row=2,column=1)
        Label(self.consi,font = ('',13), text = 'Thanks for Exploring!').grid(row = 4, column = 0)

        Label(self.consi, text = 'Comments:',font = ('',13)).grid(row = 5, column = 0, padx = 5, sticky = 'sw')
        Entry(self.consi,bd = 3,font = ('',15)).grid(row=5,column=1)

        Button(self.consi,text = 'Back',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.track1).grid(row=6,column=0)




        """


class Price:
    def __init__(self,master):
        self.master=master
        self.master.geometry("600x400+0+0")
        self.master.title("Price List")
        self.frame = Frame(self.master, bg="pink")
        self.frame.pack()
        tops = Frame(self.master, width=1600, height=50, bg="pink", relief=SUNKEN)
        tops.pack(side=TOP)

        roo = Frame(self.master, width=800, height=700, relief=SUNKEN)
        roo.pack(side=LEFT)

        rf = Frame(self.master, width=300, height=700, relief=SUNKEN)
        rf.pack(side=RIGHT)



        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
        lblinfo.grid(row=0, column=2)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries ", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pasta", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="180", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sizzlers", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="300", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cookies", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheesecake", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza", fg="steel blue", anchor=W)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="250", fg="steel blue", anchor=W)
        lblinfo.grid(row=7, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger", fg="steel blue", anchor=W)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="steel blue", anchor=W)
        lblinfo.grid(row=8, column=3)

#class Login:

    """def __init__(self,master):
        self.master=master
        self.master.title("RESTAURANT BILLING SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg='pink')
        self.frame=Frame(self.master,bg="pink")
        self.frame.pack()


        self.Title=Label(self.frame,text="RESTARAUNT",font=('arial',40,'bold'),bg='pink',fg='Cornsilk')
        self.Title.grid(row=0,column=0,columnspan=2,pady=20)
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.LoginFrame1=LabelFrame(self.frame,width=800,height=600,font=('arial',20,'bold'),relief='ridge',text="Login",bd=5)
        self.LoginFrame1.grid(row=1,column=0)
        #self.LoginFrame2 = LabelFrame(self.frame, width=800, height=200, font=('arial', 20, 'bold'), relief='ridge',bd=20 )
        #self.LoginFrame2.grid(row=2, column=0)

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.Username = StringVar()
        self.Password = StringVar()
        lblpass = Label(self.LoginFrame1, font=('arial', '16', 'bold'), text="Password", bd=16, anchor='w')
        lblpass.grid(row=2, column=0)
        txtpass = Entry(self.LoginFrame1, font=('arial', '16', 'bold'), textvariable=self.Password, insertwidth=4, bg='white',
                         justify='right',show="*")
        txtpass.grid(row=2, column=1,pady=20)


        lblUsername = Label(self.LoginFrame1, font=('arial', '16', 'bold'), text="Username", bd=16, anchor='w')
        lblUsername.grid(row=1, column=0)
        txtUsername = Entry(self.LoginFrame1, font=('arial', '16', 'bold'), textvariable=self.Username, insertwidth=4, bg='white',
                         justify='right')
        txtUsername.grid(row=1, column=1,pady=20)

        btnLogin=Button(self.LoginFrame1,text="Login",width=15,font=('freemono', '30', 'bold'),bg="ivory3",command=self.Login_System,fg="black")
        btnLogin.grid(row=3,columnspan=2,pady=8,padx=8)
        "btnReset = Button(self.LoginFrame1, text="Reset", width=15, font=('arial', '30', 'bold'), bg="grey",
                          fg="Cornsilk",command=Reset)
        btnReset.grid(row=3, column=1, pady=20, padx=8)
        btnExit = Button(self.LoginFrame1, text="Exit", width=15, font=('arial', '30', 'bold'), bg="grey",
                          fg="Cornsilk",command=qExit)
        btnExit.grid(row=3, column=2, pady=10, padx=8)"

    def Login_System(self):
        user=str(self.Username.get())
        pas=str(self.Password.get())
        User=dict()
        User={"Disha2706":"12345","RasikaGawande":"2rasika4"}
        if user=="Disha" and pas == "12345":
        #if user in User and pas==User[user]:
            self.Login_Window()
        else:
            tkinter.messagebox.askyesno("INVALID LOGIN","Invalid Login username or password")

            Username.set("")
            Password.set("")



    def Login_Window(self):
        self.SaleWindow=Toplevel(self.master)
        self.app=Billing(self.SaleWindow)"""

class Billing:
    def __init__(self,master):
        self.master=master
        self.master.title("RESTAURANT BILLING SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.bg = Image.open("cafe.jpg")
        self.bg = self.bg.resize((2000, 1000))
        self.bg = ImageTk.PhotoImage(self.bg)

        #self.master.config(bg='pink')
        self.frame=Frame(self.master)

        self.frame.pack()

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
        tops = Frame(self.master, width=1600, height=50, bg="pink", relief=SUNKEN)
        tops.pack(side=TOP)

        lf = Frame(self.master, width=800, height=700, relief=SUNKEN)
        lf.pack(side=LEFT)

        rf = Frame(self.master, width=300, height=700, relief=SUNKEN)
        rf.pack(side=RIGHT)
        bg1_lbl = Label(self.master, image=self.bg).pack()
        heading = Label(tops, font=('Ink Free', 100, 'bold'), text="VJ  Cafe", fg="Purple", bd=10, anchor='w')
        heading.grid(row=0, column=0)

        # -----time----
        localtime = time.asctime(time.localtime(time.time()))

        # ----labelinfo----
        lblinfo = Label(tops, font=('Ink Free', 100, 'bold',), text="VJ Cafe", bd=10, fg="Purple", anchor='w')
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(tops, font=('ariel', 20, 'bold',), text=localtime, fg="Purple", bd=10, anchor='w')
        lblinfo.grid(row=1, column=0)

        # ................buttons.................
        def Ref():
            x = random.randint(200000, 700000)
            randomRef = str(x)
            rand.set(randomRef)

            COF = float(Fries.get())
            COP = float(Pasta.get())
            COD = float(Drinks.get())
            COS = float(Sizzlers.get())
            CO = float(Cookies.get())
            CC = float(Cheesecake.get())
            COPP = float(Pizza.get())
            COB = float(Burger.get())

            CostOfFries = COF * 100
            CostOfDrinks = COD * 50
            CostOfPasta = COP * 180
            CostOfSizzlers = COS * 300
            CostOfCookies = CO * 120
            CostOfCheesecake = CC * 200
            CostOfPizza = COPP * 250
            CostOfBurger = COB * 150

            CostOfMeal = "Rs", str(
                '%.2f' % (CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies+CostOfPizza+CostOfBurger))
            PayTax = ((CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies+CostOfPizza+CostOfBurger) * 0.02)
            Total = (CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies+CostOfPizza+CostOfBurger)

            OverallCost = "Rs", str('%.2f' % (Total + PayTax))

            TaxPaid = "Rs", str('%.2f' % (PayTax))

            Tax.set(TaxPaid)
            TotalCost.set(OverallCost)

        def qExit():
            self.master.destroy()

        def Reset():
            rand.set("")
            Fries.set("0")
            Pasta.set("0")
            Drinks.set("0")
            Sizzlers.set("0")
            Cookies.set("0")
            Cheesecake.set("0")
            Pizza.set("0")
            Burger.set("0")
            Tax.set("")
            TotalCost.set("")

        def Receipt():
            txtReceipt.delete("1.0", END)
            x = random.randint(10903, 609235)
            #randomRef = str(x)
            y="BILL"
            ref=y+str(x)
            #rf.set("BILL"+randomRef)
            txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ref+'\n'+localtime+"\n")
            txtReceipt.insert(END, 'ITEM:\t\t\t' + "Cost of Items\n")
            txtReceipt.insert(END, 'Fries:\t\t\t' + Fries.get() + "\n")
            txtReceipt.insert(END, 'Cheesecake:\t\t\t' + Cheesecake.get() + "\n")
            txtReceipt.insert(END, 'Pizza:\t\t\t' + Pizza.get() + "\n")
            txtReceipt.insert(END, 'Burger:\t\t\t' + Burger.get() + "\n")
            txtReceipt.insert(END, 'Drinks:\t\t\t' + Drinks.get() + "\n")
            txtReceipt.insert(END, 'Pasta:\t\t\t' + Pasta.get() + "\n")
            txtReceipt.insert(END, 'Sizzlers:\t\t\t' + Sizzlers.get() + "\n")
            txtReceipt.insert(END, 'Cookies:\t\t\t' + Cookies.get() + "\n")
            txtReceipt.insert(END, 'Tax:\t\t\t' + Tax.get() + "\n")
            txtReceipt.insert(END, 'Total Cost:\t\t\t' + TotalCost.get() + "\n")
            with sqlite3.connect('database.db') as db:
                c = db.cursor()

            # Find user If there is any take proper action
            find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
            #c.execute(find_user, ['disha22','22222'])

            #result1 = c.fetchall()
            #print(result1[0][2])
            #print(str(username1), str(password1))
            c.execute(find_user,[str(username1), str(password1)])
            result1 = c.fetchall()
            email1(result1[0][2])

        def email1(emailid):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # Next, log in to the server
            server.login("dishacheck123@gmail.com", "2rasika4")

            # Send the mail
            msg = "SENT FROM PYTHON3.7"  # The /n separates the message from the headers
            server.sendmail("dishacheck123@gmail.com", emailid, msg)

        def price():
                #Price=
                app=Price(Toplevel())

        # ..............................................................................

        # --------------------------------------Resturant Information  1------------------------------------------------------------

        rand = StringVar()
        """lblReference = Label(lf,font = ('arial','16','bold'),text="Reference",bd = 16, anchor = 'w')
        lblReference.grid(row=0,column=0)
        txtReference = Entry(lf,font = ('arial','16','bold'),textvariable = rand,bd =10,insertwidth=4,bg ='pink',justify='right')
        txtReference.grid(row=0,column=1)"""

        Fries = StringVar()
        Fries.set("0")
        lblFries = Label(lf, font=('arial', '16', 'bold'), text="Large Fries", bd=16, anchor='w')
        lblFries.grid(row=1, column=0)
        txtFries = Spinbox(lf, from_=0, textvariable=Fries, font=('arial', '16', 'bold'), bg='pink', justify='right',
                           to=1000)
        txtFries.grid(row=1, column=1)

        Pasta = StringVar()
        Pasta.set("0")
        lblVeg = Label(lf, font=('arial', '16', 'bold'), text="Pasta", bd=16, anchor='w')
        lblVeg.grid(row=2, column=0)
        txtVeg = Spinbox(lf, from_=0, textvariable=Pasta, font=('arial', '16', 'bold'), bg='pink', justify='right', to=1000)
        txtVeg.grid(row=2, column=1)
        """font = ('arial','16','bold'),insertwidth=4,,"""

        Sizzlers = StringVar()
        Sizzlers.set("0")
        lblChicken = Label(lf, font=('arial', '16', 'bold'), text="Sizzlers", bd=16, anchor='w')
        lblChicken.grid(row=3, column=0)
        txtChicken = Spinbox(lf, from_=0, textvariable=Sizzlers, font=('arial', '16', 'bold'), bg='pink', justify='right',
                             to=1000)
        txtChicken.grid(row=3, column=1)

        Drinks = StringVar()
        Drinks.set("0")
        lblDrinks = Label(lf, font=('arial', '16', 'bold'), text="Drinks", bd=16, anchor='w')
        lblDrinks.grid(row=3, column=2)
        txtDrinks = Spinbox(lf, from_=0, textvariable=Drinks, font=('arial', '16', 'bold'), bg='pink', justify='right',
                            to=1000)
        txtDrinks.grid(row=3, column=3)

        Pizza = StringVar()
        Pizza.set("0")
        lblDrinks = Label(lf, font=('arial', '16', 'bold'), text="Pizza", bd=16, anchor='w')
        lblDrinks.grid(row=4, column=2)
        txtDrinks = Spinbox(lf, font=('arial', '16', 'bold'), textvariable=Pizza, bd=10, insertwidth=4, bg='pink',
                          justify='right',to=1000)
        txtDrinks.grid(row=4, column=3)

        Burger = StringVar()
        Burger.set("0")
        lblBurger = Label(lf, font=('arial', '16', 'bold'), text="Burger", bd=16, anchor='w')
        lblBurger.grid(row=4, column=0)
        txtBurger = Spinbox(lf, font=('arial', '16', 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg='pink',
                          justify='right',to=1000)
        txtBurger.grid(row=4, column=1)

        Cookies = StringVar()
        Cookies.set("0")
        lblservice = Label(lf, font=('arial', '16', 'bold'), text="Cookies ", bd=16, anchor='w')
        lblservice.grid(row=1, column=2)
        txtservice = Spinbox(lf, from_=0, textvariable=Cookies, font=('arial', '16', 'bold'), bg='pink', justify='right',
                             to=1000)
        txtservice.grid(row=1, column=3)

        Tax = StringVar()
        lblTax = Label(lf, font=('arial', '16', 'bold'), text="Tax", bd=16, anchor='w')
        lblTax.grid(row=5, column=0)
        txtTax = Label(lf, font=('arial', '16', 'bold'), textvariable=Tax, bd=10)
        txtTax.grid(row=5, column=1)

        Cheesecake = StringVar()
        Cheesecake.set("0")
        lblservice = Label(lf, font=('arial', '16', 'bold'), text="Cheesecake ", bd=16, anchor='w')
        lblservice.grid(row=2, column=2)
        txtservice = Spinbox(lf, from_=0, textvariable=Cheesecake, font=('arial', '16', 'bold'), bg='pink', justify='right',
                             to=1000)
        txtservice.grid(row=2, column=3)

        TotalCost = StringVar()
        lblTotalCost = Label(lf, font=('arial', '16', 'bold'), text="Total", bd=16, anchor='w')
        lblTotalCost.grid(row=5, column=2)
        txtTotalCost = Label(lf, font=('arial', '16', 'bold'), textvariable=TotalCost, bd=10)
        txtTotalCost.grid(row=5, column=3)
        # -----------------------------------------------Receipt--------------------------------------------------------------------------------------

        txtReceipt = Text(rf, width=57, height=19, bg="white", bd=4, font=('arial', 12, 'bold'))
        txtReceipt.grid(row=0, column=0)
        # --------------------------Buttons-----------------------------------------------------
        btnprice = Button(lf, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="PRICE",
                          bg="pink",command=price)
        btnprice.grid(row=8, column=0)
        btnTotal = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('arial', '16', 'bold'), width=10, text="Total",
                          bg='pink', command=Ref).grid(row=8, column=1)
        btnReset = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('arial', '16', 'bold'), width=10, text="Reset",
                          bg='pink', command=Reset).grid(row=8, column=2)
        btnExit = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('arial', '16', 'bold'), width=10, text="Exit",
                         bg='pink', command=qExit).grid(row=8, column=4)
        btnReceipt = Button(lf, padx=16, pady=8, bd=16, fg='Black', font=('arial', '16', 'bold'), width=10,
                            text="Receipt", bg='pink', command=Receipt).grid(row=8, column=3)


if __name__=='__main__':
    root=Tk()
    root.title('Login')
    root.geometry('800x750+300+300')
    main(root)

    """" canvas = Canvas(root)
    canvas.pack()
    canvas.config(width=640, height=380)

    line = canvas.create_line(160, 360, 480, 120, fill='blue', width=5)
    canvas.itemconfigure(line, fill='#1abc9c')
    print(canvas.coords(line))
    canvas.coords(line, 0, 0, 320, 240, 640, 0)

    canvas.itemconfigure(line, smooth=True)
    canvas.itemconfigure(line, splinesteps=5)
    canvas.itemconfigure(line, splinesteps=100)
    canvas.delete(line)

    rect = canvas.create_rectangle(160, 120, 480, 360)
    canvas.itemconfigure(rect, fill='#3498db')
    oval = canvas.create_oval(160, 120, 480, 360)
    arc = canvas.create_arc(160, 1, 480, 240)
    canvas.itemconfigure(arc, start=0, extent=180, fill='#1abc9c')
    poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill='#95a5a6')
    text = canvas.create_text(320, 240, text='Python', font=('Courier', 32, 'bold'))

    logo = PhotoImage(file='logo1.png')
    image = canvas.create_image(320, 240, image=logo)

    canvas.lift(text)
    canvas.lower(image)
    canvas.lower(image, text)

    canvas.create_window(320, 60)

    canvas.itemconfigure(rect, tags=('shape'))
    canvas.itemconfigure(oval, tags=('shape', 'round'))
    canvas.itemconfigure('shape', fill='grey')
    print(canvas.gettags(oval))"""
    root.mainloop()



