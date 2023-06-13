#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length === 0 || !parseInt(args[0])) {
  console.log('Missing number of occurences');
} else {
  let number = parseInt(args[0]);
  while (number > 0) {
    console.log('C is fun');
    number--;
  }
}
