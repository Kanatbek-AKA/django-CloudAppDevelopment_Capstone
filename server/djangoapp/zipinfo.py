import os, sys
import requests
from requests.exceptions import ConnectionError


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('../../functions/.env'))

zipapi= os.getenv("ZIPCODE")
# zipurl= os.getenv('URLCODE')

# New member get address by zip and state code
def infoAddress(html_zip, html_code):
    import requests as rq
    response = rq.get(f"https://thezipcodes.com/api/v1/search?zipCode={html_zip}&countryCode={html_code}&apiKey={zipapi}").json()
    return response

