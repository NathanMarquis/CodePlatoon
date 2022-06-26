const fibonacci = (num) => {
    if (num <= 0) {
        return 0
    } else if (num === 1 ){
        return 1
    }
    console.log(num)
    return  fibonacci(num-2) + fibonacci(num-1)
}

console.log(fibonacci(8))
//module.exports = {fibonacci}

// 1 + 
//     1 +
//          1 +

// 0 + v
//     1 + v
//         1 +
//             2 +