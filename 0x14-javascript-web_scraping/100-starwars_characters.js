#!/usr/bin/node
// Write a script that reads and prints the content of a file.
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const request = require('request');
request.get(('https://swapi-api.hbtn.io/api/films/' + process.argv[2]), function (error, response, body) {
  if (error == null) {
    const movies = JSON.parse(body);
    for (let i = 0; i < movies.characters.length; i++) {
      request.get(movies.characters[i], function (error, respose, body) {
        if (error == null) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
