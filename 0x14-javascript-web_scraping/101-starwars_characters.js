#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
console.log(url);

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        for (const characterURL of JSON.parse(body).characters) {
            request(characterURL, (err, res, b) => {
                if (err) {
                    console.error(err);
                } else {
                    console.log(JSON.parse(b).name);
                }
            });
        }
    }
});
