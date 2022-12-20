#!/usr/bin/node
// Square class that inherits from previous square class

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let edy = 0; edy < this.height; edy++) console.log(c.repeat(this.width));
    }
  }
};
