#!/usr/bin/node
const argv = process.argv;
const value = parseInt(argv[2], 10);
if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
