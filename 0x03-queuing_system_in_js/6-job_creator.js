const kue = require('kue');
const queue = kue.createQueue();

const obj = {
  phoneNumber: "0000 0000 00",
  message: "This is the code to verify your account",
}

const job = queue.create('push_notification_code', obj).on("complete", () => {
    console.log("Notification job completed");
  }).on("failed", () => {
    console.log("Notification job failed");
  }).save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });
