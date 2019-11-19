from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root=Tk()
    app=Login(root)
    root.mainloop()



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

        #rf = Frame(self.master, width=300, height=700, relief=SUNKEN)
        #rf.pack(side=RIGHT)



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

class Login:
    def __init__(self,master):
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
        """btnReset = Button(self.LoginFrame1, text="Reset", width=15, font=('arial', '30', 'bold'), bg="grey",
                          fg="Cornsilk",command=Reset)
        btnReset.grid(row=3, column=1, pady=20, padx=8)
        btnExit = Button(self.LoginFrame1, text="Exit", width=15, font=('arial', '30', 'bold'), bg="grey",
                          fg="Cornsilk",command=qExit)
        btnExit.grid(row=3, column=2, pady=10, padx=8)"""

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
        self.app=Billing(self.SaleWindow)

class Billing:
    def __init__(self,master):
        self.master=master
        self.master.title("RESTAURANT BILLING SYSTEM")
        self.master.geometry("1600x800+0+0")
        #self.master.config(bg='pink')
        self.frame=Frame(self.master,bg="pink")
        self.frame.pack()

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
        tops = Frame(self.master, width=1600, height=50, bg="pink", relief=SUNKEN)
        tops.pack(side=TOP)

        lf = Frame(self.master, width=800, height=700, relief=SUNKEN)
        lf.pack(side=LEFT)

        rf = Frame(self.master, width=300, height=700, relief=SUNKEN)
        rf.pack(side=RIGHT)

        heading = Label(tops, font=('arial', 50, 'bold'), text="Resturant Management Systems", fg="black", bd=10,
                        anchor='w')
        heading.grid(row=0, column=0)

        # -----time----
        localtime = time.asctime(time.localtime(time.time()))

        # ----labelinfo----
        lblinfo = Label(tops, font=('ariel', 50, 'bold',), text="Restaurant Management System", bd=10, fg="blue",
                        anchor='w')
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(tops, font=('ariel', 20, 'bold',), text=localtime, fg="blue", bd=10, anchor='w')
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

            CostOfFries = COF * 100
            CostOfDrinks = COD * 50
            CostOfPasta = COP * 180
            CostOfSizzlers = COS * 300
            CostOfCookies = CO * 120
            CostOfCheesecake = CC * 200

            CostOfMeal = "Rs", str(
                '%.2f' % (CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies))
            PayTax = ((CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies) * 0.02)
            Total = (CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies)

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
            Tax.set("")
            TotalCost.set("")

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

        """Pizza = StringVar()
        Pizza.set("0")
        lblDrinks = Label(lf,font = ('arial','16','bold'),text="Pizza",bd = 16, anchor = 'w')
        lblDrinks.grid(row=0,column=2)
        txtDrinks= Entry(lf,font = ('arial','16','bold'),textvariable = Pizza,bd =10,insertwidth=4,bg ='pink',justify='right')
        txtDrinks.grid(row=0,column=3)"""

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
        # --------------------------Buttons-----------------------------------------------------
        btnprice = Button(lf, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="PRICE",
                          bg="pink",command=price)
        btnprice.grid(row=8, column=0)
        btnTotal = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('arial', '16', 'bold'), width=10, text="Total",
                          bg='pink', command=Ref).grid(row=8, column=1)
        btnReset = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('arial', '16', 'bold'), width=10, text="Reset",
                          bg='pink', command=Reset).grid(row=8, column=2)
        btnExit = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('arial', '16', 'bold'), width=10, text="Exit",
                         bg='pink', command=qExit).grid(row=8, column=3)


if __name__=='__main__':
    main()
