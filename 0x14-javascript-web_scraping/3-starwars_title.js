#!/usr/bin/node
const request = require('request');

// Check if the script was invoked with the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } catch (parseError) {
      console.error('Error parsing JSON data:', parseError);
    }
  }
});
