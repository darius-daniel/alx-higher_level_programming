#!/usr/bin/node
const dict = require('./101-data').dict;
const entries = Object.entries(dict);
const newDict = {};

for (const nbOccurrence of Object.values(dict)) {
  if (Object.keys(newDict).includes(nbOccurrence) === false) {
    const logInfo = entries.filter((entry) => entry[1] === nbOccurrence);
    const userIds = [];
    for (const user of Object.values(logInfo)) {
      userIds.push(user[0]);
    }
    newDict[nbOccurrence] = userIds;
  }
}

console.log(newDict);
