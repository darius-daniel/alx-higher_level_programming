#!/usr/bin/node

function add(a, b) {
  return (a + b);
}

if (process.argv.length < 4 || !parseInt(process.argv[2]) || !parseInt(process.argv[3])) {
  console.log(NaN);
} else {
  let a = parseInt(process.argv[2]);
  let b = parseInt(process.argv[3]);

  console.log(add(a, b));
}
