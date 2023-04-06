/**
 * Get all databases
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');
const dotenv = require('dotenv').config({
  path: require('find-config')('../.env'),
});

dct = {
  IAM_API_KEY: process.env.APIKEY,
  COUCH_URL: process.env.URL,
};

function main(params) {
  const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY });
  //console.log(authenticator)

  const cloudant = CloudantV1.newInstance({
    authenticator: authenticator,
  });
  cloudant.setServiceUrl(params.COUCH_URL);

  //    //console.log(cloudant.status)
  //    let dbList = getDbs(cloudant);
  //    return { dbs: dbList };

  // Get all DB names
  // cloudant.getAllDbs().then(response => {
  //   console.log({"dbs": response.result});
  // }).catch((error) => console.log(error));

  // Get Server information
  // cloudant.getServerInformation().then(response => {
  //   console.log(response.result);
  // }).catch((error) => console.log(error));

  // Get Membership information
  // cloudant.getMembershipInformation().then(response => {
  //     console.log(response.result);
  //   }).catch((error) => console.log(error));

  // Get Capacity information
  // cloudant.getCapacityThroughputInformation().then(response => {
  //   console.log(response.result);
  // }).catch((error) => console.log(error));

  // Get UUIDs
  // const uuidsParams = CloudantV1.GetUuidsParams = {
  //   count: 10
  // };
  // cloudant.getUuids(uuidsParams).then(response => {
  //   console.log(response.result);
  // }).catch((error) => console.log(error));

  // Get information about multiple databases
//   cloudant
//     .postDbsInfo({ keys: ['flowdb', 'diamonds', 'django-reviews'] })
//     .then(response => {
//       console.log(response.result);
//     })
//     .catch(error => console.log(error));

// Remove db
// cloudant.deleteDatabase({db: '<enter-db-name>'}).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Get information about DB content
// cloudant.getDatabaseInformation({db: 'flowdb'}).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Get head of DB  --> 200
// cloudant.headDatabase({db: 'flowdb'}).then(response => {
//   console.log(response.status);
// }).catch((error) => console.log(error));

// Create a DB
// cloudant.putDatabase({ db: 'test_new_db_cli', partitioned: false }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Change feed
// cloudant.postChanges({ db: 'test_new_db_cli' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Query a list of all design documents in a database
// cloudant.postDesignDocs({ attachments: true, db: 'diamonds' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Create or modify docs in a DB
// const productsDoc: CloudantV1.Document = {
//   _id: 'small-appliances:1000042',
//   type: 'product',
//   productid: '1000042',
//   brand: 'Salter',
//   name: 'Digital Kitchen Scales',
//   description: 'Slim Colourful Design Electronic Cooking Appliance for Home / Kitchen, Weigh up to 5kg + Aquatronic for Liquids ml + fl. oz. 15Yr Guarantee - Green',
//   price: 14.99,
//   image: 'assets/img/0gmsnghhew.jpg'
// };
// cloudant.postDocument({db: '<enter-db-name>', document: productsDoc }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Query a list of all documents in a database
// cloudant.postAllDocs({ db: 'orders', includeDocs: true, startKey: 'abc', limit: 10 }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Multiple query the list of all Docs in a DB
// const allDocsQueries: CloudantV1.AllDocsQuery[] = [{
//         keys: ['small-appliances:1000042', 'small-appliances:1000043'],
//       },
//       {
//         limit: 3,
//         skip: 2
//     }];
// cloudant.postAllDocsQueries({ db: '<enter-db-name>',  queries: allDocsQueries }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Bulk docs
// const eventDoc1: CloudantV1.Document = {
//   _id: '0007241142412418284',
//   type: 'event',
//   userid: 'abc123',
//   eventType:'addedToBasket',
//   productId: '1000042',
//   date: '2019-01-28T10:44:22.000Z'
//   }
// const eventDoc2: CloudantV1.Document = {
//   _id: '0007241142412418285',
//   type: 'event',
//   userid: 'abc234',
//   eventType: 'addedToBasket',
//   productId: '1000050',
//   date: '2019-01-25T20:00:00.000Z'
//   }
// const bulkDocs: CloudantV1.BulkDocs = {  docs: [eventDoc1, eventDoc2]}

// cloudant.postBulkDocs({ db: 'enter-db-name', bulkDocs: bulkDocs }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Bulk query revision for multiple docs
// const docId = 'order00067';
// const bulkGetDoc1: CloudantV1.BulkGetQueryDocument = {
//   id: docId,
//   rev: '3-917fa2381192822767f010b95b45325b'
// };
// const bulkGetDoc2: CloudantV1.BulkGetQueryDocument = {
//   id: docId,
//   rev: '4-a5be949eeb7296747cc271766e9a498b'
// };
// const bulkGetDocs: CloudantV1.BulkGetQueryDocument[] = [bulkGetDoc1, bulkGetDoc2];
// const postBulkGetParams: CloudantV1.PostBulkGetParams = { db: 'orders', docs: bulkGetDocs,};

// cloudant.postBulkGet(postBulkGetParams).then(response => {
//     console.log(response.result);
//   }).catch((error) => console.log(error));

// Remove a doc in a DB
// cloudant.deleteDocument({ db: '<enter-db_name>', docId: '<enter-doc-id>', rev: '2-9a0d1cd9f40472509e9aac6461837367' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve a doc
// cloudant.getDocument({ db: '<enter-db-name>', docId: '<enter-doc-id>' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Create or modify a doc in a DB
// const eventDoc: CloudantV1.Document = {
//     type: 'event',
//     userid: 'abc123',
//     eventType: 'addedToBasket',
//     productId: '1000042',
//     date: '2019-01-28T10:44:22.000Z'
//   };
// cloudant.putDocument({ db: '<enter-db-name>', docId: '<enter-doc-id>', document: eventDoc }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Get design of a doc in DB  CHECK the name of DOC
// cloudant.getDesignDocument({ db: 'flowdb', ddoc: '<enter-doc-name-of-flowdb>', latest: true }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Get infor about design of a doc
// cloudant.getDesignDocumentInformation({ db: '<enter-db-name>', ddoc: '<enter-doc-name-of-flowdb>' }).then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Create or modify a design doc
// const emailViewMapReduce: CloudantV1.DesignDocumentViewsMapReduce = {
//   map: 'function(doc) { if(doc.email_verified  === true){\n  emit(doc.email, [doc.name, doc.email_verified, doc.joined]) }}'
// }
// const userIndex: CloudantV1.SearchIndexDefinition = {
//   index: 'function (doc) {  index("name", doc.name);  index("active", doc.active);}'
// }
// const designDocument: CloudantV1.DesignDocument = {
//   views: {'getVerifiedEmails': emailViewMapReduce},
//   indexes: {'activeUsers': userIndex}}

// cloudant.putDesignDocument({ db: '<enter-db-name>', designDocument: designDocument, ddoc: 'allusers' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// const productMap: CloudantV1.DesignDocumentViewsMapReduce = {
//   map: 'function(doc) { emit(doc.productid, [doc.brand, doc.name, doc.description]) }'
// }
// const priceIndex: CloudantV1.SearchIndexDefinition = {
//   index: 'function (doc) {  index(\"price\", doc.price);}'
// }
// const partitionedDesignDoc: CloudantV1.DesignDocument = {
//   views: {'byApplianceProdId': productMap},
//   indexes: {'findByPrice': priceIndex}}

// cloudant.putDesignDocument({ db: 'products', designDocument: partitionedDesignDoc, ddoc: 'appliances' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Remove design of a doc
// cloudant.deleteDesignDocument({ db: 'enter-db-name', ddoc: 'appliances', rev: '1-98e6a25b3b45df62e7d47095ac15b16a' }).then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Retrieve information about all indexes
// cloudant.getIndexesInformation({ db: 'diamonds' }).then(response => {
//     console.log(response.result);
//   }).catch((error) => console.log(error));

// Get info about index used for a query
// const selector= CloudantV1.Selector = {
//     type: {
//       "$eq": "special"   // user
//     }
//   };
// cloudant.postExplain({ db: 'diamonds', executionStats: true, limit: 10, selector: selector }).then(response => {
//     console.log(response.result);
//   }).catch((error) => console.log(error));

// // Create a new index in a DB
// Type "json" index fields require an object that maps the name of a field to a sort direction.
// const indexField = CloudantV1.IndexField = { email: 'asc'}
// const index = CloudantV1.IndexDefinition = { fields: [indexField]}  // <<---- change  according to your db
// cloudant.postIndex({
//   db: 'django-dealerships',
//   ddoc: 'json-index',
//   name: 'getUserByEmail',
//   index: index,
//   type: 'json'
// }).then(response => {console.log(response.result) }).catch((error) => console.log(error));

// Query an index by using selector syntax
// const selector = CloudantV1.JsonObject = {email_verified: {'$eq': true }};
// const sort = CloudantV1.JsonObject = { email: 'desc'};
// cloudant.postFind({
//   db: 'django-dealerships',
//   selector: selector,
//   fields: ['_id', 'type', 'name', 'email'],
//   sort: [sort],
//   limit: 3
// }).then(response => { console.log(response.result) }).catch((error) => console.log(error));

// Remove index
// cloudant.deleteIndex({db: 'django-dealerships', ddoc: 'json-index', index: 'getUserByEmail', type: 'json'}).then(response => {
//  console.log(response.result);
//  }).catch((error) => console.log(error));

// Tokenization of sample text
//  cloudant.postSearchAnalyze({analyzer: 'english', text: 'running is fun', }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Search index
//  cloudant.postSearch({ db: '<enter-db-name>', ddoc: 'allusers', index: 'activeUsers', query: 'name:Jane* AND active:True' }).then(response => {console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve info about partition
// cloudant.getPartitionInformation({ db: '<enter-db-name>', partitionKey: '<check-and-enter-part-key>' }).then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Retrieve change event for all DB
// cloudant.getDbUpdates({ feed: 'normal', heartbeat: 10000, since: 'now'}).then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Get replication doc
// cloudant.getReplicationDocument({ docId: 'repldoc-example' }).then(response => {
//    console.log(response.result);
//  });

// Cancel replication
// cloudant.deleteReplicationDocument({ docId: 'repldoc-example', rev: '3-a0ccbdc6fe95b4184f9031d086034d85' }).then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Create or modify a replication
// const sourceDb: CloudantV1.ReplicationDatabase = { url: '<your-source-service-url>/animaldb' };
// const targetDb: CloudantV1.ReplicationDatabase = {
//   auth: {
//     iam: {
//       'api_key': '<your-iam-api-key>'
//     }
//   },
//   url: '<your-target-service-url>' + '/' + 'animaldb-target'
// };
// const replDocument: CloudantV1.ReplicationDocument = {
//   id: 'repldoc-example',
//   create_target: true,
//   source: sourceDb,
//   target: targetDb
// }
// cloudant.putReplicationDocument({docId: 'repldoc-example',replicationDocument: replDocument}).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Get replication scheduler doc
//  cloudant.getSchedulerDocs({ limit: 100, states: ['completed']}).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// cloudant.getSchedulerDocument({ docId: 'repldoc-example' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve info about scheduler job
// cloudant.getSchedulerJob({ jobId: '7b94915cd8c4a0173c77c55cd0443939+continuous' }).then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Get session cookie information
// cloudant.getSessionInformation().then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Retrieve a db permission information
// cloudant.getSecurity({ db: 'diamonds' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Modify DB permission
//  const members: CloudantV1.SecurityObject = { names: ['user1', 'user2'], roles: ['developers']};
//  cloudant.putSecurity({ db: '<enter-db-name>',  members: members }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Modify Cloudant permission
// cloudant.putCloudantSecurityConfiguration({db: '<enter-db-name>', cloudant: {'nobody': ['_reader']}}).then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Generates API keys for apps or persons to enable database access
// cloudant.postApiKeys().then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Retrieve CORS config info
// cloudant.getCorsInformation().then(response => {
//    console.log(response.result);
//  }).catch((error) => console.log(error));

// Modify CORS config
// cloudant.putCorsConfiguration({ enableCors: true,  origins: ['https://example.com'] }).then(response => {
//  console.log(response.result);
//  }).catch((error) => console.log(error));

// Retrieve an attachment
// cloudant.getAttachment({
//   db: '<enter-db-name>',
//   docId: 'small-appliances:100001',
//   attachmentName: 'product_details.txt'
// }).then(response => {
//   let attachment = response.result as Readable;
//   attachment.pipe(process.stdout);
// }).catch((error) => console.log(error));

// Create or modify an attachment
// const stream = new Readable();
// stream.push('This appliance includes...');
// stream.push(null);

// cloudant.putAttachment({
//   db: '<enter-db-name>',
//   docId: 'small-appliances:100001',
//   attachmentName: 'product_details.txt',
//   attachment: stream,
//   contentType: 'text/plain'
// }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Delete an attachment
// cloudant.deleteAttachment({
//   db: '<enter-db-name>',
//   docId: 'small-appliances:100001',
//   attachmentName: 'product_details.txt',
//   rev: '4-1a0d1cd6f40472509e9aac646183736a'
// }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve shard info
// cloudant.getShardsInformation({ db: 'diamonds' }).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve shard info for a specific doc
// cloudant.getDocumentShardsInfo({db: '<enter-db-name>', docId: 'small-appliances:1000042'}).then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve list of running task
// cloudant.getActiveTasks().then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve info whether the server is up
// cloudant.getUpInformation().then(response => {
//   console.log(response.result);
// }).catch((error) => console.log(error));

// Retrieve activity tracker info
// cloudant.getActivityTrackerEvents().then(response => {
//   console.log(response.result);
// });

// Modify activity tracker
// cloudant.postActivityTrackerEvents({ types: ['management'], }).then(response => {
//   console.log(response.result);
// });

//  }
// main(dct)

// function getDbs(cloudant) {
//    cloudant
//      .getAllDbs()
//      .then((body) => {
//        body.forEach((db) => {
//          dbList.push(db);
//        });
//      })
//      .catch((err) => {
//        console.log(err);
//      });
//  }

// Basic Authentication
// const { CloudantV1 } = require('@ibm-cloud/cloudant');
// const { BasicAuthenticator } = require('ibm-cloud-sdk-core');
// const authenticator = new BasicAuthenticator({
//     username: '{username}',
//     password: '{password}'
// });

// Error handling
// service.CloudantMethod(params)
//   .then((response) => {
//     console.log(resonpse.status) // .result
//   })
//   .catch(error => {
//     if (error.code !== undefined && error.code === "ERR_INVALID_ARG_VALUE") {
//       // The request was not sent, so there is no error status code, text and body
//       console.log("Invalid argument value: \n" + error.message);
//     } else {
//       console.log("Error status code: " + error.status);
//       console.log("Error status text: " + error.statusText);
//       console.log("Error message:     " + error.message);     // generic error message
//       console.log("Error details:     " + error.body)         // the error response body as text
//     }
//   });
