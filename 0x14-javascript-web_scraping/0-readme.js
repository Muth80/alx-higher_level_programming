#!/usr/bin/node
const fs = require('fs');

function printFileContent(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

// Check if the script was invoked with a file path as an argument
const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

printFileContent(filePath);
