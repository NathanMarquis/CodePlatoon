exports.charCount = function (word) {
    let wordArr = word.split('').sort().filter(elem => elem !== ' ') //Word put in array alphabetically and without spaces
let wordObj = {}
    for (let character of wordArr){
        if(character in wordObj === false) {
            wordObj[character] = 1
        } else {
            wordObj[character]++
        }
    }
    let objArr = Object.entries(wordObj).sort(function(a,b){
        if (a[1] === b[1]){
            if(a[0] > b[0]){return 1}
            if(a[0] < b[0]){return -1}
            if(a[0] === b[0]){return 0}
        }
        if (a[1] > b[1]){ return -1}
        if (a[1] < b[1]){ return 1}
    })
    // console.log(objArr)
    return objArr
    }
    

// console.log(exports.charCount('hello world'))