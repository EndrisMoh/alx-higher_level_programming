#!/usr/bin/node
// Creates a Square class that inherits or extends from Rectangle class

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
