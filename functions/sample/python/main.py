"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
import os
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
# 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv("../../.env"))


# get-reviews = https://us-south.functions.appdomain.cloud/api/v1/web/8a304c6c-beee-4d01-9cb7-80e658c05d70/reviews-django/get-reviews
# post-reviews =  

dct = { "COUCH_USERNAME": os.getenv("USERNAME"),
        "IAM_API_KEY" : os.getenv("APIKEY") }


# def main(param_dict):
#     try:
    #     client = Cloudant.iam(
    #         account_name=param_dict["COUCH_USERNAME"],
    #         api_key=param_dict["IAM_API_KEY"],
    #         connect=True,
    #     )
    #     print(f"Databases: {client.all_dbs()}")
    # except CloudantException as cloudant_exception:
    #     print("unable to connect")
    #     return {"error": cloudant_exception}
    # except (requests.exceptions.RequestException, ConnectionResetError) as err:
    #     print("connection error")
    #     return {"error": err}

    # return {"dbs": client.all_dbs()}

# main(dct)


# import os
# # from cloudant.client import Cloudant
# client = Cloudant.bluemix(os.getenv('VCAP_SERVICES'),
#                         'Cloudant NoSQL DB')
# client = Cloudant.iam(
#     account_name=dct["COUCH_USERNAME"],
#     api_key=dct["IAM_API_KEY"],
#     connect=True,
#     )

# db = client.keys(remote=True) # all_dbs()
# print(db)

# db_data = client.get(key="django-dealerships", default="django-dealerships", remote=True)
# print(db_data)

# print(help(client.get)) 
# get(key, default=None, remote=False)
# :param str key: Database name used to retrieve the database object.
# :param str default: Default database name.  Defaults to None.
# :param bool remote: Dictates whether the locally cached
#     database is returned or a remote request is made to retrieve
#     the database from the server.  Defaults to False.


# print(f"Databases: {client.all_dbs()}")   | values  | is_iam_authenticated |
# print(dir(client.items()))
# print(help(client.items))

# print(f"Databases: {client.metadata()}")
# # print(help(client.metadata))

# print(f"Databases: {client.keys()}")  
# print(f"Databases: {client.values()}")  
# print(client.disconnect())
