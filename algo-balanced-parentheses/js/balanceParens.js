balanceParens = (str) =>{
    let ansArr = []
    let counter = 0
for(let char of str) {
    if (char !== '(' || char!== ')'){
        ansArr.push(char)
    }else if (counter = false && char === '(') {
        ansArr.push(char)
    }else if (counter > 1 && char === ')')
}
}
console.log(balanceParens("(((()"))
module.exports = { balanceParens }