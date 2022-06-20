
from getpass import getpass

import smtplib, ssl;
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart("alternative")

smtp_server = "smtp.gmail.com";
port = 465
reciever_email = input('enter the gmail you want to Send the gmail to\n')
sender_email = input('enter your Gmail you want to be sending from\n');
msg = input("Enter message you want to send\n")
subject = input("subject of Gmail?\n")
password = getpass();
part1 = MIMEText(msg, "plain")

message["Subject"] = subject;
message["From"] = input("What name do you want to send as (beta)\n")
message["To"] = reciever_email

message.attach(part1)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
      server.login(str(sender_email), str(password))
    except: 
      print("Error signing in. Either incorrect password or check here (ITS NOT A VIRUS U CAN CHECK SOURCE CODE) https://myaccount.google.com/lesssecureapps (Repl issue)")
    server.sendmail(sender_email, reciever_email, message.as_string())
    print("Sent email!");
