import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ast


def sendEmail(subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_sender = os.environ.get("email")
    code = os.environ.get("gcode")

    recipients = os.environ.get("recipients")
    recipients = ast.literal_eval(recipients)

    msg = MIMEMultipart()
    msg["From"] = email_sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as servidor:
            servidor.starttls()
            servidor.login(email_sender, code)
            servidor.sendmail(email_sender, recipients, msg.as_string())
            print("E-mail sent")
    except Exception as e:
        print(f"Error sending e-mail: {e}")
