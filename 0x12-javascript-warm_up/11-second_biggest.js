#!/usr/bin/node
const integers = [];

for (let i = 0; i < process.argv.length; i++) {
  if (isNaN(process.argv[i]) === false) {
    integers.push(process.argv[i]);
  }
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(integers.sort()[integers.length - 2]);
}
