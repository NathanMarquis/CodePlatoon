// How can you make this more scalable and reusable later?
function createArrayOfNum(maxValue) {
    return Array.apply(null, {length: maxValue}).map(Number.call, Number)
  }

exports.findArmstrongNumbers = function (numbers) {
    let answerArr = []
    for (let element of numbers) {
        const item = element.toString()
        varLen = item.length
        let sum = 0
        for (let digit of item) {
            sum += (digit * 1) ** varLen
            if (sum == element) {
                answerArr.push(element)
            }
        }
    }
    return answerArr
};

console.log(exports.findArmstrongNumbers([1, 2, 3, 10]))
console.log(exports.findArmstrongNumbers([0])) //0
console.log(exports.findArmstrongNumbers(createArrayOfNum(8))) // [0, 1, 2, 3, 4, 5, 6, 7])
console.log(exports.findArmstrongNumbers(createArrayOfNum(99))) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
console.log(exports.findArmstrongNumbers(createArrayOfNum(999)))// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
