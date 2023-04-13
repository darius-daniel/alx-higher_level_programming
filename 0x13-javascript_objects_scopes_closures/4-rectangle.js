#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 1; i <= this.height; i++) {
      let line = '';

      for (let j = 1; j <= this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate() {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle
