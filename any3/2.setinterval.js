let count = 0;
const intervalId = setInterval(() => {
  count++;
  console.log("Count:", count);
  if (count >= 5) {
    clearInterval(intervalId); // Stop the interval after 5 iterations
  }
}, 1000);
console.log("start");