#!/usr/bin/node
const fs = require('fs');

function writeToFile(filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

// Check if the script was invoked with the correct number of arguments
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file_path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

writeToFile(filePath, content);
