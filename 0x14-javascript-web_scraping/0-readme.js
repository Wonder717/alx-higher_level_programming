#!/usr/bin/node

/**
 * Script reads and prints the content of a file
 * first argument is the file path
 * If an error occurred during the reading, print the error object
 */

const fs = require('fs');

const filePath = process.argv[2];
try {
  const data = fs.readFileSync(filePath, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
