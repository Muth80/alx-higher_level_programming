#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable quotes */

function findSecondBiggest(arr) {
  if (arr.length <= 1) {
    return 0;
  }

  let max = Number.NEGATIVE_INFINITY;
  let secondMax = Number.NEGATIVE_INFINITY;

  for (let i = 0; i < arr.length; i++) {
    const num = parseInt(arr[i]);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  return secondMax;
}

const args = process.argv.slice(2);
const result = findSecondBiggest(args);
console.log(result);
