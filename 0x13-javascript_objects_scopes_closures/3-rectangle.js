#!/usr/bin/node
// Prints the parameters provided

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let edy = 0; edy < this.height; edy++) console.log('X'.repeat(this.width));
  }
};
