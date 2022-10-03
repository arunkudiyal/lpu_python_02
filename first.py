# Data

# Operators --> +, -, *, /
# print( 10 + 50 )
# print( 100 - 50 )
# print( 10 * 5 )
# print( 10 / 2 ) # Quotient

# # Modulous
# print( 10 % 2 ) # Remiander
# # power
# print(7 ** 2)

# print( (10 + 20) * 2 )
# print( 10 + 20 * 2 ) # Python used the concept of BODMAS for expression evaluation


# VARIBALES

# variableOne = 10 + 20
# print( variableOne * 2 )


# Diff Types of data

# r_no = 12217871
# name = "Shashvat Mishra"
# isGraduated = False
# percentage = 92.78

# print( type(r_no) ) # int
# print( type(name) ) # string
# print( type(isGraduated) )  # boolean
# print( type(percentage) )   # float

# print( 10 / 2 ) # using '/' --> Result is always in float
# print( 10 // 2 ) # using '//' --> Result is always in int


# STRING

''' This is a multi line comment '''

# stringOne = "This is String One"
# stringTwo = 'This is String Two'
# print(stringOne)
# print(stringTwo)

# Operations
# print( stringOne + " " + stringTwo )  # String Concatenation
# print( stringOne - stringTwo )  # NA
# print( stringOne * stringTwo )  # NA
# print( stringOne / stringTwo )  # NA

# stringThree = "100"
# stringFour = "10"
# print( stringThree - stringFour )  # String Concatenation
# print( stringThree * stringFour )  # String Concatenation
# print( stringThree / stringFour )  # String Concatenation


# "\n" --> next line
# myString = "pytho\n programming"

myString = "python programming"
# myString = 100
# print(myString)

# number * string
# print( 3 * myString )
# print( 5 * "Arun\n" )

# String Concat
# myNewString = myString + myString
# print(myNewString)

# print("Python" "Programming")  # STRING CONCAT --> This is Possible
# print(myString myString) --> Not Possible

# String & Indices

# print( myString[10] )
# myAlphabets = myString[10] + myString[3] + myString[11] + myString[15]
# print(myAlphabets)
# print( myString[100] )

# print( myString[-1] )
# print( myString[-2] )
# print( myString[-3] )
# print( myString[-4] )
# print( myString[-5] )

# find the length of the string --> len()

# print( "The length of myString variable is:" * len(myString) )


# SLICING (sub-string) OF STRINGS --> [ x:y ]

# print( myString[0:10] )     # x (inclusive) ; y (exclusive)
# print( myString[0:1000] )   # if the upper values is too large, the whole string is returned

# print( myString[-1:-12] )
# print( myString[-11:] )
# print( myString[4:] )


# STRING METHODS --> len( myString )