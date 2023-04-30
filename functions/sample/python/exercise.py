# IBM Cloudant
import json
import os
import sys
from ibmcloudant.cloudant_v1 import CloudantV1, Document, AllDocsQuery, BulkDocs, BulkGetQueryDocument, Analyzer, AnalyzerConfiguration, DesignDocument, DesignDocumentOptions, DesignDocumentViewsMapReduce, SearchIndexDefinition, ViewQuery, IndexDefinition, IndexField, SecurityObject
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core import ApiException

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv("../../.env"))


# Credentials
dct = {"COUCH_USERNAME": os.getenv("USERNAME"),
       "IAM_API_KEY": os.getenv("APIKEY"),
       "COUCH_URL": os.getenv('URL'),
       }
# service = CloudantV1.new_instance(service_name="{service-name}")


#
# def connectCloudant(params):
#     authenticator = IAMAuthenticator(params["IAM_API_KEY"])
#     service = CloudantV1(authenticator=authenticator)
#     service.set_service_url(params["COUCH_URL"])
#     # a = [i for i in dir(service) if "head" in i]
#     # print(a)
#     return service

# connectCloudant(dct)


# dDefault header
# ['default_headers', 'head_attachment', 'head_database', 'head_design_document', 'head_document', 'head_local_document', 'head_replication_document', 'head_scheduler_document', 'head_scheduler_job', 'head_up_information', 'set_default_headers', 'user_agent_header']
# def defaultHeader(db):
# 	headers = db.default_headers(db='django-reviews').get_result()
# 	print(headers)
# 	return

# defaultHeader(connectCloudant(dct))

# def serverCheck(db):
# 	response = db.get_up_information().get_result()           # Check if the server is up|on
# 	print("Checking server whether up | down \n", response)
# 	# print(response.get_status_code())
# 	return
    # BasicAuthentication required password that I do not have from Cloudant at all.
    # try:
    # 	authenticator = BasicAuthenticator(username, password)
    # 	service = CloudantV1(authenticator=authenticator)
    # 	service.set_service_url(url)
    # 	ser = service.get_server_information().get_result()
    # 	print(ser)
    # except ApiException as ae:
    # 	print("Error ", ae.code, ae.message, ae.http_response.json()['reason'])


# def serverInfo(db):
    # serverinfo = db.get_server_information().get_result()
# 	print("Server information: \t", serverinfo)
    # response = service.head_database(db='products')                                     # head info 200
# 	memberinfo = db.get_membership_information().get_result()
# 	print("Membership: \t", memberinfo)
# 	uuidsinfo = db.get_uuids(count=10).get_result()
# 	print("UUIDs: \n", uuidsinfo)
# 	capacityinfo = db.get_capacity_throughput_information().get_result()
# 	print("Capacity: \t", capacityinfo)
# 	# response = db.put_capacity_throughput_configuration( blocks=1).get_result()
# 	return

# import sys

# def getAllDB(db):
# 	allDB = db.get_all_dbs().get_result()
# 	print({"DBs": allDB})
# 	return allDB


# def infoAboutDB(db):
# 	print("Enter db name to get information")
# 	dbname = input("Which  DB? ")
# 	response = db.get_database_information(db=dbname).get_result()             # retrieve info about a db
# 	print( response)
# 	return


def getInfoMultipleDB(db, **kwargs):
	db1, db2= input("1st DB name: "), input("2nd DB name: ")
	response = db.post_dbs_info( keys=[db1, db2]).get_result()  # multiple db info
	print(response)
	return


def getValues(db, dbname, **kwargs):
    value = db.post_all_docs(db=dbname, include_docs=True,
                             limit=10).get_result()  # start_key=""
    # value = db.post_all_docs_as_stream( db=dbname, include_docs=True, limit=10).get_result()  # response 200 status
    # print(value)
    res = {
        'headers': {'Content-Type': 'application/json'},
        'body': value
    }
    # # print(type(res))
    for i in res['body']['rows']:
        trans_jsformat = json.dumps(i)
        print(type(trans_jsformat))
    # print(res)
    return


def createNewDB(db, **kwargs):
    dbname = input("Enter DB name: ")
    response = db.put_database(db=dbname, partitioned=False).get_result()
    print(response)
    return


# def getInfoDoc(db, dbname, docid):
# 	response = db.get_document(db=dbname, doc_id=docid ).get_result()
# 	# print(response)
# 	res = {
# 		'headers': {'Content-Type':'application/json'},
# 		'body': response
# 		}
# 	print(res)
# 	return res


# Create a new Doc
def createDOC(db, dbname, **kwargs):
    # print("This is a test of creating a new doc review ")
    docid = "001"
    products_doc = Document(
        _id=docid,           # new id new doc
        type="reviews",
        id="1",                # ID of doc
        name="Berkly Shepley",
        dealership="15",
        # Total grid-enabled service-desk
        review="Let's try to add id like other docs... ",
        car_make="Audi",
        car_model="A6",
        purchase_date="07/09/1999"
        # image="assets/img/0gmsnghhew.jpg")
    )
    response = db.post_document(db=dbname, document=products_doc).get_result()
    res = {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        'body': response
    }
    print(res)
    return res

# Edit exsiting document
def modifyDOC(db, dbname, **kwargs):
    print("This is a test of modification of an existing review ")
    docid = "868d332061185672fe633f284f0f0d2e"
    products_doc = Document(
        id=docid,
        rev="3-aa312a4058c88be8ead010170dbc356d",
        type="reviews",
        name="Berkly Shepley",
        dealership="15",
        # Total grid-enabled service-desk
        review="How to add an id that was in review initially?",
        car_make="Audi",
        car_model="A6",
        car_year=2010,
        purchase=True,
        purchase_date="07/11/2019",
        # image="path/img.jpg"
    )
    response = db.post_document(db=dbname, document=products_doc).get_result()
    res = {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        'body': response
    }
    print(res)
    return res


#  Multiple docs
def valuesMultDocs(db, dbname, **kwargs):
    all_docs_query1 = AllDocsQuery(keys=['id_of_doc', 'id_of_sec_doc'])
    all_docs_query2 = AllDocsQuery(limit=3,  skip=2)
    response = db.post_all_docs_queries(
        db='products', queries=[all_docs_query1, all_docs_query2]).get_result()
    res = {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        'body': response
    }
    print(res)
    return res


def checkChanges(db, dbname, **kwargs):
    # show recent changes
    response = db.post_changes(db=dbname).get_result()
    res = {
        'headers': {'Content-Type': 'application/json'},
        'body': response
    }
    print(res)
    return res


# Delete doc
def deleteDoc(db, dbname, **kwargs):
    idd = "1"
    rev_id = '3-ace5c96629824af4cc3400d8bd75a751'
    response = db.delete_document(
        db=dbname, doc_id=idd, rev=rev_id).get_result()
    print(response)
    return response


# Get info about design
def getDesign(db, dbname, **kwargs):
    response = db.post_design_docs(attachments=True, db=dbname).get_result()
    print(response)
    return response


# serverCheck(connectCloudant(dct))
# serverInfo(connectCloudant(dct))
# getAllDB(connectCloudant(dct))
# infoAboutDB(connectCloudant(dct))
# getInfoMultipleDB(connectCloudant(dct))
# getValues(connectCloudant(dct), 'django-reviews')
# getInfoDoc(connectCloudant(dct), "django-reviews", "868d332061185672fe633f284f0f0d2e")
# createDOC(connectCloudant(dct), "django-reviews")
# checkChanges(connectCloudant(dct), "django-reviews")
# modifyDOC(connectCloudant(dct), "django-reviews")
# deleteDoc(connectCloudant(dct), "django-reviews")
# getDesign(connectCloudant(dct), "django-reviews")


# response = service.delete_database(db='<db-name>').get_result()      # remove a db


# Query a list of all documents in a database
# ['post_all_docs', 'post_all_docs_as_stream', 'post_all_docs_queries', 'post_all_docs_queries_as_stream']
# response = service.post_all_docs( db='<db-name>', include_docs=True, start_key='abc', limit=10).get_result()  #


# Bulk doc
# event_doc_1 = Document(id="0007241142412418284", type="event", userid="abc123", eventType="addedToBasket", productId="1000042",  date="2019-01-28T10:44:22.000Z")
# event_doc_2 = Document(id="0007241142412418285", type="event", userid="abc234", eventType="addedToBasket", productId="1000050", date="2019-01-25T20:00:00.000Z")

# bulk_docs = BulkDocs(docs=[event_doc_1, event_doc_2])
# response = service.post_bulk_docs(db='<db-name>', bulk_docs=bulk_docs).get_result()

# Create or modify event doc
# event_doc = Document(type='event', userid='abc123', eventType='addedToBasket', productId='1000042', date='2019-01-28T10:44:22.000Z')
# response = service.put_document(db='db-name', doc_id='0007241142412418284', document=event_doc).get_result()

# Retrieve design doc
# response = service.get_design_document(db='<db-name>', ddoc='appliances', latest=True).get_result()
# Retrieve info about design
# response = service.get_design_document_information(db='<db-name>', ddoc='appliances').get_result()

# Create or Modify design doc
# email_view_map_reduce = DesignDocumentViewsMapReduce(map='function(doc) { if(doc.email_verified  === true){\n  emit(doc.email, [doc.name, doc.email_verified, doc.joined]) }}')
# user_index = SearchIndexDefinition(index='function (doc) { index("name", doc.name); index("active", doc.active); }', analyzer=AnalyzerConfiguration(name="standard", fields={"email": Analyzer(name="email")}))
# design_document = DesignDocument(views={'getVerifiedEmails': email_view_map_reduce}, indexes={'activeUsers': user_index})
# response = service.put_design_document(db='<db-name>', design_document=design_document, ddoc='allusers').get_result()

# Get info about design
# response = service.post_design_docs(attachments=True, db='<db-name>').get_result()

# Multi-query a MapReduce view
# query1 = ViewQuery(include_docs=True, limit=5)
# query2 = ViewQuery(descending=True, skip=1)
# response = service.post_view_queries(db='<db-name>', ddoc='allusers', queries=[query1, query2], view='getVerifiedEmails').get_result()
#
# Get index of db
# response = service.post_explain(db='<db-name>', execution_stats=True, limit=10, selector={'type': {"$eq": "user"}}).get_result()
# Get info about index
# response = service.get_indexes_information(db='<db-name>').get_result()
# Query an index by using selector syntax
# response = service.post_find(db='<db-name>', selector={'email_verified': {'$eq': True}}, fields=["_id", "type", "name", "email"], sort=[{'email': 'desc'}], limit=3).get_result()

# Create an index
# index_field = IndexField(email="asc")
# index = IndexDefinition(fields=[index_field])
# response = service.post_index(db='<db-name>', ddoc='json-index', name='getUserByEmail', index=index, type='json').get_result()

# Delete index
# response = service.delete_index(db='<db-name>', ddoc='json-index', index='getUserByName', type='json').get_result()
#
# Tokenazation
# response = service.post_search_analyze(analyzer='english', text='running is fun').get_result()

# Query a search index
# response = service.post_search(db='<db-name>', ddoc='allusers', index='activeUsers', query='name:Jane* AND active:True').get_result()
# Retrieve information about a search index
# response = service.get_search_info(db='<db-name>', ddoc='appliances', index='findByPrice').get_result()

# Retrieve information about a database partition
# response = service.get_partition_information(db='<db-name>', partition_key='small-appliances').get_result()

# Query a list of all documents in a database partition
# response = service.post_partition_all_docs(db='<db-name>', partition_key='small-appliances', include_docs=True).get_result()
#
# Retrieve change events for all databases
# response = service.get_db_updates(feed='normal', heartbeat=10000, since='now').get_result()
# response = service.post_changes(db='<db-name>').get_result()
#
# Cancel replication
# response = service.delete_replication_document(doc_id='repldoc-example', rev='3-a0ccbdc6fe95b4184f9031d086034d85').get_result()
#
# Retrieve replication doc
# response = service.get_replication_document(doc_id='repldoc-example').get_result()
#
# Retrieve current session cookie information
# response = service.get_session_information().get_result()
#
# Retrieve database permissions information
# response = service.get_security(db='<db-name>').get_result()
#
# Modify database permissions   | nobody username applies to all unauthenticated connection attempts
# members = SecurityObject(names=['user1', 'user2'], roles=['developers'])
# response = service.put_security(db='<db-name>', members=members).get_result()
#
# security_object = {'nobody':['_reader']}
# response = service.put_cloudant_security_configuration(db='<db-name>', cloudant=security_object).get_result()
#
# Generates API keys for apps or persons to enable database access
# response = service.post_api_keys().get_result()
#
# Get CORS info
# response = service.get_cors_information().get_result()
#
# Retrieve shard information
# response = service.get_shards_information(db='<db-name>').get_result()
# Retrieve shard information for a specific document
# response = service.get_document_shards_info(db='<db-name>', doc_id='small-appliances:1000042').get_result()
#
# Get running tasks
# response = service.get_active_tasks().get_result()
#
# Retrieve Activity Tracker events information
# response = service.get_activity_tracker_events().get_result()
# Modify Activity Tracker events configuration	management | data
# response = service.post_activity_tracker_events(types=['management']).get_result()
#
# Retrieve the current provisioned throughput capacity consumption
# response = service.get_current_throughput_information().get_result()

# print(response)


# Session Cookies
# authenticator = CouchDbSessionAuthenticator('{username}', '{password}')
# service = CloudantV1(authenticator=authenticator)
# service.set_service_url('{url}')


# Api
# try:
#   # Invoke a Cloudant method request
#   authenticator = IAMAuthenticator('{dct.IAM_API_KEY}')
#   service = CloudantV1(authenticator=authenticator)
#   service.set_service_url('{dct.COUCH_URL}')
# except ApiException as ae:
#   print("Method failed")
#   print(" - status code: " + str(ae.code))
#   print(" - error message: " + ae.message)
#   if ("reason" in ae.http_response.json()):
#     print(" - reason: " + ae.http_response.json()["reason"])

#
# from requests import ConnectionError, ReadTimeout, RequestException, ValueError

# try:
#   # Invoke a Cloudant method request
# except ConnectionError as cerr:
#   print("Connection error occurred:")
#   print(cerr)
# except ReadTimeout as rt:
#   # The server did not send any data in the allotted amount of time.
#   print("Read timed out:")
#   print(rt)
# except RequestException as re:
#   # Handle other request failures
#   print("Request Exception:")
#   print(re)
# except ValueError as ve:
#   print("Invalid argument value:\n" + ve.message)
# finally:
#
