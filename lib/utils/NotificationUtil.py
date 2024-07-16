# Import smtplib for the actual sending function
import smtplib

from email.message import EmailMessage

def send_email(to, subject, content):
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = subject
    msg['From'] = 'arnoor2@illinois.edu'
    msg['To'] = to
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

