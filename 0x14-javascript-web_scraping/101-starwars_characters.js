#!/usr/bin/node
const request = require('request');

// Check if the script was invoked with the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie_ID>');
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
      const characterUrls = movieData.characters;

      // Function to fetch character data from character URLs
      const fetchCharacterData = (url) => {
        return new Promise((resolve, reject) => {
          request(url, (err, res, body) => {
            if (err) {
              reject(err);
            } else if (res.statusCode !== 200) {
              reject(`Failed to fetch character data. Status code: ${res.statusCode}`);
            } else {
              const character = JSON.parse(body);
              resolve(character.name);
            }
          });
        });
      };

      // Fetch data for all characters and print their names
      Promise.all(characterUrls.map(fetchCharacterData))
        .then(names => {
          names.forEach((name, index) => {
            console.log(movieData.characters[index].name);
          });
        })
        .catch(error => {
          console.error('Error fetching character data:', error);
        });
    } catch (parseError) {
      console.error('Error parsing JSON data:', parseError);
    }
  }
});
