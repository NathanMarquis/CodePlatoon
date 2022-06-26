exports.creditCheck = function (str) {
    let numStr = str.split('')
    for (i = numStr.length - 2; i >= 0; i--) {
        if (i % 2 === 0) {
            let intNum = numStr[i] * 2
            if (intNum > 9) {
                let minisum = 0
                for (let elem of intNum.toString()) {
                    minisum += elem * 1
                }
                intNum = minisum
            }
            numStr[i] = intNum
        }
    }
    let sum = numStr.reduce((aggie, current) => aggie + current)
    if (sum % 10 === 0) {
        return 'The number is valid!'
    } else {
        return 'The number is not valid!'
    }
}