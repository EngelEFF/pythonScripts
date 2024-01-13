
# Building a email composer script to send emails to several recepients
# importing the necessary dependenci:wq

# sending the email

import smtplib

# composing the email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

# initializing datetime

now = datetime.datetime.now()






# credentials


SERVER = "smtp.gmail.com"
PORT = 587
SENDER =  input("Sender's email: ").strip()
PASSWORD = input("Enter your password: ").strip()
RECEIVER = input("Receiver email(s): ")
#path = input("Enter path to mail").strip()
#email = input("Enter the message to send: ")

# composing message

message = MIMEMultipart()


message["subject"] = ".The Email Composer. "+str(now.day)+","+str(now.month) +","+str(now.year)

message["sender"] = SENDER
message["password"] = PASSWORD
message["receiver"] = RECEIVER


message.attach(MIMEText("Hello"))



# initializing the server


server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(SENDER,PASSWORD)
server.sendmail(SENDER, RECEIVER, message.as_string())

print(f"email sent successfully ....")

server.quit()








