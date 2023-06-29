#!/usr/bin/node
/* eslint-disable semi, no-console */
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destination = process.argv[4];

const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');
const combinedContent = contentA + contentB;

fs.writeFileSync(destination, combinedContent);

console.log(`Successfully concatenated ${fileA} and ${fileB} into ${destination}`);
