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


# LISTS IN PYTHON

# Way 1 - Using [ ]
# alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f' ]
# print( alphabets )
# print( type(alphabets) )

# my_list = [ 100, 'hello', True, 2+3j ]
# print( type(my_list) )
# print( my_list )


# # Way 2 - list() constructor

# # my_list_2 = list( 'A', 'B', 'C', 'D', 'E', 'F' )
# # my_list_2 = list()
# my_list_2 = list( 'Hello' )
# print( my_list_2 )
# print( type(my_list_2) )

# Operations on the List

# alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f' ]

# Accessing values from list
# alphabets[ index ]
# print( alphabets[2] )
# print( alphabets[-2] )

# # slicing in List
# print( alphabets[2:5] ) # ['c', 'd', 'e']
# print( alphabets[-1] )
# print( alphabets[-2] )
# print( alphabets[-5:-2] ) # ['b', 'c', 'd']
# print( alphabets[-2:-5] ) # WRONG --> You can only move in the forward direction

# print( alphabets[:] )
# print( alphabets[1:] )  # [ 'b', 'c', 'd', 'e', 'f' ]
# print( alphabets[:-2] ) # [ 'a', 'b', 'c', 'd' ]


# Replacemnt Mechanism in Lists

# alphabets[2:-1] =  [ 'C', 'D', 'E' ]
# print(alphabets)

# alphabets[:] = []
# print(alphabets) 

#remove a certain part of the list
# alphabets[:-2] = []
# print(alphabets)

alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f' ]

# Built-In Operations in the list

# 1. length of the list
print( len(alphabets) ) # 6

# 2. Add an element at the end of the list
# alphabets.append(10)
# alphabets.append(20)
# alphabets.append(30)
# print( alphabets )

# # 3. Insert an element in the certain position of the list
# alphabets.insert(1, 'B')
# print(alphabets)

# 4. Add a list of elts at the end
alphabets.extend( ['g', 'h', 'i'] )
print(alphabets)

# 5. Reverse a list
# alphabets.reverse()
# print(alphabets)

# 6. Remove a value from the list
alphabets.remove('c')
alphabets.remove('d')
alphabets.remove('e')
print(alphabets)

# 7. Remove the last elt of the list --> pop()
alphabets.pop()
alphabets.pop()
print(alphabets)