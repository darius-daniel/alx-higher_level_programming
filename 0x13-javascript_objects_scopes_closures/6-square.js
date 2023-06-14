#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }

  charPrint (c = 'X') {
    for (let i = 1; i <= this.height; i++) {
      let line = '';
      for (let j = 1; j <= this.width; j++) {
        line = line.concat(c);
      }
      console.log(line);
    }
  }
}

module.exports = Square;
