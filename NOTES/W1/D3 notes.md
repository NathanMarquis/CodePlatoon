Python intro

No keywords to define variables
    variable = value
    It will not create global variables like JS
    Python writing style is snake_case:  a_small_number = 4

NUMBERS: Manipulate numbers like JS
    BUT there is no === or !==
    ONLY == and !=

STRINGS: '' or "" normally 

    multiline_strings = """
    lalala 
    lala 
    la
    """

    string interpolation
        print( f"Lets go {activity} on {day} afternoon!" )

BOOLEANS: True or false

LISTS: same formatting as JS with ['lala', 'lolo']
    index -1 is first from the end
        array[-1] would be 'lolo'
    
    slicing would be array[1:3] to take items from idx1 to idx 3
        [:3] would slice everything before idx3
        [3:] would slice everything idx3 and after

TUPLE: like lists but immutable
    a_tuple = (1, 2, 3)
    change to tuple: tuple(list_name)
    change to list: list(tuple_name)

DICTIONARY
    Roughly like object in JS
    Set of key: value pairs
    REQUIRES QUOTES FOR KEYS
    Bracket notation to access such as: dict['one']
    dict = {
        'one': 1,
        'two': 2
    }

FUNCTIONS
    Define with: 

    def function_name(args):
        return code
        
    if an argument has a *, it will take any number of positional args and use it as a tuple of them

    if an argument has a **, it will take any number of positional parameters /* usually used as **kwargs *\

CONDITIONALS
    'and, or' used instead of && ||

    if blabla == true:
        do this
    elif blabla == false:
        do this instead
    else:
        do this alright!
LOOPS
    for x in random_list:
        do this

    for x in range(10): #useful for algorithmic challenges to do 10
        do thissssss
    
    for i, x in enumerate(my_list): #enumerate makes key:value pairs
        do dis
    
    while x > 0:
        do this
        x = x - 1