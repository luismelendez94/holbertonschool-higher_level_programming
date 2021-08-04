#!/usr/bin/node
const SquareP = require('./5-square');
module.exports = class Square extends SquareP {
  charPrint (c) {
    let line = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
      line = '';
    }
  }
};
