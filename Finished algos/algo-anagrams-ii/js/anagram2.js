exports.anagramsFor = function (word, listOfWords) {

    let sortFunction = (elem) => { //Function to sort words
        return elem.toUpperCase().split('').filter(letter => letter !== ' ').sort().join('')
    }

    const mainWord = sortFunction(word)
    // console.log(mainWord)

    let ansArr = []
    let count = 0
    for (let piece of listOfWords) {
        let sortedWord = sortFunction(piece)
        if (mainWord === sortedWord){
            ansArr.push(listOfWords[count])
        }
        count++
    }
    return ansArr
}

//console.log(exports.anagramsFor('Greeek', ['Egr eek', 'gre eke', 'cancer', 'i'])) //=== false)

// Create an array of objects with counts in them from FUNCTION
// 