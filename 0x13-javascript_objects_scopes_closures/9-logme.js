#!/usr/bin/node
/* eslint-disable semi, no-unused-vars */
let count = 0;

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
