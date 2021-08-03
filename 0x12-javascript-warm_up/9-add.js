#!/usr/bin/node
const process = require('process');
const args = process.argv;
const number1 = parseInt(args[2]);
const number2 = parseInt(args[3]);

console.log(add(number1, number2));

function add (a, b) {
  return (number1 + number2);
}
