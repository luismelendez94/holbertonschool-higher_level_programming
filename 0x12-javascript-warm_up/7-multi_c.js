#!/usr/bin/node
const process = require('process');
const args = process.argv;
const myVar = 'C is fun';
const number = parseInt(args[2]);

if (!number) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < number; i++) {
  console.log(myVar);
}
