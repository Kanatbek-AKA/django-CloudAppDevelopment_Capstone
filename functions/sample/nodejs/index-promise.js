/**
 * Get all dealerships
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');
// const path = require('path')
const dotenv = require('dotenv')
dotenv.config({path: require('find-config')('../.env')})

dct = {
  IAM_API_KEY: process.env.APIKEY,
  COUCH_URL: process.env.URL,
}


// Connecting to Server 
function main(params) {
    const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
    });
    cloudant.setServiceUrl(params.COUCH_URL);
    return cloudant
}


// Get all DN names 
function getDbs(cloudant) {
     return new Promise((resolve, reject) => {
         cloudant.getAllDbs()  // db.list()   
             .then(body => {
                 console.log({ dbs: body.result });
                 resolve({ dbs: body.result });
             })
             .catch(err => {
                  console.log(err);
                 reject({ err: err });
             });
     });
 } 

// getDbs(main(dct))

 /*
 Sample implementation to get the records in a db based on a selector. If selector is empty, it returns all records. 
 eg: selector = {state:"Texas"} - Will return all records which has value 'Texas' in the column 'State'
 */
 // Get selected value from DB e.g. column name and its value
function getMatchingRecords(cloudant, dbname, selector) {
     return new Promise((resolve, reject) => {
         cloudant.postFind({db:dbname, selector:selector})
                 .then((result)=>{
                  // console.log({result:result.result.docs})
                   resolve({result:result.result.docs});
                 })
                 .catch(err => {
                    console.log(err);
                     reject({ err: err });
                 });
          })
 }

console.log("selected")
select = {"id": 5}
getMatchingRecords(main(dct), "django-dealerships", select)


 /*
 Sample implementation to get all the records in a db.
 */
 // Retrieve all values of the DB 
// function getAllRecords(cloudant, dbname) {
//      return new Promise((resolve, reject) => {
//          cloudant.postAllDocs({ db: dbname, includeDocs: true, limit: 10 })
//              .then((result)=>{
//                console.log({result:result.result.rows});
//                resolve({result:result.result.rows});
//              })
//              .catch(err => {
//                 console.log(err);
//                 reject({ err: err });
//              });
//          })
//  }

// console.log("details from DB")
// getAllRecords(main(dct), 'django-dealerships')


// //  Testing
// function getAllRecords(cloudant, dbname) {
//      return new Promise((resolve, reject) => {
//          cloudant.postAllDocs({ db: dbname, includeDocs: true, limit: 20 })
//              .then( (result) => {
//                  return console.log({
//                   statusCode: 200,
//                   headers: { 'Content-Type': 'application/json' },
//                   body: result.result.docs,
//                  });
//              })
//              .catch(err => {
//                 // console.log(err);
//                 return reject({err: err});
//              });
//          })
//  }


// getAllRecords(main(dct), 'django-dealerships')

