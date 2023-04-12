#!/usr/bin/node
if (!process.argv[2] || !parseInt(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    console.log('C is fun');
  }
}
