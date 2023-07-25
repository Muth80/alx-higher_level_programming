#!/usr/bin/node
const request = require('request');

// Check if the script was invoked with the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API_URL>');
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
      const tasks = JSON.parse(body);
      const completedTasks = tasks.filter(task => task.completed);
      const completedByUser = completedTasks.reduce((acc, task) => {
        if (acc[task.userId]) {
          acc[task.userId]++;
        } else {
          acc[task.userId] = 1;
        }
        return acc;
      }, {});
      console.log(completedByUser);
    } catch (parseError) {
      console.error('Error parsing JSON data:', parseError);
    }
  }
});
