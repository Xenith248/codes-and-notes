let x; // variable declared but not initialized
console.log(x); // Output: undefined

function doSomething() {
  // no return statement, so the function returns undefined
}
console.log(doSomething()); // Output: undefined

let obj = {};
console.log(obj.property); // Output: undefined

//Uninitialized Variables: A variable that is declared but not initialized will have the value undefined.
//Missing Function Return: If a function does not explicitly return a value, it returns undefined by default.


