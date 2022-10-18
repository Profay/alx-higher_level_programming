#!/usr/bin/node
// Write a script that reads and prints the content of a file.
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('code: ' + error.code);
  } else if (response) {
    console.log('code: ' + response.statusCode);
  }
});
