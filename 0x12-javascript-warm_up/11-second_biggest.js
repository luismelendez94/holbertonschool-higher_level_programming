#!/usr/bin/node
const arg = process.argv;
const array = arg.filter(function (x) { return (!isNaN(x)); });

if (arg.length <= 3) {
  console.log(0);
} else {
  for (let idx = 0; idx < array.length; idx++) {
    array[idx] = parseInt(array[idx]);
  }
  bubbleSort(array);
}

function bubbleSort (arr) {
  let temp;

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  console.log(arr[arr.length - 2]);
}
