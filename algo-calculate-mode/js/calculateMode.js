const calculateMode = (arr) => {
    let ansArr = []
    let countArr = arr
    let countObj = {}
    for (let elem of countArr) {
        if (elem in countObj === false) {
            countObj[elem] = 1
        } else {
            countObj[elem]++
        }
    }
    let mostFrequentNumber = Math.max(...Object.values(countObj))
    for (let char in countObj){
        if(countObj[char] === mostFrequentNumber){
            ansArr.push(Number(char) || char)
        }
    }
    // console.log(countObj)
    return ansArr
}

console.log(calculateMode([0, 1, 2, 3, 4, 4, -1, 1.5])) 
console.log(calculateMode([-1, -2, -3, -5, -5, -5])) 
console.log(calculateMode([0, 1, 2, 3, 4, 5, -1, 1.5])) 
console.log(calculateMode([100, 2, 100, 2, 4, 4, -1, 1.5])) 
