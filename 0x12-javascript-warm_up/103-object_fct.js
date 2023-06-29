#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable quotes */

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.incr = function () {
  this.value += 1;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
