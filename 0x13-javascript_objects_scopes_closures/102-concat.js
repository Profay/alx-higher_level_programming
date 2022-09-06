#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

fs.readFile(file1, function (err, data) {
  if (err) console.log(err);
  fs.appendFile(file3, data, function (err) {
    if (err) console.log(err);
  });
});

fs.readFile(file2, function (err, data) {
  if (err) console.log(err.stack);
  fs.appendFile(file3, data, function (err) {
    if (err) console.log(err.stack);
  });
});
