exports.isCharacterMatch = function (string1, string2) {

    let strToObjFunction = (str) => { //Function to change an input string into an object with number of each letter
        let strObj = {}
        let strArr = str.toUpperCase().split('')
        for (let elem of strArr) {
            if (elem in strObj) {
                strObj[elem]++
            } else if (elem in strObj === false) {
                strObj[elem] = 1
            }
        }
        return strObj
    }

    const str1Obj = strToObjFunction(string1) // Calling string to object function for inputs
    const str2Obj = strToObjFunction(string2)

    console.log(str1Obj, str2Obj)

    for (let digit in str1Obj) { // Comparing objects to see if they are the same
        if (digit === ' ') {
            //console.log('blank!') 
            continue
        } else if (digit in str2Obj === false) { // If one has a letter that the other doesnt
            return false
        } else if (str1Obj[digit] !== str2Obj[digit]) {
            return false
        }
    }
    return true
}

console.log(exports.isCharacterMatch('Greeek', 'geekre')) //=== false)
