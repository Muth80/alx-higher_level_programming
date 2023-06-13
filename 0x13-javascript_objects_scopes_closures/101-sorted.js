#!/usr/bin/node
/* eslint-disable semi, no-console */
const { dict } = require('./101-data');

const sortedDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (sortedDict[occurrence]) {
    sortedDict[occurrence].push(userId);
  } else {
    sortedDict[occurrence] = [userId];
  }
}

console.log(sortedDict);
