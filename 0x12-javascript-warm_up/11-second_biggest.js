#!/usr/bin/node

const arg_num = process.argv.length;
if (arg_num <= 3) {
  console.log(0);
} else {
  console.log(process.argv.sort()[arg_num - 2]);
}
