function strObjCounter(str) {
    let sampObj = {}
    for(let elem of str.toUpperCase()) {
        if (elem in sampObj) {
            sampObj[elem] ++
        } else if (elem in sampObj === false) {
            sampObj[elem] = 1
        }
    }
    for(let [key, entry] of Object.entries(sampObj)){
        //console.log([key, entry])
    }
    
return sampObj
}

//console.log(strObjCounter('Greek'))


    console.log(['a', 'A', 'z', 'Z', '!'].sort())
