//LOCAL/Function

// code here can NOT use carName

function myFunction() {
    let carName = "Function";
    // code here CAN use carName
  }
  
  // code here can NOT use carName


//GLOBAL
let Name = "Global";
// code here can use carName

function myFunction() {
    console.log(Name)
// code here can also use carName
}

//BLOCK

{
    let x = 2;
    var y = 3;
  }
  // x can NOT be used here
  // y can be used here 
  console.log(x,y)