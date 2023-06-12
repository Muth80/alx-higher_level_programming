#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable quotes */

const arg = process.argv[2];

if (arg){
	console.log(arg);
} else {
	console.log("No argument");
}
