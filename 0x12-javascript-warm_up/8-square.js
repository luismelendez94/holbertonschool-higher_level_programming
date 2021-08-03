#!/usr/bin/node
const process = require('process');
const args = process.argv;
const myVar = 'X';
const number = parseInt(args[2]);
let string = '';

if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) {
      string += myVar;
    }
    if (i < number - 1) {
      string += '\n';
    }
  }
  console.log(string);
}
