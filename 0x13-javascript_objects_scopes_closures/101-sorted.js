#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const el in dict) {
  const key = dict[el];
  if (key in newDict) {
    newDict[key].push(el);
  } else {
    newDict[key] = [el];
  }
}
console.log(newDict);
