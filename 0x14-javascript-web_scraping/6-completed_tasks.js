#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const output = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (Object.keys(output).includes(`${task.userId}`)) {
          output[`${task.userId}`]++;
        } else {
          output[`${task.userId}`] = 1;
        }
      }
    }
    console.log(output);
  }
});
