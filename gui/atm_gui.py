from distutils import command
from tkinter import *
from locale import currency
import locale
import time

window = Tk()
window.title('ATM')
window.attributes('-fullscreen',True)



class Customer:
    def __init__(self, name, age, balance):
        self.name = name        
        self.age = age
        self.balance = balance



customers = [Customer('Amanda Keller', 22, 10000000.00),Customer('Will Orme', 23, 10000000.00)
,Customer('Steve Orme', 26, 25.00)]  


def withdraw():
    for customer in customers:

        q = input ('Enter amount to withdraw: ')
        new_balance = customer.balance - float(q)
        print('Withdrawing cash...')
        time.sleep(3)
        if float(q) > customer.balance:
            print ('Insufficient funds')
            continue
        else: 
            print('Your balance is now {}'.format(currency(float(new_balance))))
            break


def deposit():
    for customer in customers:
    
        q = input ('Enter amount to deposit: ')
        new_balance = customer.balance + float(q)
        print('Adding funds to your account...')
        time.sleep(3)
        if float(q) <= 0:
            print('Must deposit amount greater than 0')
            continue
        else:
            print('Your balance is now {}'.format(currency(float(new_balance))))
            break

l = Label(window, text='Customer Name',font=('Helvetica',28))
l.pack()
l.place(x=600,y=100)


e = Entry(window, textvariable=customers ,bg='white', fg='black')
e.place(x=600, y=200)


def acctInfo():
   
    for customer in customers:

        if e.get() == customer.name:
            response = Label(window, text='{}, your current balance is {}'.format(customer.name, currency(float(customer.balance))))
            response.place(x=600,y=230)
            break
        else:
            response2 = Label(window, text='Name does not match existing account')
            response2.place(x=600,y=230)
            break
    



header = Label(window, text='Orme Bank ATM',font=('Helvetica',32),justify=CENTER)
header.pack()

getAcct = Button(window, text='Get Account Info', command=acctInfo)
getAcct.place(x=600,y=300)

wb = Button(window, text='Withdraw', font=('Helvetica',24), command=withdraw)

db = Button(window, text='Deposit', font=('Helvetica',24), command=deposit)





window.mainloop()