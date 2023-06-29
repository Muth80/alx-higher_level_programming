#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable quotes */

function addMeMaybe(number, theFunction) {
  number += 1;
  theFunction(number);
}

module.exports = { addMeMaybe };
