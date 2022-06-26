// REMEMBER TO PSEUDOCODE
const pad = (array, minSize, value=null) => {
    let ansArr = array
    for(let i = ansArr.length; i < minSize; i++){
        ansArr.push(value)
    }
    return ansArr
}

// console.log(pad([1, 2, 3], 0, 'apple'))
