function strObjCounter(str) {
    let sampObj = {}
    for(let elem of str.toUpperCase()) {
        if (elem in sampObj) {
            sampObj[elem] ++
        } else if (elem in sampObj === false) {
            sampObj[elem] = 1
        }
    }
return sampObj
}

console.log(strObjCounter('Greek'))