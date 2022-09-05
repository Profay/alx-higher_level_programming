#!/usr/bin/node
const argv = process.argv;
const arr = [];
if (argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    arr[i - 2] = parseInt(argv[i]);
  }
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  const secondMax = Math.max.apply(null, arr);
  console.log(secondMax);
}
