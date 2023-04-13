#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 1; i <= this.height; i++) {
      let line = '';

      for (let j = 1; j <= this.width; j++) {
        line = line + 'X';
      }
      console.log(line);
    }
  }
}


module.exports = Rectangle
