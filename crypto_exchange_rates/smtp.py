import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from PyQt6 import  QtWidgets

def send_email(receiver_email: str, html: str):
    load_dotenv()

    PASSWORD = os.getenv("PASSWORD")
    EMAIL = os.getenv("EMAIL")

    sender_email = "cryptocoinrates@gmx.com"
    receiver_email = receiver_email
    subject = "Your Personal Cryptocurrency Tracker"


   
    body = html
    


   
    smtp_server = 'mail.gmx.com'
    smtp_port = 587  

    
    username = EMAIL
    password = PASSWORD

  
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    
    message.attach(MIMEText(body, "html"))

 
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(username, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        
    finally:
        server.quit()  
