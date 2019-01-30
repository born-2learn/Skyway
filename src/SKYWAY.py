import sys
import math
from random import *
from tkinter import *
import time
from tkMessageBox import *

from .gmail import *
from .otp_gmail import *
import .read_resort_details


def exit_paid():
    paid_win.destroy()


def exit_func():
    rate_win.destroy()


def tulip_destroy():
    tulip_window.destroy()


def presidency_destroy():
    presidency_window.destroy()


def wonderla_destroy():
    wonder_window.destroy()


def clubcabana_destroy():
    clubcabana_window.destroy()


def elegant_destroy():
    elegant_window.destroy()


def otp_enter_func(INTEGER):
    # 1-NORMAL
    # 2-WHEN WRONG-RESEND
    otp = send_mail_otp(INTEGER, email)
    global otp
    print
    otp, 'skyway'
    message = 'OTP Sent to ' + email
    showinfo(message, 'Please type the OTP in the Terminal to Create your SKYWAY ACCOUNT')
    otp_enter = int(raw_input('Enter the OTP from your email: '))

    global otp_enter
    if (otp_enter == otp):
        Successful(1)
    else:
        print
        'Wrong OTP entered'
        print
        'For Security Purposes, please Redo the process\
from the beginning.'


def rating():
    global rate_win
    paid_win.destroy()
    rate_win = Tk()
    rate_win.title("Rating")
    l = Label(rate_win, text="")
    l.config(font=("Courier", 22))
    l.pack()
    l = Label(rate_win, text="Please enter the number of stars with which you would like to rate us")
    l.config(font=("Courier", 20))
    l.pack()
    v = StringVar()

    e = Entry(rate_win, textvariable=v)
    e.pack()
    b = Button(rate_win, text='EXIT', command=exit_func)
    b.pack()
    rate_win.mainloop()


def paid_1():
    pay_win.destroy()
    r = Tk()
    global r
    r.geometry('1600x900')
    l = Label(r, text='PLEASE WAIT REDIRECTING YOU TO PAYMENT GATEWAY....')
    l.config(font=("Courier", 28))
    l.place(x=0, y=0)

    b = Button(r, text='click to proceed', command=paid, height=2, width=40, fg='white', bg='black')
    b.config(font=("Courier", 15))
    b.place(x=600, y=80)
    r.mainloop()


def paid():
    global paid_win
    r.destroy()
    paid_win = Tk()
    paid_win.title('Payment Successful')
    paid_win.geometry('1500x700')
    print
    print
    print
    print
    'Please wait while we Complete the Transaction...'
    send_mail_payment(final_amt, email)

    paid_win.configure(background='White')
    l = Label(paid_win, text='CONGRATULATIONS!!!!')
    l.config(font=("Courier", 40))
    l.place(x=600, y=0)

    l = Label(paid_win, text='You have sucessfully made your payment')
    l.config(font=("Courier", 28))
    l.place(x=450, y=80)

    b = Button(paid_win, text='Rate us', command=rating, height=2, width=40, fg='white', bg='black')
    b.config(font=("Courier", 15))
    b.place(x=600, y=160)

    l = Label(paid_win, text='Thanks for using skyway \n Hope to see you again')
    l.config(font=("Courier", 28))
    l.place(x=450, y=240)

    b = Button(paid_win, text='EXIT', command=exit_paid, height=2, width=40, fg='white', bg='black')
    b.config(font=("Courier", 15))
    b.place(x=600, y=320)

    paid_win.mainloop()


def payment():
    global pay_win
    bill_win.destroy()
    pay_win = Tk()
    f = '''    PAYMENTS
       How would you like to make your payment?
               '''
    l = Label(pay_win, text=f)
    l.config(font=("Courier", 15))
    l.pack()

    b = Button(pay_win, text='Online Banking', command=paid_1)
    b.config(font=("Courier", 12))
    b.pack()
    b = Button(pay_win, text='Credit/Debit Card', command=paid_1)
    b.config(font=("Courier", 12))
    b.pack()
    b = Button(pay_win, text='PayTM', command=paid_1)
    b.config(font=("Courier", 12))
    b.pack()
    b = Button(pay_win, text='PhonePE', command=paid_1)
    b.config(font=("Courier", 12))
    b.pack()
    b = Button(pay_win, text='Ola_Money', command=paid_1)
    b.config(font=("Courier", 12))
    b.pack()


def bill_calc():
    global no_of_passengers
    amt = no_of_passengers * a
    global amt
    d_percent = '10%'
    global d_percent
    discount = amt * 0.1
    global discount
    final_amt = amt - discount
    global final_amt


def bill():
    bill_calc()
    bill_win = Tk()
    global bill_win
    bill_win.geometry('1500x700')
    l = Label(bill_win, text='SKYWAY')
    l.config(font=("Courier", 35))
    l.place(x=600)
    f = 'Resort Booking Invoice ...' + 'INVOICE No ' + str(randint(1, 9))
    l = Label(bill_win, text=f)
    l.config(font=("Courier", 24))
    l.place(x=360, y=80)
    l = time.localtime()
    f1 = 'Date: ' + str(l[2]) + '/' + str(l[1]) + '/' + str(l[0])
    l = Label(bill_win, text=f1)
    l.config(font=("Courier", 18))
    l.place(y=160, x=960)
    f1 = '7th Floor Raheja Towers'
    f2 = 'MG road,Bangalore'
    f3 = '080-28882973'
    f4 = 'info@skyway.com'
    l = Label(bill_win, text=f1)
    l.config(font=("Courier", 18))
    l.place(y=240, x=0)
    l = Label(bill_win, text=f2)
    l.config(font=("Courier", 18))
    l.place(y=270, x=0)
    l = Label(bill_win, text=f3)
    l.config(font=("Courier", 18))
    l.place(y=300, x=0)
    l = Label(bill_win, text=f4)
    l.config(font=("Courier", 18))
    l.place(y=330, x=0)
    l = Label(bill_win, text='Bill to:')
    l.config(font=("Courier", 21))
    l.place(y=360, x=0)
    l = Label(bill_win, text=name)
    l.config(font=("Courier", 18))
    l.place(y=400, x=140)
    g = 'Phone:' + str(phone)
    l = Label(bill_win, text=g)
    l.config(font=("Courier", 18))
    l.place(y=430, x=140)
    g = 'EMAIL:' + email
    l = Label(bill_win, text=g)
    l.config(font=("Courier", 18))
    l.place(y=460, x=140)
    l = Label(bill_win, text='Resort booked')
    l.config(font=("Courier", 18, 'bold'))
    l.place(y=490, x=0)
    l = Label(bill_win, text=res)
    l.config(font=("Courier", 16))
    l.place(y=520, x=0)
    l = Label(bill_win, text='No. of passengers')
    l.config(font=("Courier", 18, 'bold'))
    l.place(y=490, x=400)
    l = Label(bill_win, text=no_of_passengers)
    l.config(font=("Courier", 18))
    l.place(y=520, x=400)
    l = Label(bill_win, text='Price')
    l.config(font=("Courier", 18, 'bold'))
    l.place(y=490, x=670)
    n = 'Rs.' + str(a)
    l = Label(bill_win, text=n)
    l.config(font=("Courier", 18))
    l.place(y=520, x=670)
    l = Label(bill_win, text='Amount ')
    l.config(font=("Courier", 18, 'bold'))
    l.place(y=490, x=800)

    l = Label(bill_win, text=amt)
    l.config(font=("Courier", 18))
    l.place(y=520, x=800)
    f = 'Subtotal:' + str(amt)
    l = Label(bill_win, text=f)
    l.config(font=("Courier", 18))
    l.place(y=550, x=1000)
    f = 'Discount:' + ' 10' + '%'
    l = Label(bill_win, text=f)
    l.config(font=("Courier", 18))
    l.place(y=580, x=1000)
    f = 'Final price:Rs.' + str(final_amt)
    l = Label(bill_win, text=f)
    l.config(font=("Courier", 18, 'bold'))
    l.place(y=620, x=1000)
    b = Button(bill_win, text='Make Payment', command=payment, height=2, width=40, fg='white', bg='black')
    b.config(font=("Courier", 11))
    b.place(y=640, x=560)

    print
    'Please wait for a while...'
    send_mail_invoice(name, res, date, a, no_of_passengers, amt, discount, d_percent, final_amt, email)
    aaa = 'We have sent the invoice to ' + email + '. Please check your email .'
    showinfo('Important information', aaa)
    print
    print
    print
    print
    print
    print
    '          SKYWAY RESORT BOOKING'
    print
    '                INVOICE'
    print
    print
    'Name: ', name
    print
    'Resort booked: ', res
    print
    'Date: ', date
    print
    'Cost of 1 day stay per person=Rs.', a
    print
    'Number of passengers visiting', res, ':', no_of_passengers
    print
    'Subtotal: Rs.', amt
    print
    'Discount Applied: Rs.', discount
    print
    'Discount %: ', d_percent
    print
    '------------------------'
    print
    'Final Amount= Rs.', final_amt
    print
    '------------------------'

    time.sleep(2)
    bill_win.mainloop()


def check_time(k):
    re = 0
    k_yr = k[2];
    k_month = k[1];
    k_day = k[0]
    t = time.localtime()
    t_yr = t[0];
    t_month = t[1];
    t_day = t[2]

    if (k_yr > (t_yr + 1)):
        re = 1
    if (k_yr == t_yr):
        if (k_month < t_month):
            re = 2
    if (k_yr == t_yr):
        if (k_month == t_month):
            if (k_day < t_day):
                re = 2
    return re


def date_check():
    d = eval(raw_input('Date: '))
    stat = check_time(d)
    if (stat == 1):
        print
        'Bookings can be done only till 2018 for now'
        print
        'please Enter a date which is valid'
        date_check()
    if (stat == 2):
        print
        'Please enter a valid Date'
        date_check()
    return d


def phone_check():
    phone = int(raw_input('Enter your Phone Number: '))
    if (phone < 1000000000 or phone > 9999999999):
        print
        'The mobile number is invalid , Plaese enter a valid Mobile Number.'
        phone_check()
    return phone


def email_check():
    email = raw_input('Enter your E-Mail Address: ')
    if ('@' not in email or '.' not in email):
        print
        'Please enter a valid email id'
        email_check()
    return email


def no_of_passengers_func():
    no_of_passengers = int(raw_input('Enter the number of passengers who will be visiting'))
    global no_of_passengers
    if no_of_passengers < 1 or no_of_passengers > 10:
        print
        'The Minimum number of Visitors is 1 and the maximum is 10'
        no_of_passengers_func()


def customer_details(integer):
    if (integer == 1 or integer == 2):
        name = raw_input('Enter your Name:')
        global name
        phone = phone_check()
        global phone
        email = email_check()
        global email
        k = [name, phone, email]
        counter = 0
        pin = 1000
        global dict1
        # File operation to change the counter value to generate unique PIN.
        try:
            c = int(open('counter.txt', 'r').read())

            f = open('counter.txt', 'w')
            counter = c + 1
            counter = str(counter)
            f.write(counter)
            f.close()
            pin = c + 1000  # generating unique PIN

        except IOError:
            print
            'Error Opening  File'
        except EOFError:
            print
            'Reached end of file'
        if (integer == 1):

            try:  # File operation to store member details in Database.
                f = open('database.txt', 'a')
                details = str(pin) + ' ' + str(name) + ' ' + str(phone) + ' ' + str(email) + '\n'
                f.write(details)
                f.close()
            except IOError:
                print
                'File Not Found.'
        if (integer == 1):
            otp_enter_func(1)
            if (otp_enter == otp):
                Successful(1)
            else:
                otp_enter_func(2)

    if (integer == 3 or integer == 2):
        # 3 for already a member
        # 2 for without membership
        # 1 for becoming member
        no_of_passengers = int(raw_input('Enter the number of passengers who will be visiting the resort: '))
        global no_of_passengers
        print
        'Enter the date when you would like to go'
        print
        'Please enter the date in this format: [DD,MM,YYYY]'
        date = date_check()  # For checking if the date entered is valid.
        global date
    bill()


def without_membership():
    intermediate_window.destroy()
    showinfo('Important Information',
             'You have opted for continuing without membership. Please use the Terminal for filling up the Details.')
    customer_details(2)


def ch_1():
    ch = int(raw_input('Enter 1 to Continue: '))
    if (ch == 1):
        customer_details(3)
    else:
        print
        'Please Enter 1'
        ch_1()


def Successful(integer):
    # 1-new customer
    # 2--old customer
    abc = 'Success - Congratulations ' + name
    if (integer == 1):
        abc1 = 'You have Successfully Created your Account.An email has been sent to ' + email + ' with the required details.Please use the Terminal to Continue.'
        send_mail_reg(name, phone, email)
        showinfo(abc, abc1)
    if (integer == 2):
        abc2 = 'We have successfully verified your details. An email has been sent to ' + email + ' with the required details'
        send_mail_member(name, phone, email)
        showinfo(abc, abc2)

    ch_1()


def membership():
    intermediate_window.destroy()
    showinfo("Terminal Used Further on",
             'Please use the Python Terminal for entering the details.Sorry for the inconvenience. We are fixing this shortly')
    customer_details(1)


def login_accept():
    password = v1.get()
    pin_window.destroy()
    print
    password
    # return pin
    condition = False
    try:
        f1 = open('database.txt', 'r')
        for i in range(15):
            line_from_file = f1.readline()
            k = line_from_file.split()
            if (password == k[0]):
                condition = True
                name = k[1]
                global name
                phone = k[2]
                global phone
                email = k[3]
                global email
                break
    except EOFError:
        pass

    '''members={'1000':['Syed Farhan Ahmad','9988856567','farhan.tuba@gmail.com'],'1001':['Nikhil Nair','9765876543','nikhilnicky972@gmail.com']}
    kk=0
    details=[x for x in range(2)]
    for i in members:
           if password==i:
                  kk=1
                  name=members[i][0]
                  global name
                  phone=members[i][1]
                  global phone
                  email=members[i][2]
                  global email'''

    if condition:
        Successful(2)

    else:

        root = Tk()

        l = Label(root, text='Failed to sign in :(')
        l.config(font=("Courier", 30))

        l.pack()

        l = Label(root, text='Do you want to continue without Membership?')
        l.pack()
        b = Button(root, text='Proceed without Membership', command=without_membership)
        b.pack()
        b1 = Button(root, text='Become Member of SKYWAY', command=membership)
        b1.pack()
        root.mainloop()


def pin():
    interested_window.destroy()
    # showinfo('Important Information','Please use the Terminal for entering your 4 digit unique ID')
    # password=raw_input('Enter your four digit unique ID:')

    global pin_window

    global v1
    pin_window = Tk()
    pin_window.title('LogIn')
    pin_window.geometry('600x400')
    v1 = StringVar()

    l = Label(pin_window, text='LogIn')
    l.config(font=("Courier", 30))
    l.pack()

    k = Label(pin_window, text="PLease enter your 4 digit PIN:")

    k.place(x=0, y=40)

    pin = Entry(pin_window, textvariable=v1)

    pin.pack()

    b = Button(pin_window, text='Submit', command=login_accept)
    # b.config(font=("Courier",17))
    b.pack()
    pin_window.mainloop()
    password = login_accept()


def intermediate():
    global intermediate_window
    intermediate_window = Tk()
    interested_window.destroy()
    intermediate_window.geometry('600x400')
    l = Label(intermediate_window, text='Do you want to continue without Membership?')
    l.pack()
    b = Button(intermediate_window, text='Proceed without Membership', command=without_membership)
    b.pack()
    b1 = Button(intermediate_window, text='Become Member of SKYWAY', command=membership)
    b1.pack()
    intermediate_window.mainloop()


def interested():
    global interested_window
    resorts.destroy()
    if (res == 'MAGNIFICIENT TULIPS RESORTS'):
        tulip_window.destroy()

    if (res == 'WONDERLA AMUSEMENT PARK'):
        wonder_window.destroy()
    if (res == 'CLUBCABANA RESORTS'):
        clubcabana_window.destroy()
    if (res == 'PRESIDENCY RESORTS'):
        presidency_window.destroy()
    if (res == 'ELEGANT FANTACIES RESORTS'):
        elegant_window.destroy()
    interested_window = Tk()

    l = Label(interested_window, text='Are You a Member of SKYWAY?')
    l.config(font=("Courier", 30))
    l.pack()

    b = Button(interested_window, text='Yes', command=pin)
    b.config(font=("Courier", 17))
    b.pack()
    b = Button(interested_window, text='NO', command=intermediate)
    b.config(font=("Courier", 17))
    b.pack()


def tulip():
    a = 1000;
    global a
    res = 'MAGNIFICIENT TULIPS RESORTS'
    global res
    global tulip_window

    tulip_window = Tk()

    f = '''__________WELCOME TO MAGNIFICIENT TULIPS RESORTS______________'''
    l = Label(tulip_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()
    f = read_resort_details.read()
    l = Label(tulip_window, text=f)
    l.config(font=("Courier", 12))
    l.pack()

    f = '''THE PRICE OF STAY IN THIS RESORT IS RS.1000/-'''
    l = Label(tulip_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()

    interested_b = Button(tulip_window, text='INTERESTED', command=interested)
    interested_b.config(font=("Courier", 17))
    interested_b.pack()

    not_int_b = Button(tulip_window, text='NOT INTERESTED', command=tulip_destroy)
    not_int_b.config(font=("Courier", 17))
    not_int_b.pack()

    '''exit_b=Button(tulip_window,text='INTERESTED')
    exit_b.config(font=("Courier",17)).pack()'''


def wonderla():
    a = 1750
    global a
    res = 'WONDERLA AMUSEMENT PARK'
    global res
    global wonder_window

    wonder_window = Tk()

    f = '''__________WELCOME TO WONDERLA AMUSEMENT PARK______________'''
    l = Label(wonder_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()
    f = read_resort_details.read()
    l = Label(wonder_window, text=f)
    l.config(font=("Courier", 12))
    l.pack()

    f = '''THE PRICE OF STAY IN THIS RESORT IS RS.1750/-'''
    l = Label(wonder_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()

    interested_b = Button(wonder_window, text='INTERESTED', command=interested)
    interested_b.config(font=("Courier", 17))
    interested_b.pack()

    not_int_b = Button(wonder_window, text='NOT INTERESTED', command=wonderla_destroy)
    not_int_b.config(font=("Courier", 17))
    not_int_b.pack()

    '''exit_b=Button(wonder_window,text='INTERESTED')
    exit_b.config(font=("Courier",17)).pack()'''


def club():
    a = 1500
    global a
    res = 'CLUBCABANA RESORTS'
    global res
    global clubcabana_window

    clubcabana_window = Tk()

    f = '''__________WELCOME TO CLUBCABANA RESORTS______________'''
    l = Label(clubcabana_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()
    f = read_resort_details.read()
    l = Label(clubcabana_window, text=f)
    l.config(font=("Courier", 12))
    l.pack()

    f = '''THE PRICE OF STAY IN THIS RESORT IS RS.1500/-'''
    l = Label(clubcabana_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()

    interested_b = Button(clubcabana_window, text='INTERESTED', command=interested)
    interested_b.config(font=("Courier", 17))
    interested_b.pack()

    not_int_b = Button(clubcabana_window, text='NOT INTERESTED', command=clubcabana_destroy)
    not_int_b.config(font=("Courier", 17))
    not_int_b.pack()

    '''exit_b=Button(clubcabana_window,text='INTERESTED')
    exit_b.config(font=("Courier",17)).pack()'''


def pres():
    a = 1200
    global a
    res = 'PRESIDENCY RESORTS'
    global res
    global presidency_window

    presidency_window = Tk()

    f = '''__________WELCOME TO PRESIDENCY RESORTS______________'''
    l = Label(presidency_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()
    f = read_resort_details.read()
    l = Label(presidency_window, text=f)
    l.config(font=("Courier", 12))
    l.pack()

    f = '''THE PRICE OF STAY IN THIS RESORT IS RS.1200/-'''
    l = Label(presidency_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()

    interested_b = Button(presidency_window, text='INTERESTED', command=interested)
    interested_b.config(font=("Courier", 17))
    interested_b.pack()

    not_int_b = Button(presidency_window, text='NOT INTERESTED', command=presidency_destroy)
    not_int_b.config(font=("Courier", 17))
    not_int_b.pack()

    '''exit_b=Button(presidency_window.text='INTERESTED')
    exit_b.config(font=("Courier",17)).pack()'''


def elegant():
    a = 2000
    global a
    res = 'ELEGANT FANTACIES RESORTS'
    global res
    global elegant_window

    elegant_window = Tk()

    f = '''__________WELCOME TO ELEGANT FANTACIES RESORTS______________'''
    l = Label(elegant_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()
    f = read_resort_details.read()
    l = Label(elegant_window, text=f)
    l.config(font=("Courier", 12))
    l.pack()

    f = '''THE PRICE OF STAY IN THIS RESORT IS RS.2000/-'''
    l = Label(elegant_window, text=f)
    l.config(font=("Courier", 25))
    l.pack()

    interested_b = Button(elegant_window, text='INTERESTED', command=interested)
    interested_b.config(font=("Courier", 17))
    interested_b.pack()

    not_int_b = Button(elegant_window, text='NOT INTERESTED', command=elegant_destroy)
    not_int_b.config(font=("Courier", 17))
    not_int_b.pack()

    '''exit_b=Button(elegant_window.text='INTERESTED')
    exit_b.config(font=("Courier",17)).pack()'''


def resorts():
    global resorts
    logo_window.destroy()
    resorts = Tk()
    resorts.configure(background='White')

    f = '''           ____We are  recognised by Ministry of Tourism, Govt. of India as Inbound Tour Operator____
---We have our Head Office in Bangalore and Registered office in Mysore, Karnataka and branches/associate offices  India.---  
        We are in travel business for last 20 years having management with travel trade experience for 28 years. 
 IATA Accredited, Active Member of Indian Association of Tour Operators (IATO) & Travel Agent Federation of India (TAFI)
                              ++++An ISO 9001-2008 Certified Travel Company.+++++
'''

    info = Label(resorts, text=f)
    info.config(font=("Courier", 12))
    info.pack()
    f = '''_______GIVEN BELOW ARE OUR ONE DAY TRIP PACKAGES_________'''

    info = Label(resorts, text=f)
    info.config(font=("Courier", 12))
    info.pack()
    a = 0
    tulip_b = Button(resorts, text='Magnificent Tulip Resort', command=tulip)
    tulip_b.config(font=("Courier", 17))
    tulip_b.pack()
    wonder_b = Button(resorts, text='Wonderla Amusement park', command=wonderla)
    wonder_b.config(font=("Courier", 17))
    wonder_b.pack()
    club_b = Button(resorts, text='Clubcabana Resorts', command=club)
    club_b.config(font=("Courier", 17))
    club_b.pack()
    pres_b = Button(resorts, text='Presidency Resorts', command=pres)
    pres_b.config(font=("Courier", 17))
    pres_b.pack()
    elegant_b = Button(resorts, text='Elegant Fanatacies Resort', command=elegant)
    elegant_b.config(font=("Courier", 17))
    elegant_b.pack()


def main():
    global logo_window
    logo_window = Tk()

    logo_window.configure(background='White')
    logo_window.geometry("600x300")
    logo_window.title('SKYWAY')

    image = PhotoImage(file="SKY.gif")
    L = Label(logo_window, image=image).pack()

    #
    b = Button(logo_window, text='Click to proceed', command=resorts)
    b.config(font=("Courier", 22))
    b.pack()
    logo_window.mainloop()


main()
