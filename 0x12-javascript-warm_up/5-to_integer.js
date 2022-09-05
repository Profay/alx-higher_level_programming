#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2], 10);
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + value);
}
