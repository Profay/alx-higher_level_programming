#!/usr/bin/node
// Write a script that reads and prints the content of a file.
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];
fs.writeFile(path, content, 'utf8', function (error) {
  if (error) {
    console.log(error.message);
  }
});
