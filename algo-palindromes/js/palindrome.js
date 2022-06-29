exports.palindrome = function(word) {
    let wordArr = []
    if ((word*1) == word ){
        wordArr = word.toString().split('')
        //  console.log('crap')
    } else {
        wordArr = word.toUpperCase().split('').filter(elem => (elem >= 'A' && elem <= 'Z'))
    }
    let reverseWordArr = []
    wordArr.forEach(elem => reverseWordArr.unshift(elem))

    //  console.log(wordArr, reverseWordArr)

    if (wordArr.join('') === reverseWordArr.join('')) {return true} 
    else {return false}
    

    
    
};

// console.log(exports.palindrome("Sore was I ere I saw Eros."))