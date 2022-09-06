#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let j = 0; j < this.width; j++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};