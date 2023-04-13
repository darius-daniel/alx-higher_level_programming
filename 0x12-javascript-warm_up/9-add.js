#!/usr/bin/node

function add(a, b) {
  return a + b;
}

if (process.argv.length < 4 || !parseInt(process.argv[2]) || !parseInt(process.argv[3])) {
  console.log(NaN);
} else {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);

  console.log(add(a, b));
}
