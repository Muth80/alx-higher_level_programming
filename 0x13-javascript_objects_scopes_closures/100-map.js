#!/usr/bin/node
/* eslint-disable semi, no-console */
const { list } = require('./100-data');

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
