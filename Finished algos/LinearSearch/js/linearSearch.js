const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
    arrayToSearchThrough.push(i);
}
exports.linearSearch = function (valueToFind, arrayToSearchThrough) {
    //let linearSearch = function(valueToFind, arrayToSearchThrough) {

    let answer = arrayToSearchThrough.indexOf(valueToFind)
    if (answer === -1) {
        return undefined
    } return answer

};


let linearSearchGlobal = function (value, array) {
    let ansArr = []
    for (let i = 0; i < array.length; i++) {
        if (value === array[i]) {
            ansArr.push(i)
        }
    }
    if (ansArr.length === 0) return undefined

    return ansArr
}

 console.log(linearSearchGlobal(3, [1, 2, 5, 3, 6, 7, 3, 8]))
// console.log(linearSearch(3, [1, 2, 5, 6, 7, 8]))