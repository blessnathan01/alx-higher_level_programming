#!/usr/bin/node
// Prints x times “C is fun”
const argOne = process.argv[2];
if (isNaN(Number(argOne))) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < argOne; x++) {
    console.log('C is fun');
  }
}
