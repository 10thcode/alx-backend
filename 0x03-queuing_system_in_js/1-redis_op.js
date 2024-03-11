import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log("Redis client connected to the server");
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, (err, data) => {
    if (err) {
      console.log(`Error: ${err}`);
    } else {
      console.log(`Reply: ${data}`);
    }
  });
}


function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, data) => {
    console.log(data);
  });
} 


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
