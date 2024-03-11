import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
  console.log("Redis client connected to the server");
});

client.HSET("HolbertonSchools", "Portland", "50", (err, data) => {
  console.log(`Reply: ${data}`);
});

client.HSET("HolbertonSchools", "Seattle", "80", (err, data) => {
  console.log(`Reply: ${data}`);
});

client.HSET("HolbertonSchools", "New York", "20", (err, data) => {
  console.log(`Reply: ${data}`);
});

client.HSET("HolbertonSchools", "Bogota", "20", (err, data) => {
  console.log(`Reply: ${data}`);
});

client.HSET("HolbertonSchools", "Cali", "40", (err, data) => {
  console.log(`Reply: ${data}`);
});

client.HSET("HolbertonSchools", "Paris", "2", (err, data) => {
  console.log(`Reply: ${data}`);
});

client.HGETALL("HolbertonSchools", (err, data) => {
  console.log(data);
});
