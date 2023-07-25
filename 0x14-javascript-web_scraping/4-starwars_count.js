#!/usr/bin/node
const request = require('request');

// Check if the script was invoked with the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      const wedgeAntillesMovies = movieData.results.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
      console.log(wedgeAntillesMovies.length);
    } catch (parseError) {
      console.error('Error parsing JSON data:', parseError);
    }
  }
});
