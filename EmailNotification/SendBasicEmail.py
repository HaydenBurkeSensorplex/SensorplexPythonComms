'''
Sends emails through the smtp/gmail server using the basic python libraries.
For examples using ease-of-use libraries see yagmailExample.py

Walk Through: https://realpython.com/python-send-email/
See also further things like sending mass emails from csv, sending files and HTML type emails

'''

import smtplib, ssl

#Google encryption port
port = 465  # For SSL
#gmail server
smtp_server = "smtp.gmail.com"
sender_email = "sensorplexnotification@gmail.com"  
receiver_email ="herbert@sensorplex.com"

password = input("Type your password and press enter: ")

message = """\
Subject: Test Email Using Python

This is a test email sent from python.



"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)