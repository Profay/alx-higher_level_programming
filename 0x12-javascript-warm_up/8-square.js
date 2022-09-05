#!/usr/bin/node
const argv = process.argv;
const value = parseInt(argv[2], 10);
if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('X'.repeat(argv[2]));
  }
}
