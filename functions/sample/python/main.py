"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
import os, sys
# from cloudant.client import Cloudant          # deprecated 
# from cloudant.error import CloudantException  # deprecated
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv("../../.env")) 

# Loading packages 
from ibmcloudant.cloudant_v1 import CloudantV1, Document, AllDocsQuery, IndexField, ViewQuery
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, ApiException

dct {
   "URL": os.getenv("URL"),
   "USERNAME": os.getenv("USERNAME"),
   "APIKEY": os.getenv("API"),
}

#  E.g. testting if the dotenv finds the .env file and retrieves creadentials
print( dct['API'] )




# Fundtion of deprecated module  unneccessary
# def main(param_dict):
#     try:
#         client = Cloudant.iam(
#             account_name=param_dict["COUCH_USERNAME"],
#             api_key=param_dict["IAM_API_KEY"],
#             connect=True,
#         )
#         print(f"Databases: {client.all_dbs()}")
#     except CloudantException as cloudant_exception:
#         print("unable to connect")
#         return {"error": cloudant_exception}
#     except (requests.exceptions.RequestException, ConnectionResetError) as err:
#         print("connection error")
#         return {"error": err}

#     return {"dbs": client.all_dbs()}
