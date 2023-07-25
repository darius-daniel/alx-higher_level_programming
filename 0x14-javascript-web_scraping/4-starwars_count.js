#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    for (const movie of JSON.parse(body).results) {
      for (const character of movie.characters) {
        const charID = character.split('/')[5];
        if (charID === String(18)) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
