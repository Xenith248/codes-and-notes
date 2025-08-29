//callback

function doSomethingWithCallback(callback) {
    setTimeout(() => {
        callback("Task done using callback!");
    }, 1000); // Simulates a delay of 1 second
}

doSomethingWithCallback((message) => {
    console.log(message); // Output: Task done using callback!
});


//promise

function doSomethingWithPromise() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Task done using promise!");
        }, 2000); // Simulates a delay of 1 second
    });
}

doSomethingWithPromise().then((message) => {
    console.log(message); // Output: Task done using promise!
});

