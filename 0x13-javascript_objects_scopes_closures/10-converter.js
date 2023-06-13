#!/usr/bin/node
/* eslint-disable semi, no-unused-vars */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
