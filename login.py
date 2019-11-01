import tkinter as tk
from tkinter import *
#from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk


def menu():
    root = Tk()
    root.geometry("1600x800+0+0")
    root.title("Resturant Management System")
    imgroot = Image.open("C:\\Users\\Ayush\\Pictures\\spam\\giphy.gif")
    img = ImageTk.PhotoImage(imgroot)
    root.tk.call('wm', 'iconphoto', root._w, img)

    text_Input = StringVar()
    operator = ""

    tops = Frame(root, width=1600, height=50, bg="pink", relief=SUNKEN)
    tops.pack(side=TOP)

    lf = Frame(root, width=800, height=700, relief=SUNKEN)
    lf.pack(side=LEFT)

    rf = Frame(root, width=300, height=700, relief=SUNKEN)
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

    # ---------calculator----------#
    def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)

    def btnClear():
        global operator
        operator = ""
        text_Input.set("")

    def btnEquals():
        global operator
        sumUp = str(eval(operator))
        text_Input.set(sumUp)
        operator = ""

    # ................buttons.................
    def Ref():
        x = random.randint(200000, 700000)
        randomRef = str(x)
        rand.set(randomRef)

        COF = float(Fries.get())
        COV = float(veg.get())
        COC = float(Chicken.get())
        COD = float(Drinks.get())

        CostOfFries = COF * 100
        CostOfDrinks = COD * 60
        CostOfChickenMeal = COC * 550
        CostOfVegMeal = COV * 300

        CostOfMeal = "Rs", str('%.2f' % (CostOfFries + CostOfDrinks + CostOfChickenMeal + CostOfVegMeal))
        PayTax = ((CostOfFries + CostOfDrinks + CostOfChickenMeal + CostOfVegMeal) * 0.12)
        Total = (CostOfFries + CostOfDrinks + CostOfChickenMeal + CostOfVegMeal)
        Service_crg = ((CostOfFries + CostOfDrinks + CostOfChickenMeal + CostOfVegMeal) / 99)
        OverallCost = "Rs", str('%.2f' % (Total + PayTax + Service_crg))
        service_c = "Rs", str('%.2f' % (Service_crg))
        TaxPaid = "Rs", str('%.2f' % (PayTax))

        service.set(service_c)
        cost.set(CostOfMeal)
        Tax.set(TaxPaid)
        SubTotal.set(CostOfMeal)
        TotalCost.set(OverallCost)

    def qExit():
        root.destroy()

    def Reset():
        rand.set("")
        Fries.set("0")
        veg.set("0")
        Drinks.set("0")
        Chicken.set("0")
        cost.set("")
        service.set("")
        Tax.set("")
        SubTotal("")
        TotalCost("")

    # ..............................................................................

    txtDisplay = Entry(rf, font=('arial', 20, 'bold'), textvariable=text_Input, insertwidth=4, bd=20, bg="light pink",
                       justify="right")
    txtDisplay.grid(columnspan=4)

    btn1 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="1",
                  command=lambda: btnClick(1)).grid(row=2, column=0)
    btn2 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="2",
                  command=lambda: btnClick(2)).grid(row=2, column=1)
    btn3 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="3",
                  command=lambda: btnClick(3)).grid(row=2, column=2)
    Addition = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="+",
                      command=lambda: btnClick("+")).grid(row=2, column=3)

    btn4 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="4",
                  command=lambda: btnClick(4)).grid(row=3, column=0)
    btn5 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="5",
                  command=lambda: btnClick(5)).grid(row=3, column=1)
    btn6 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="6",
                  command=lambda: btnClick(6)).grid(row=3, column=2)
    Subtraction = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="-",
                         command=lambda: btnClick("-")).grid(row=3, column=3)

    btn7 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="7",
                  command=lambda: btnClick(7)).grid(row=4, column=0)
    btn8 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="8",
                  command=lambda: btnClick(8)).grid(row=4, column=1)
    btn9 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="9",
                  command=lambda: btnClick(9)).grid(row=4, column=2)
    Multiplication = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="",
                            command=lambda: btnClick("")).grid(row=4, column=3)

    btn0 = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="0",
                  command=lambda: btnClick(0)).grid(row=5, column=0)
    btnClear = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="C",
                      command=btnClear).grid(row=5, column=1)
    btnEquals = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="=",
                       command=btnEquals).grid(row=5, column=2)
    btnDivision = Button(rf, padx=16, pady=16, bd=8, bg='light pink', font=('arial', 20, 'bold'), text="/",
                         command=lambda: btnClick("/")).grid(row=5, column=3)
    # btn7 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "7", command = lambda:btnClick(7)).grid(row=4,column=0)

    # --------------------------------------Resturant Information  1------------------------------------------------------------

    rand = StringVar()
    lblReference = Label(lf, font=('arial', '16', 'bold'), text="Reference", bd=16, anchor='w')
    lblReference.grid(row=0, column=0)
    txtReference = Entry(lf, font=('arial', '16', 'bold'), textvariable=rand, bd=10, insertwidth=4, bg='pink',
                         justify='right')
    txtReference.grid(row=0, column=1)

    Fries = StringVar()
    Fries.set("0")
    lblFries = Label(lf, font=('arial', '16', 'bold'), text="Large Fries", bd=16, anchor='w')
    lblFries.grid(row=1, column=0)
    txtFries = Entry(lf, font=('arial', '16', 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg='pink',
                     justify='right')
    txtFries.grid(row=1, column=1)

    veg = StringVar()
    veg.set("0")
    lblVeg = Label(lf, font=('arial', '16', 'bold'), text="Veg Meal", bd=16, anchor='w')
    lblVeg.grid(row=2, column=0)
    txtVeg = Entry(lf, font=('arial', '16', 'bold'), textvariable=veg, bd=10, insertwidth=4, bg='pink', justify='right')
    txtVeg.grid(row=2, column=1)

    Chicken = StringVar()
    Chicken.set("0")
    lblChicken = Label(lf, font=('arial', '16', 'bold'), text="Chicken Meal", bd=16, anchor='w')
    lblChicken.grid(row=3, column=0)
    txtChicken = Entry(lf, font=('arial', '16', 'bold'), textvariable=Chicken, bd=10, insertwidth=4, bg='pink',
                       justify='right')
    txtChicken.grid(row=3, column=1)

    Drinks = StringVar()
    Drinks.set("0")
    lblDrinks = Label(lf, font=('arial', '16', 'bold'), text="Drinks", bd=16, anchor='w')
    lblDrinks.grid(row=4, column=0)
    txtDrinks = Entry(lf, font=('arial', '16', 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg='pink',
                      justify='right')
    txtDrinks.grid(row=4, column=1)

    # --------------------------------------Resturant Information  2-------------------------------------
    cost = StringVar()
    lblcost = Label(lf, font=('arial', '16', 'bold'), text="Cost of Meal", bd=16, anchor='w')
    lblcost.grid(row=0, column=2)
    txtcost = Entry(lf, font=('arial', '16', 'bold'), textvariable=cost, bd=10, insertwidth=4, bg='pink',
                    justify='right')
    txtcost.grid(row=0, column=3)

    service = StringVar()
    lblservice = Label(lf, font=('arial', '16', 'bold'), text="Service Cost ", bd=16, anchor='w')
    lblservice.grid(row=1, column=2)
    txtservice = Entry(lf, font=('arial', '16', 'bold'), textvariable=service, bd=10, insertwidth=4, bg='pink',
                       justify='right')
    txtservice.grid(row=1, column=3)

    Tax = StringVar()
    lblTax = Label(lf, font=('arial', '16', 'bold'), text="Tax", bd=16, anchor='w')
    lblTax.grid(row=2, column=2)
    txtTax = Entry(lf, font=('arial', '16', 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg='pink', justify='right')
    txtTax.grid(row=2, column=3)

    SubTotal = StringVar()
    lblSubTotal = Label(lf, font=('arial', '16', 'bold'), text="SubTotal", bd=16, anchor='w')
    lblSubTotal.grid(row=3, column=2)
    txtSubTotal = Entry(lf, font=('arial', '16', 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg='pink',
                        justify='right')
    txtSubTotal.grid(row=3, column=3)

    TotalCost = StringVar()
    lblTotalCost = Label(lf, font=('arial', '16', 'bold'), text="TotalCost", bd=16, anchor='w')
    lblTotalCost.grid(row=4, column=2)
    txtTotalCost = Entry(lf, font=('arial', '16', 'bold'), textvariable=TotalCost, bd=10, insertwidth=4, bg='pink',
                         justify='right')
    txtTotalCost.grid(row=4, column=3)
    # --------------------------Buttons-----------------------------------------------------
    btnTotal = Button(lf, padx=16, pady=8, bd=16, fg='Black', font=('arial', '16', 'bold'), width=10, text="Total",
                      bg='pink', command=Ref).grid(row=7, column=1)
    btnReset = Button(lf, padx=16, pady=8, bd=16, fg='Black', font=('arial', '16', 'bold'), width=10, text="Reset",
                      bg='pink', command=Reset).grid(row=7, column=2)
    btnExit = Button(lf, padx=16, pady=8, bd=16, fg='Black', font=('arial', '16', 'bold'), width=10, text="Exit",
                     bg='pink', command=qExit).grid(row=7, column=3)

    root.mainloop()
    #-----------------------------------------

    m = tk.Tk()

    # def hello():
    # return messagebox.showinfo("welcome", "HELLO")

    name = tk.Label(m, text='username').grid(row=0, column=0)
    password = tk.Label(m, text='password').grid(row=1, column=0)
    name1 = tk.Entry(m).grid(row=0, column=1)
    pass1 = tk.Entry(m).grid(row=1, column=1)
    submit = tk.Button(m, text='submit', activebackground='blue', bg='green', command=menu).grid(row=2, column=0)

    m.mainloop()