/**
 * Get all dealerships
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');
// Load and provide the path where the credentials stored 
const dotenv = require('dotenv').config({path: require('find-config')('../../.env')})

// Read credentials 
dct = {
  IAM_API_KEY: process.env.APIKEY,
  COUCH_URL: process.env.URL,
  }


async function main(params) {
      const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
      const cloudant = CloudantV1.newInstance({
          authenticator: authenticator
      });
      cloudant.setServiceUrl(params.COUCH_URL);
 
      try  {
          let dbList = await conn.postAllDocs({ db: dbname, includeDocs: true, limit: 10 });
          // console.log(dbList.result.rows.length)
          return {
                  statusCode: 200,
                  headers: { 'Content-Type': 'application/json' },
                  body: dbList.result.rows
                 };

      } catch (error) {
          // console.log(error)
          return { error: error.description };
      }




      // try {
      //   let dbList = await cloudant.getAllDbs();
      //   console.log({ "dbs": dbList.result });
      //   return { "dbs": dbList.result };
      // } catch (error) {
      //     return { error: error.description };
      // }
}

main(dct)




// // Q&A
// function main(params) {

//     return new Promise(function (resolve, reject) {
//         const { CloudantV1 } = require('@ibm-cloud/cloudant');
//         const { IamAuthenticator } = require('ibm-cloud-sdk-core');
//         const authenticator = new IamAuthenticator({ apikey: process.env.APIKEY })
//         const cloudant = CloudantV1.newInstance({
//             authenticator: authenticator
//         });

//         cloudant.setServiceUrl(process.env.URL);
        
//         if (params.st) {
//             // return dealership with this state 
//             cloudant.postFind({db:'django-dealerships',selector:{st:params.st}})
//             .then((result)=>{
//               console.log(result.result.docs);
//               let code = 200;
//               if (result.result.docs.length == 0) {
//                   code = 404;
//               }
//               resolve({
//                   statusCode: code,
//                   headers: { 'Content-Type': 'application/json' },
//                   body: result.result.docs
//               });
//             }).catch((err)=>{
//               reject(err);
//             })
//         } else if (params.id) {
//             id = parseInt(params.dealerId)
//             // return dealership with this state 
//             cloudant.postFind({
//               db: 'django-dealerships',
//               selector: {
//                 id: parseInt(params.id)
//               }
//             })
//             .then((result)=>{
//               console.log(result.result.docs);
//               let code = 200;
//               if (result.result.docs.length == 0) {
//                   code = 404;
//               }
//               resolve({
//                   statusCode: code,
//                   headers: { 'Content-Type': 'application/json' },
//                   body: result.result.docs
//               });
//             }).catch((err)=>{
//               reject(err);
//             })
//         } else {
//             // return all documents 
//             cloudant.postAllDocs({ db: 'django-dealerships', includeDocs: true, limit: 10 })            
//             .then((result)=>{
//               console.log(result.result.rows);
//               let code = 200;
//               if (result.result.rows.length == 0) {
//                   code = 404;
//               }
//               resolve({
//                   statusCode: code,
//                   headers: { 'Content-Type': 'application/json' },
//                   body: result.result.rows
//               });
//             }).catch((err)=>{
//               reject(err);
//             })
//       }
//     }
//     )}

// main(this)





// // // //  Get dealerships values
// function connectServer() {
//       const authenticator = new IamAuthenticator({ apikey:"API_KEY" })
//       const cloudant = CloudantV1.newInstance({
//           authenticator: authenticator
//       });
//       cloudant.setServiceUrl("https://5a588e5c-d74b-4305-80cc-e6cadb6069d6-bluemix.cloudantnosqldb.appdomain.cloud");
//       // console.log(cloudant)
//       return cloudant;
// }


// var tasks = [
//     //  get db with selector
//     async (conn, dbname, select_value) => {
//       const res = await conn.postFind({db:dbname, selector:select_value});
//       if (res.result.docs !== [] ) {
//         const slt = {
//               statusCode: 200,
//               headers: { 'Content-Type': 'application/json' },
//               body: res.result.docs
//             };
//         return slt;
//         }  
//       else {
//         let code = 404;
//         console.log(code)
//         return {
//           statusCode: code,
//           headers: { 'Content-Type': 'text/html' },
//           body: `<html><body><h1>Not Found ${code}</h1><p>Or file was removed.</p></body></html>`
//         }
//       }
//     },

//     // get values of db
//     async (conn, dbname) => {
//       try  {
//           let dbList = await conn.postAllDocs({ db: dbname, includeDocs: true, limit: 10 });
//           // console.log(dbList.result.rows.length)
//           return {
//                   statusCode: 200,
//                   headers: { 'Content-Type': 'application/json' },
//                   body: dbList.result.rows
//                  };

//       } catch (error) {
//           // console.log(error)
//           return { error: error.description };
//       }
//     },
    
//     // get all DB name 
//     async (conn) => {
//       try {
//         let dbList = await conn.getAllDbs();
//         // console.log({ "dbs": dbList.result.length });
//         return { 
//               statusCode: 200,
//               headers: { 'Content-Type': 'application/json' },
//               body: dbList.result };
//       } catch (error) {
//           // console.log(error);
//           return { error: error.description };
//       }
//     }
// ]

// const output = async function(conn, dbname, selector) {
//   return await Promise.all(tasks.map(p => p(conn, dbname, selector)));
// }

// selected = {"state": "Texas"};
// output(connectServer(), "django-dealerships", selected);


// // // 
// const selectValue = async function(conn, dbname, select_value) {
//       console.log(dbname, select_value)
//       const res = await conn.postFind({db:dbname, selector:select_value});
//       if (res.result.docs !== [] ) {
//         console.log(res.result.docs.length) //,'\t', dbList.result.rows.length);
//         const slt = {
//               statusCode: 200,
//               headers: { 'Content-Type': 'application/json' },
//               body: res.result.docs
//             };
//         return slt;
//         }  
//       else {
//         let code = 404;
//         console.log(code)
//         return {
//           statusCode: code,
//           headers: { 'Content-Type': 'text/html' },
//           body: `<html><body><h1>Not Found ${code}</h1><p>Or file was removed.</p></body></html>`
//         }
//       }
// }


// const getAllValues= async function(conn, dbname) {
//         //   Retrieve leaderships values -- 10 rows
//       try  {
//           let dbList = await conn.postAllDocs({ db: dbname, includeDocs: true, limit: 10 });
//           console.log(dbList.result.rows.length)
//           return {
//                   statusCode: 200,
//                   headers: { 'Content-Type': 'application/json' },
//                   body: dbList.result.rows
//                  };

//       } catch (error) {
//           console.log(error)
//           return { error: error.description };
//       }
// }



// Clue TODO something
// function wait(ms, data) {
//     console.log('Starting task:', data, ms);
//     return new Promise(resolve => setTimeout(resolve, ms, data));
// }

// var tasks = [
//     async () => {
//         var result = await wait(1000, 'moose');
//         // do something with result
//         console.log(result);
//     },
//     async () => {
//         var result = await wait(500, 'taco');
//         // do something with result
//         console.log(result);
//     },
//     async () => {
//         var result = await wait(5000, 'burp');
//         // do something with result
//         console.log(result);
//     }
// ]

// const output = async function() {
//   return await Promise.all(tasks.map(p => p()));
// }
// output();
// console.log('done');


// const selector1 = {"state": "California"};
// selectValue(connectServer(), "django-dealerships", selector1);
// getAllValues(connectServer(), "django-reviews");


// FOr test
// const correctAsync500ms = () => {
//   return new Promise(resolve => {
//     setTimeout(resolve, 500, 'correct500msResult');
//   });
// };

// const correctAsync100ms = () => {
//   return new Promise(resolve => {
//     setTimeout(resolve, 100, 'correct100msResult');
//   });
// };

// const rejectAsync100ms = () => {
//   return new Promise((resolve, reject) => {
//     setTimeout(reject, 100, 'reject100msError');
//   });
// };

// const asyncInArray = async (fun1, fun2) => {
//   const label = 'test async functions in array';
//   try {
//     console.time(label);
//     const p1 = fun1();
//     const p2 = fun2();
//     const result = [await p1, await p2];
//     console.timeEnd(label);
//   } catch (e) {
//     console.error('error is', e);
//     console.timeEnd(label);
//   }
// };

// const asyncInPromiseAll = async (fun1, fun2) => {
//   const label = 'test async functions with Promise.all';
//   try {
//     console.time(label);
//     let [value1, value2] = await Promise.all([fun1(), fun2()]);
//     console.timeEnd(label);
//   } catch (e) {
//     console.error('error is', e);
//     console.timeEnd(label);
//   }
// };

// (async () => {
//   console.group('async functions without error');
//   console.log('async functions without error: start')
//   await asyncInArray(correctAsync500ms, correctAsync100ms);
//   await asyncInPromiseAll(correctAsync500ms, correctAsync100ms);
//   console.groupEnd();

//   console.group('async functions with error');
//   console.log('async functions with error: start')
//   await asyncInArray(correctAsync500ms, rejectAsync100ms);
//   await asyncInPromiseAll(correctAsync500ms, rejectAsync100ms);
//   console.groupEnd();
// })();
