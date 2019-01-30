import smtplib
import time
from .otp_gmail import *


def mail(gmail_user, gmail_password, froma, to, subject, return_state=False):
    body = aaa
    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (froma, ", ".join(to), subject, body)

    try:

        start_time = time.time()
        # print 'Connecting...'
        print
        'Please Wait for a while...'

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # print("--- %s seconds ---" % (time.time() - start_time))
        # print 'connected'
        server.ehlo()
        # print 'Signing ...'
        server.login(gmail_user, gmail_password)
        # print 'logged in'
        # print 'Sending...'

        server.sendmail(froma, to, email_text)

        server.close()

        # print 'Email sent!'

    except:
        print
        'Something went wrong...'
        print
        'Please Check your Internet Connection and try again.'


def send_mail_otp(INTEGER, email):
    gmail_user = 'python.connections@gmail.com'
    gmail_password = 'qwer@1234'
    otp = otp_func(INTEGER)
    global otp
    froma = gmail_user
    to = [email]
    subject = 'SKYWAY MEMBERSHIP REGISTRATION'
    print
    otp, 'mail'

    aaa = "Your OTP is " + str(otp)
    global aaa

    mail(gmail_user, gmail_password, froma, to, subject, True)
    return otp


def send_mail_reg(name, phone, email):
    gmail_user = 'python.connections@gmail.com'
    gmail_password = 'qwer@1234'

    froma = gmail_user
    to = [email]
    subject = 'SKYWAY MEMBERSHIP REGISTRATION SUCCESSFUL'
    aaa = "Congratulations - You are a member of the SKYWAY Family.\n Your details are as follows...\nName: " + name + "\nMobile Number: " + str(
        phone) + "\nEmail Id: " + email + "\nWe are happy to serve you."
    global aaa
    mail(gmail_user, gmail_password, froma, to, subject)


def send_mail_member(name, phone, email):
    gmail_user = 'python.connections@gmail.com'
    gmail_password = 'qwer@1234'

    froma = gmail_user
    to = [email]
    subject = 'SKYWAY MEMBER DETAILS'
    aaa = "Congratulations - You are a member of the SKYWAY Family.\n Your details are as follows...\nName: " + name + "\nMobile Number: " + str(
        phone) + "\nEmail Id: " + email + "\nWe are happy to serve you."
    global aaa
    mail(gmail_user, gmail_password, froma, to, subject)


def send_mail_invoice(name, res, date, a, no_of_passengers, amt, discount, d_percent, final_amt, email):
    gmail_user = 'python.connections@gmail.com'
    gmail_password = 'qwer@1234'

    froma = gmail_user
    to = [email]
    if (1 == 1):
        subject = 'SKYWAY RESORT BOOKING : INVOICE'
        a1 = 'Name: ' + name + '\n'
        a2 = 'Resort booked: ' + res + '\n'
        a3 = 'Date: ' + str(date) + '\n'
        a4 = 'Cost of 1 day stay per person=Rs.' + str(a) + '\n'
        a5 = 'Number of passengers visiting' + res + ':' + str(no_of_passengers) + '\n'
        a6 = 'Subtotal: Rs.' + str(amt) + '\n'
        a7 = 'Discount Applied: Rs.' + str(discount) + '\n'
        a8 = 'Discount %: ' + d_percent + '\n'
        a9 = '------------------------\n'
        a10 = 'Final Amount= Rs.' + str(final_amt) + '\n'
        a11 = '------------------------\n'
        aaa = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11
        global aaa
    mail(gmail_user, gmail_password, froma, to, subject)


def send_mail_payment(final_amt, email):
    gmail_user = 'python.connections@gmail.com'
    gmail_password = 'qwer@1234'
    froma = gmail_user
    to = [email]
    if (1 == 1):
        subject = 'SKYWAY PAYMENT RECEIPT'
        b1 = 'Amount successfully paid: ' + str(final_amt) + '\n'
        b2 = '\n'
        b3 = 'Thank you for booking with SKYWAY. We are happy to serve you'
        aaa = b1 + b2 + b3
        global aaa
    mail(gmail_user, gmail_password, froma, to, subject)




