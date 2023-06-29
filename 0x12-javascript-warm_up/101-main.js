#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable quotes */

const callMeMoby = require('./101-call_me_moby').callMeMoby;

callMeMoby(3, function () {
  console.log('C is fun');
});
