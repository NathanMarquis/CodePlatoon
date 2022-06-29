exports.factorial = function (num) {
    if (num === 1 || num === 0) {
        return 1
    } else {
        return num * this.factorial(num - 1)
    }
}






// if (num === 1 || num === 0) {
//     answer2 = answer
//     answer = 1
//     //console.log('answer2 ' + answer2)
//     return answer2 //does not work!
// } else {
//     answer *= num
//     //console.log(answer)
//     return answer * this.factorial(num-1)
// }
// return answer2
// }




// console.log(factorial(0))






// let answer = 1
// let number = num
// function factorio(num) {
//     if (num === 1 || num === 0) {
//         return answer
//     } else {
//         answer *= num
//         console.log(answer)
//     }
//     factorio(num - 1)
// }
// factorio(number)

// return answer
// };