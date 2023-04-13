#!/usr/bin/node

function factorial(n) {
  if (n === 0) {
    return 1;
  }
  return (n * factorial(n - 1));
}

if (process.argv.length < 3){
  n = 1;
} else {
  n = parseInt(process.argv[2]);
}

console.log(factorial(n));
