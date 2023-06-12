#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable quotes */

const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;

addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
