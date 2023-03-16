/**
 * Get all databases
 */

const { CloudantV1 } = require("@ibm-cloud/cloudant");
const { IamAuthenticator } = require("ibm-cloud-sdk-core");

require("dotenv").config({path: require("find-config")("../../.env")})
// I tried this one too
// const path = require("path")
// require('dotenv").config({path: path.join(__dirname: "../../.env") })                      //  undefined
// require('dotenv").config({path: path.resolve(__dirname + "../../.env") })                  // undefined
// require('dotenv").config({path: path.resolve(__dirname + "provided_full_path_to/.env") })  // undefined

dct = {
    "API_KEY": process.env.API,
    "URL" : process.env.URL
}

// Checking if the .env file values readable
console.log( dct.API_KEY )
 


function connectServer(params) {
  const authenticator = new IamAuthenticator({ apikey: params.API_KEY });
  const cloudant = CloudantV1.newInstance({
    authenticator: authenticator,
  });
  cloudant.setServiceUrl(params.URL);
  return cloudant
}

function getDbs(cloudant) {
  cloudant
    .getAllDbs()
    .then((body) => {
       console.log(body.result)
      });
    })
    .catch((err) => {
      console.log(err);
    });
}

// invoke function
// getDBs(connectServer(dct))  
