import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from celery import shared_task


smtp_port = 587
smtp_server = "smtp.gmail.com"
email_from = "romakostin.mtb2006@gmail.com"
pswd = "keccgvkgumzzajsb"

@shared_task
def send_emails(emails_list, title, msg):
    time.sleep(1)

    # Connect with the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Successfully connected to server")
    print()

    emails_list.split(',')
    for person in emails_list:
        body = msg

        # Make a MIME object to define parts of the email
        email_msg = MIMEMultipart()
        email_msg['From'] = email_from
        email_msg['To'] = person
        email_msg['Subject'] = title

        # Attach the body of the message
        email_msg.attach(MIMEText(body, 'plain'))

        # Cast as string
        text = email_msg.as_string()

        # Send email
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the server connection
    TIE_server.quit()
