exports.sumPairs = function (numList, num) {
    let ansArr = []
    let onumList = numList.sort()
    for (let i = 0; i < onumList.length; i++) {
        for (let j = 0; j < onumList.length; j++) {
            if (onumList[i] + onumList[j] === num && i !== j) {
                ansArr.push([onumList[i], onumList[j]])
            }
        }
    }
    let ansLen = ansArr.length / 2
    if (ansLen > 0) {
        return ansArr.slice(0, ansLen)
    } else {
        return 'No combinations ;('
    }
};

console.log(exports.sumPairs([1, 2, 3, 4, 4, 5, 5, 4, 3, 7, 9], 10))

