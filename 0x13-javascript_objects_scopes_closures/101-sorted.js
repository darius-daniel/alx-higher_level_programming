#!/usr/bin/node
const dict = require('./101-data').dict;
const entries = Object.entries(dict);
const newDict = {};

for (const entry of entries) {
  if (entry[1] in Object.keys(newDict) === false) {
    const userIds = [];
    for (const e of entries) {
      if (e[1] === entry[1]) {
        userIds.push(e[0].toString());
      }
    }
    newDict[entry[1]] = userIds;
  }
}

console.log(newDict);
