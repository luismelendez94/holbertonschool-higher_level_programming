#!/usr/bin/node
const process = require('process');
const args = process.argv;
const number = parseInt(args[2]);

if (!number) {
  console.log(1);
} else {
  console.log(factorial(number));
}

function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
