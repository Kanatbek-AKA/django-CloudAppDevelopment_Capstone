from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1, Document, AllDocsQuery
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ClassificationsOptions, ConceptsOptions, EmotionOptions, SemanticRolesOptions, SentimentOptions
import os
import json
# import related models here
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError

# django-environ worked 5-10 minutes ago and now stopped working on 
# import environ
# environ.Env()
# environ.Env.read_env('../../functions/.env')

# This part works pure with Cloudant DB remotely, and you do not need to have a local DB dbsqlite3 in your app
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('../../functions/.env'))

dct = {
# "COUCH_USERNAME": os.getenv('USERNAME'),
# 'IAM_API_KEY': os.getenv("APIKEY"),
# 'COUCH_URL': os.getenv("URL"),
# "DB1": os.getenv("DATADBNAME"),
# 'DB2': os.getenv("DATADBNAME2"),
"DEALERS": os.environ.get('ACTION_URL_PY'),
'REVIEWS': os.environ.get('ACTION_URL_NODE'), 
'NLUAPI': os.getenv('NLU_KEY'),
"NLURL": os.getenv('NLU_URL'),
}


def connectServer(params):
    try:
        authenticator = IAMAuthenticator(params['IAM_API_KEY'])
        service = CloudantV1(authenticator=authenticator)
        service.set_service_url(params['COUCH_URL'])
        return service
    except (KeyError,ValueError, AttributeError,ApiException) as anyerror:
        pass


def get_dealers():
    try:
        service = connectServer(dct)
        dbname = dct['DB1']
        values = service.post_all_docs(db=dbname, include_docs=True).get_result()
        result = {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': values
        }
        return result
    except (KeyError,ValueError, AttributeError,ApiException) as anyerror:
        pass


# # Get reviews
def get_reviews():
    try:
        service = connectServer(dct)
        dbname = dct['DB2']
        values = service.post_all_docs(
            db=dbname, include_docs=True).get_result()
        result = {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': values
        }
        # print(result)
        return result
    except (KeyError,ValueError, AttributeError,ApiException) as anyerror:
        pass



def be_aka(params):
    service = connectServer(dct)
    dbname = dct['DB1']
    new_member = Document(
        id=params['ids'],
        full_name=params['full_name'],
        short_name=params['short_name'],
        address=params['address'],
        city=params['city'],
        state=params['state'],
        # or use JS  to read and find abbrivation for each state
        st=params['st'],
        zip=params['zipcode'],
        # Using JS or Python to get address lat (new)
        lat=params['latitude'],
        # Using JS or Python to get address long (new)
        long=params['longitude'],
        # date of registration being aka
        reg_date=params['date'],
        # Image required
        image=params['image'],
        # Device informtion
        device=params['device'],
        machine=params['machine'],
        system=params['system'],
        processor=params['processor'],
    )
    response = service.post_document(
        db=dbname, document=new_member).get_result()
    res = {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        'body': response
    }
    # print(res)
    return res






# Post review
def post_reviews(params):
    service = connectServer(dct)
    dbname = dct['DB2']
    products_doc = Document(
        id=params['ids'],
        type="reviews",
        name=params['name'],
        dealership=params['dealership'],
        review=params['review'],
        car_make=params['car_make'],
        car_model=params['car_model'],
        purchase=params['bool'],
        car_year=params['year'],
        client_purchase_date= params['client_purchase'],
        reviews_date=params['date']
        # image="assets/img/0gmsnghhew.jpg")
    )
    response = service.post_document(
        db=dbname, document=products_doc).get_result()
    res = {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        'body': response
    }
    # print(res)
    return res


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(text):
    try:
        authenticator = IAMAuthenticator(dct['NLUAPI'])
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2022-04-07', authenticator=authenticator)
        natural_language_understanding.set_service_url(dct['NLURL'])
        response = natural_language_understanding.analyze(
            text=text,
            # return_analyzed_text=True,
            # fallback_to_raw=True,  # to use raw html
            features=Features(
                entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
                keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2))).get_result()
        # print(json.dumps(response, indent=2))
        return response
    except (ValueError, AttributeError,ApiException) as anyerror:
        pass





# Extra exercise 
# IDs related both dbs 
def intermediarForSameID(file, file2):
    res = []
    r = [rev['doc'] for rev in file2['body']['rows']]
    d = [deal['doc'] for deal in file['body']['rows']]

    for dk, rk in zip(d, r):
        for key, val in (dk.items() & rk.items()):  
            if dk[key] == rk[key]:                  # looking for same keys e.g. id
                res.append({key:val})
                # print(key, val)

    return res


















