#!/usr/bin/node
/* eslint-disable semi, no-unused-vars */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
