# Example from the Docs  https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
 
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv("../../functions/.env"))

api_key= os.environ.get('API_SEND')
your_email = os.environ.get('EMAIL')

def send_emails(to_email):
    message = Mail(
        from_email=your_email,
        to_emails=to_email,
        subject='Subcription confirmation for AKA motors',
        html_content=f'<strong>Hey, you subcribed in AKA motors.</strong>')
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        pass
