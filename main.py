# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

from flask import Flask, request
app = Flask(__name__)

# a simple route to testing our app 
@app.route('/')
def hello_world():
    return 'Hello, World!'

# app route
@app.route('/smtp')
def send_smt():
    gmail_user = 'your@email.com'
    gmail_password = ''

    sent_from = 'sent from me'
    to = ['anotherperson@email.com']
    subject = 'email app'
    body = 'testing smtp using flask to build routes'

    email_text =f'''
    From:{sent_from},
    To: {",".joinn(to)}
    Subject: {subject},
    Body: {body},
    ''' 
    # ", ".join(to),
    # email_text = "Anoter Mail to you"
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        return "Email sent successfully!"
    except Exception as ex:
        return f'Something went wrong….{ex}'

    # return 'done!!'

