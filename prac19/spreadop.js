
// Using the Spread Operator with Arrays
const arr1 = [1, 2, 3];
const arr2 = [...arr1];  // Copying arr1 into arr2

console.log(arr2);  // [1, 2, 3]


//Using the Spread Operator with Objects
const obj1 = { name: "Alice" };
const obj2 = { age: 25 };
const mergedObj = { ...obj1, ...obj2 };  // Merging two objects

console.log(mergedObj);  // { name: "Alice", age: 25 }


//Using the Spread Operator in Function Calls
const numbers = [1, 2, 3];

function sum(a, b, c) {
    return a + b + c;
}

console.log(sum(...numbers));  // 6


//Destructuring with Spread Operator
const arr = [1, 2, 3, 4, 5];
const [first, second, ...rest] = arr;

console.log(first);  // 1
console.log(second); // 2
console.log(rest);   // [3, 4, 5]
