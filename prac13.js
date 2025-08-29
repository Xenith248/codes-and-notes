// A basic function to greet a user
function adding(num1,num2) {
    console.log(num1+num2);
}

// Call the function
adding ("this is a "," normal funtion")


// Define the callback function
function myDisplayer(something) {
    console.log(something);
  }
  
  function myCalculator(string1, string2, myCallback) {
    let sum = string1 + string2;
    myCallback(sum);
  }
  
  myCalculator("this is a string", " added with and displayed with a callback funtion", myDisplayer);