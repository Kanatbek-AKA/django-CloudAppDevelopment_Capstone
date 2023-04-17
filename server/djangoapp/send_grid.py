# Example from the Docs  https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Note: safely store your api key  and email  
# This api key and email are only for demo
api_key= "api_key"


def send_emails(to_email, text):
    message = Mail(
        from_email='your_email_address',
        to_emails='to_email',
        subject='Your subject or go to SendGrid and create Template',
        html_content=f'<strong>{text}</strong>')
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
