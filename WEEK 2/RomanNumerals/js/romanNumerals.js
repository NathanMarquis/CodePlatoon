exports.toRoman = function(num) {

let romanStr = ''

let roman = new Map() 
roman.set('M', 1000)
roman.set('CM', 900)
roman.set('D', 500)
roman.set('CD', 400)
roman.set('C', 100)
roman.set('XC', 90)
roman.set('L', 50)
roman.set('XL', 40)
roman.set('X', 10)
roman.set('IX', 9)
roman.set('V', 5)
roman.set('IV', 4)
roman.set('I', 1)

while (num > 0) {
for(let i of roman) {
if (num >= i[1]) {
romanStr+= i[0]
num -= i[1]
break
}}}

return romanStr
};

/* ```Python
# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
# 2. Create a OUTPUT string, set to ''
# 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
# 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
# 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
# 6. If EVENLY_DIVISIBLE_TIMES >= 1
  # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
  # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
# 7. Return OUTPUT
``` */