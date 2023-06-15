#!/usr/bin/node
const fs = require('fs');
const files = process.argv.slice(2);

fs.readFile(files[0], (err, data1) => {
  if (err) {
    throw err;
  } else {
    fs.writeFile(files[2], data1, (err) => {
      if (err) throw err;
    });
  }
});

fs.readFile(files[1], (err, data2) => {
  if (err) {
    throw err;
  } else {
    fs.appendFile(files[2], data2, (err) => {
      if (err) throw err;
    });
  }
});
