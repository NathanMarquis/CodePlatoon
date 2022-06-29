
DAY 2: Javascript
It is the only language available for website front end
    Can run servers with node.js
English words with parts of speech is like JS statements composed of mostly values
    Values have types such as primitive (num, string, boolean, null, undefined) and complex (object, array, function)

## Variable declaration
    Three ways to declare variables:
        Var - used to be only option, 
        Let - can be reassigned
        Const - cannot reassign variable

## Primitive data types:

    Numbers: One type in JS sadly, so no distinction between floats and integers
        Literal numbers are numbers on their own

        BE VERY CAREFUL BECAUSE JS SUCKS AT MATH WITH FLOATS

        Arithmetic operators are binary such as +, -, %, *, /
    
    Strings: Between quotes to make literal string
        \ can go before character to make it have special meaning, or remove the special meaning
        `` can span multiple lines and interpolate variables inside

        String operators:
            string concatnation is 'lala' + 'lolo'
            string interpolation with ``

    Booleans: True or false
        Logic operators such as && or || 
        ! as unary operator
        !! can be used to convert value to boolean
        === to be used usually to compare
        == RARELY USED BECAUSE INTERPRETATION

## Complex data types:

    Arrays: Ordered list of values

    Objects: Unordered list of key-value pairs

## Functions

    Use fat arrow functions when possible const yo = () => {}
    Only use function() when NEEDED

    Functions attached to object is a method
        String built-in methods
            .includes, etc...
            .slice can also be used to copy
            .split to convert string to array
          

JS can be used for everything front end, but mostly interactive elements
    HTML and CSS for visuals, and HTML can be incorporated mostly in JS
