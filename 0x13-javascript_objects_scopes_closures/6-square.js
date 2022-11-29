#!/usr/bin/node
const Square5 = require('./5-square.js');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) { console.log(c.repeat(this.width)); }
    }
  }
};
