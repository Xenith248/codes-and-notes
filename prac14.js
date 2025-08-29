function myDisplayer(something) {
    console.log(something);
}

function myProcessor(string1, string2, myCallback) {
    setTimeout(() => {
        let sum = string1 + string2; // Operation happens after a delay
        myCallback(sum); // Calls the callback after the timeout
    }, 2000); // 2-second delay
}

console.log("Starting calculation..."); //calling 1st operation
myProcessor("this is a string", " im adding another string >:)", myDisplayer); //calling 2nd !!ASYNC!! operation
console.log("Calculation initiated..."); //calliong 3rd operation
