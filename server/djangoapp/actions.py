import os
import json
import requests
# from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError, InvalidURL

# import environ
# environ.Env()
# environ.Env.read_env('../../functions/.env')

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('../../functions/.env'))

DEALERS= os.environ.get('ACTION_URL_PY')
REVIEWS= os.environ.get('ACTION_URL_NODE')

def get_action_dealers():
    try:
        response = requests.get(DEALERS, headers={'Content-Type': 'application/json'}).json()
        return response
    except (InvalidURL,ConnectionError, NameError) as err:
        pass

def get_action_reviews():
    try:
        response = requests.get(REVIEWS, headers={'Content-Type': 'application/json'}).json()
        return response
    except (InvalidURL, ConnectionError, NameError) as err:
        pass



# This part works with local DB dbsqlite3 in your app
# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
# Since my cloudant account is unusual and it does not contain any password, am using django-environ | dotenv both are same
# to retrieve data from server and render it on a template
# import requests
# import json
# from .models import CarDealer
# from requests.auth import HTTPBasicAuth
# def get_request(url, **kwargs):
#     print(kwargs)
#     print("GET from {} ".format(url))
#     try:
#         # Call get method of requests library with URL and parameters
#         response = requests.get(url, headers={'Content-Type': 'application/json'},
#                                     params=kwargs)
            # # Updated for sentiment anaylsis
            # if api_key:
            # # Basic authentication GET
            # requests.get(url, params=params, headers={'Content-Type': 'application/json'},
            #                                 auth=HTTPBasicAuth('apikey', api_key))
            # else:
            # # no authentication GET
            # request.get(url, params=params)

#     except:
#         # If any error occurs
#         print("Network exception occurred")

#     status_code = response.status_code
#     print("With status {} ".format(status_code))
#     json_data = json.loads(response.text)
#     return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
# def get_dealers_from_cf(url, **kwargs):
#     results = []
#     # Call get_request with a URL parameter
#     json_result = get_request(url)
#     if json_result:
#         # Get the row list in JSON as dealers
#         dealers = json_result["rows"]
#         # For each dealer object
#         for dealer in dealers:
#             # Get its content in `doc` object
#             dealer_doc = dealer["doc"]
#             # Create a CarDealer object with values in `doc` object
#             dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
#                                    id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
#                                    short_name=dealer_doc["short_name"],
#                                    st=dealer_doc["st"], zip=dealer_doc["zip"])
#             results.append(dealer_obj)
#     return results


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
# url= "https://us-south.functions.appdomain.cloud/api/v1/web/8a304c6c-beee-4d01-9cb7-80e658c05d70/dealership-package/get-dealerships"
# url2 = "https://us-south.functions.appdomain.cloud/api/v1/web/8a304c6c-beee-4d01-9cb7-80e658c05d70/reviews-django/get-reviews"


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
