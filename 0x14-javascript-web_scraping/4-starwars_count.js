#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let movies = 0;

request(url, function (err, res, content) {
  if (err) {
    console.error(err);
  }
  for (let i = 0; i < 7; i++) {
    if JSON.parse(content).characters
	  movies++;
  }
  console.log(movies);
});
