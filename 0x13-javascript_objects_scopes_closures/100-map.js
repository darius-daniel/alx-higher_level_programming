#!/usr/bin/node

const list = require('./100-data').list;
const newList = [];

for (let i = 0; i < list.length; i++) {
  newList.push(i * list[i]);
}

console.log(list);
console.log(newList);
