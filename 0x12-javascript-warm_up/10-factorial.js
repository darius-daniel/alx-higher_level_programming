#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) === true) {
    return 1;
  } else if (n < 2) {
    return n;
  }

  return n * factorial(n - 1);
}

const number = parseInt(process.argv[2]);
console.log(factorial(number));
