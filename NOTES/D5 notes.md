
//JS Output would be 9 to 0. Ends at 0 because 0 is a falsy statement when it gets there
let i = 10
while (i--){
    console.log(i)
}

// When troubleshooting HTML files, ALWAYS OPEN CONSOLE FIRST

//PYTHON for html files we can use:
    python -m http.server       to make server
    open localhost:8000 on browser

//JS array.sort(function(a,b))
return positive number puts a before b
return 0 does nothing
return negative number puts b before a

Tip to assign variable to the direction ***
  let sortDirection = 1 //change to -1 to reverse
  array.sort(function(a, b))
    if( a > b) {return 1} //instead do sortDirection
    if( a < b) {return 0}
    if( a == b ){return -1} //instead do -sortDirection

//JS continue passes over everthing after it in a loop and does the next loop

//Destructive methods modify original array like push() pop()
    Nondestructive methods create new array like slice() filter()
    For some reason, sort() in JS will BOTH return new array and modify original array

//