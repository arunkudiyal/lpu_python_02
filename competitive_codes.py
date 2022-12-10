# BITWISE OPERATORS - &(AND), |(OR), ~(NOT), ^(XOR)
# a, b = 5, 4

# '''
# 5 -> 0101
# 4 -> 0100

# AND -> 0100 -> 4
# OR -> 0101 -> 5
# NOT -> -(0101 + 1) -> -(0110) -> -6
# XOR -> 0001 -> 1

# print('Bitwise AND is -> ', a & b)
# print('Bitwise OR is -> ', a | b)
# print('Bitwise NOT is -> ', ~a)
# print('Bitwise XOR is -> ', a ^ b)


# EXAMPLES ON BITWISE --> Binary digits
# 4 bit binary representation of 9
# ...  (2^3) (2^2) (2^1) (2^0)
# 16 8 4 2 1
# 0  1 0 0 1 . -> binary(9) -> 1001

# 15 -> 8 + 4 + 2 + 1 => 001111

# AND
# no(Input) -> a, b
# a     b       O/P
# 0     0       0
# 0     1       0
# 1     0       0
# 1     1       1
# num1 = 15
# num2 = 20
# 15 -> 0 1 1 1 1
# 20 -> 1 0 1 0 0
#           AND
#    -> 0 0 1 0 0 -> 4 -> ANS
# print(num1 & num2)

# OR
# no(Input) -> a, b
# a     b       O/P
# 0     0       0
# 0     1       1
# 1     0       1
# 1     1       1
# 15 -> 0 1 1 1 1
# 20 -> 1 0 1 0 0
#           OR
#       1 1 1 1 1   -> 31 -> ANS
# print(num1 | num2)

# NOT
# no(Input) -> a
# a      O/P
# 0      1
# 1      0
# 20 -> 1 0 1 0 0
#           NOT -> -(1 0 1 0 0 + 1)
#        +      1
#       - 1 0 1 0 1 -> -21 -> ANS


# 15 -> 0 1 1 1 1
#             + 1 
#       1 0 0 0 0 -> -16 -> ANS
# num3 = -15
# print("NOT of a -ve value - ", ~num3)
# print(~num1)
# print(~num2)

# XOR
# no(Input) -> a, b
# a     b       O/P
# 0     0       0
# 0     1       1
# 1     0       1
# 1     1       0
# 15 -> 0 1 1 1 1
# 20 -> 1 0 1 0 0
#           XOR
#        1 1 0 1 1 -> 27 -> ANS
# print(num1 ^ num2)

# FUNCTIONS
# -> A way to create some re-usable block of code, which can called anytime for proceesing
# SYNTAX - def functionName(parameters):

# Q -> Create a function to add 2 numbers
# def addTwoNums(num1, num2):
#     return num1 + num2

# # Q -> To get two numbers, add them and print the cube
# val_one = int(input('enter I value -'))
# val_two = int(input('enter II value -'))
# sum_val = addTwoNums(val_one, val_two)
# print(sum_val * sum_val * sum_val)

# PRIME-PALINDROME

# I/O Formatting
# name = "Arun Kudiyal"
# age = 21
# print("hello... my name is " + name + " and I am", age, "years old!")
# f-strings
# print(f"Hello my name is {name} and I am {age} years old!")

# format()
# txt = "For only {:d} dollars!".format(0b11111)
# print(txt)

# import datetime
# print(datetime.datetime.now())

# date = datetime.datetime.now().strftime("%d")
# month = datetime.datetime.now().strftime("%B")
# year = datetime.datetime.now().strftime("%Y")

# hours = datetime.datetime.now().strftime("%H")
# minutes = datetime.datetime.now().strftime("%M")
# seconds = datetime.datetime.now().strftime("%S")
# am_pm = datetime.datetime.now().strftime("%p")
# print(f"Today is {month} {date}th, {year} ; and time is {hours}:{minutes}:{seconds} {am_pm}") 


# month_list = { 1: "Jan", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "June", 7:"July", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec" }
# inp_month = int(input("Enter the month number - "))
# print( month_list[inp_month] )

# import datetime
# date = int(input("Enter date (1-31) - "))
# month = int(input("Enter date (1-12) - "))
# year = int(input("Enter date (yyyy) - "))
# myDate = datetime.datetime(year, month, date)
# print(myDate)


# Loops -> Repitive statements

# range(a) -> Range starts with 0 and (num - 1)
# 1. FOR LOOP
# for variableName in range(upperRange):
#   EXPRESSION YOU WANT TO PERFORM IN LOOP

# for variable in range(10):
#     print(variable, end=" ")
# print("\n")

# Questions -> Find the sum of all ositive number upto the user's input
# steps = int(input("Enter the upper range - "))
# sum = 0
# for variable in range(steps):
#     # Checking if the number if even or not
#     if( variable % 2 == 0 ):
#         sum += variable

# print(sum)

# Q -> Given a set of numbers, print the numbers as a list
# steps = int(input("Enter the upper range - "))
# myList = []
# for var in range(steps):
#     # Input the values
#     value = int(input("Enter the value for the set - "))
#     # Inset each value at the end of the set
#     myList.append(value)

# for var2 in myList:
#     print(var2)

# range(a, b)
# print( range(10, 20) ) -> 10 is incluse but 20 is exclusive
# for value in range(10, 20):
#     print(value)

# Q -> Given a range, find all the prime numbers for that range
# lower = int(input("Enter the starting range - "))
# upper = int(input("Enter the ending range - "))
# prime_numbers = set()
# # 10, 11, 12, 13, .... , 19

# # 5, 6, 7, 8, 9, 10
# # variable = 15
# for variable in range(lower, upper):
#     # 2 -> 4, 2 -> 5, 2 -> 6, 2 -> 7, 2 -> 8, 2 -> 9
#     if variable > 1:
#         # variable2 -> (2 - 14)
#         for variable2 in range(2, variable):
#             if(variable % variable2) == 0:
#                 # STOP
#                 break
#         else:
#             prime_numbers.add(variable)
            
# for values in prime_numbers:
#     print(values, end=" ")

# FUNCTIONAL APPROACH -
# prime_numbers = set()
# def checkPrime(number):
#     if number > 1:
#         for i in range(2, number):
#             if(number % i == 0):
#                 break
#         else:
#             prime_numbers.add(number)

# range1 = int(input("Enter a lower range - "))
# range2 = int(input("Enter a upper range - "))
# for number in range(range1, range2):
#     checkPrime(number)

# for j in prime_numbers:
#     print(j, end=", ")

# range(a, b, c)
# for i in range(2, 21, 2):
#     print(i, end=" ")
# print("\n")

# for i in range(20, 0, -2):
#     print(i, end=" ")
# print("\n")


# PATTERN PRINTING -

# num = int(input("Enter your number value - "))
# PATTERN - 1

# *
# * *
# * * *
# * * * *
# * * * * *

# Approach - 1
# Rows
# for row in range(1, num+1):
#     # Coloumns
#     for col in range(1, row+1):
#         print('*', end=" ")
#     print("\n")

# Approach - 2
# row = 1
# col = 1
# # rows -> 1, 2, 3, 4, 5
# while(row < num+1):
#     # cols -> 
#     while(col < row+1):
#         print('*', end=" ")
#         col += 1
#     print("\n")
#     row += 1


# Approach - 3 - Using Lists
# myList = ['*', '* *', '* * *', '* * * *', '* * * * *']
# for i in myList:
#     print(i)

# PATTERN - 2

# * * * * *
# * * * *
# * * *
# * *
# *

# FUNCTIONS

# def sum(a, b):
#     # print(a + b)
#     return (a + b)

# res1 = sum(10, 20)
# res2 = sum(105, 209)

# print(sum(res1, res2))

# Return Types
# def functionName(para1: type1, para2: type2) -> returnType:
# def sum(a: int, b: int) -> int:
#     return (a + b)

# res = sum(10, 20)
# print(res)

# def square(n: int):
#     # print(n * n)
#     return n * n

# answer = square(10)
# print(answer)

# Arguments / Parameters are refernces | Refernce Parameters
# def printList(li: list):
#     li[1] = -10
#     for value in li:
#         print(value)

# myList = [100, 200, 250, 210, 500]
# print(myList)           # [100, 200, 250, 210, 500]
# printList(myList)       # 100, -10, 250, 210, 500
# print(myList)           # [100, 200, 250, 210, 500]


# myList2 = [10, 20, 30]
# print(myList2)
# memLoc(myList2) = #ABCDEF

# printList(myList2)
# printList( [10, 20, 30] ) WRONG
# printList(#ABCDEF)

# Default Arguments
# def checPrime(n: int = 1) -> str:
#     count = 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             count += 1
#     if count == 2:
#         return "Yes, it's a Prime Number"
#     else:
#         return "No, it's not a Prime Number"

# ans1 = checPrime(5)
# print(ans1)

# Keyboard Arguments | Variable Length Arguments
# Your number of arguments is variable
# def addNumbers(*args: int) -> int:
#     sum = 0
#     print(args.__len__())
#     for value in range(0, args.__len__()):
#         sum += args[value]
#     return sum

# sum1 = addNumbers(10, 20, 30, 40)
# sum2 = addNumbers(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# print('Sum1 is ', sum1)
# print('Sum2 is ', sum2)

# DOC-STRING in Functions
# def findSquare(n: int) -> int:
#     '''A utility function to find the square of any given passed argumnet or value '''
#     return n*n

# print(findSquare.__doc__)

# Anouymous Functions -> Any function which is created not by using def
# def functionName(params: type) -> return type

# Q -> Diff b/w Function & Anouymous Functions
# variableName = lambda parameters: functionBody

# findCube = lambda num1: (num1 * num1 * num1)
# ans = findCube(9)
# print(ans)



# RECURSION #
# Q :- Given a number, you are supposed to fnd the sum of the n natural numbers.
# n = 5 -> 5 + 4 + 3 + 2 + 1 = 15
# n = 4 -> 4 + 3 + 2 + 1 = ...
# n = 6 -> 6 + 5 + 4 + 3 + 2 + 1 = ...

# n = k -> k + (k-1) + (k-2) + (k-3) + .... + 1 

# Sum of n natural nos -> n(n+1) / 2

# def sumOfNatutalNumbers(n: int) -> int:
#     # Base Condition
#     if(n == 2):
#         return 3
#     else:
#         return n + sumOfNatutalNumbers(n-1)

# n = int(input('Enter any value - '))
# ans1 = sumOfNatutalNumbers(n)
# print(ans1)

# explaination

# sum(10) -> result = sum(10 - 1) -> return 10 + sum(9) -> return 10 + 45 -> return 55
# sum(9) -> result = sum(9 - 1) -> return 9 + sum(8)
# sum(8) -> result = sum(8 - 1) -> return 8 + sum(7) -> return 8 + 
#.
#.
# sum(3) -> reult = sum(3 - 1) -> return 3 + sum(2) -> return 3 + 3 -> return 6
# sum(2) -> result = sum(2 - 1) -> return 2 + sum(1) -> 2 + 1 -> return 3
# sum(1) -> 1


# Q -> given a n value, find the fibonacci series upto n 
# fib(2) -> 0 1
# fib(5) -> 0 1 1 2 3

# fib(n) -> fib(n) + fib(n-1) + fib(n-2) + fib(n-3) + ... + fib(1) + fib(0)

# IMP -> Series start from ? -> 0 & 1
# def fib_series(n: int):
#     # Base Condition
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_series(n-1) + fib_series(n-2)

# terms = int(input('enter the term - '))
# if(terms < 0):
#     print('Enter a +ve number')
# else:
#     for i in range(0, terms):
#         print(fib_series(i))

# EXPLAINATION - 
# fib_series(10) -> for(i -> 0 to 9)
#               -> i = 0 --> 0

#               -> i = 1 --> 1

#               -> i = 2 --> fib_series(1) + fib_series(0) -> 1 + 0 -> 1

#               -> i = 3 -> fib_series(2) + fib_series(1) -> fib_series(0) + fib_series(1) +    fib_series(1) -> 0 + 1 + 1 -> 2

#               -> i = 4 -> fib_series(3) + fib(2) -> (fib(2) + fib(1)) + (fib(1) + fib(0)) -> 1 + 1 + 1 + 0 -> 3



# TOWER OF HANOI --> (2^n - 1) --> (2^3 - 1) --> 8 - 1 --> 7

# A             B           C
# 3 disc

# A --> B
# A --> C

# A -> 1 {largest}
# B -> 1 {smalles}
# C -> 1 {second largest}

# B -> C
# A -> 1 {largest}
# B -> 0 {}
# C -> 2 {smalles, second largest}

# A -> B
# A -> 0 {}
# B -> 1 {largest}
# C -> 2 {smalles, second largest}

# C -> A
# A -> 1 {smallest}
# B -> 1 {largest}
# C -> 1 {second largest}

# C -> B
# A -> 1 {smallest}
# B -> 2 {largest, second largest}
# C -> 0 {}

# A -> B
# A -> 0 {}
# B -> 3 {largest, second largest, smallest}
# C -> 0 {}


# Hint 1 --> Use Recursion --> What is the base condition
# n = 3
# Hint 2 --> def TOI(n, sourceRod, destinationRod, auxRod):

# def TOH(n, sourceRod, destinationRod, auxRod):
#     # Base Condition
#     if(n == 0):
#         return

# TOH(0, 'A', 'B', 'C')


# MATH MODULE

# import math

# # Mathematical Constants
# # 1. PI = 22 / 7 = 3.14...
# print(math.pi)

# # Q:- Given a radius, find the area of a circle
# def find_circle_area(radius):
#     return (math.pi * radius * radius)

# ans = find_circle_area(10)
# print(ans)


# print(math.inf)
# print(-math.inf)

# # div =  
# if( 10e108 > math.inf ):
#     print('True')
# else:
#     print('False')

# print(f"Euler's Constant", math.e)
# print(f"Tau Constant", math.tau)

# # NaN -> Not a Number
# a = "Arun"
# b = "Kudiyal"
# def add(num1, num2):
#     if(type(num1) == 'str' or type(num2) == 'str'):
#         return math.nan
#     else:
#         return num1 + num2

# add(a, b)
# add(100, 200)


# Mathematical Methods
# import math

# def calculate_area_of_circle(radius):
#     PI = 3.14
#     return PI * radius * radius

# def calculate_area_of_circle_using_math(radius):
#     return math.pi * radius * radius

# radius = int(input('enter the value of the radius - '))
# areaOne = calculate_area_of_circle(radius)
# areaTwo = calculate_area_of_circle_using_math(radius)
# print(areaOne)
# print(areaTwo)


# Q:- Strong Numbers
# n -> upper_range -> 1000 --> 1 - 1000
# 145 -> 1! + 4! + 5!

# Function to find a factorial of a given number
# def factorial(num) -> int:
#     if(num == 0):
#         return 1
#     return num * factorial(num-1)

# # Function to check for a strng number
# def isStrong(num) -> bool:
#     # Reverse a number -> FORMULA
#     newNum = str(num)
#     # temp variable to store the sum
#     sum = 0
#     # loop can access each digit the number
#     for i in range(len(newNum)):
#         sum += factorial(int(newNum[i]))

#     if(sum == num):
#         return True
#     else:
#         return False

# # Driver Code
# n = int(input('enter an upper range - '))
# if n <= 0:
#     print('enter a +ve value')
# else:
#     for value in range(1, n+1):
#         if isStrong(value):
#             print(value, end=" ")
#     print("\n")


# Math Module
# import math

# Math Module -> Constants
# print( math.pi )
# print( math.tau )
# print( math.e )
# print( math.inf )
# print( -math.inf )

# # Methods
# # 1. ceil() & floor()
# print( math.ceil(2.55) )
# print( math.floor(2.55) )

# # 2. factorial
# print( math.factorial(5) )

# # 3. Absolute values -> fabs(number) -> float
# print( math.fabs(-10) )

# # Logarithmic operations
# x = 10
# print('e^x is - ', math.e ** x)

# print(math.log(x))
# print(math.log2(x))
# print(math.log10(x))


# # Trigonometric Functions
# x = 10
# print( math.sin(x) )
# print( math.cos(x) )
# print( math.tan(x) )

# # square root
# print( math.sqrt(25) )


# Tower of Hanoi (ToH)

# Rod -> 3 --> (A, B, C)
# n -> No of discs

# n = 1
# A --> C
# (steps --> 1)

# n = 2
# A --> B
# A --> C
# B --> C
# (steps --> 3)

# n = 3 --> (D1, D2, D3)
# D1 -> A --> C
# D2 -> A --> B
# D1 -> C --> B
# D3 -> A --> C
# [ n(A) = 0, n(B) = 2, n(C) = 1 ]
# D1 -> B --> A
# [ A -> Smallest, B -> Second Largest, C -> Largest ]
# D2 -> B --> C
# D1 -> A --> C
# (steps --> 7)

# n = 4 --> (D1, D2, D3, D4)
# D1 -> A --> B
# D2 -> A --> C
# D1 -> B --> C
# [Rod B is empty]
# D3 -> A --> B
# D1 -> C --> A
# [ D1 = A; D2 = C; D3 = B ]
# D2 -> C --> B
# D1 -> A --> B
# D4 -> A --> C
# [ D1 = B; D2 = B; D3 = B ]
# D1 -> B --> C
# D2 -> B --> A
# D1 -> C --> A
# D3 -> B --> C
# D1 -> A --> B
# D2 -> A --> C
# D1 -> B --> C
# (n = 4, steps = 15)
# { 2^n - 1 }

# n --> n; steps = 2^n - 1


# SOLUTION :-
# Statergy 1 - I have to move discs from A to B; so that i can find the largest disc and place it from A to C --> Assume that A and C are empty and all the other discs are at Rod B 

# All the disc -> 
def tower_of_hanoi(n, start_rod, aux_rod, end_rod):
    # BASE CONDITION - 
    if n == 1:
        print( "Move Disc 1 from {} to {}".format(start_rod, end_rod) )
        return
    # Plan - A
    # --> Taking largest disc from A -> Rod A is empty
    # --> Placing largest disc to C -> No other smaller discs there -> Rod C is empty
    # --> All the disc are at B
    tower_of_hanoi(n-1, start_rod, end_rod, aux_rod)
    print("Move Disc {} from {} to {}".format(n, start_rod, end_rod))

    # Plan - B
    # I will have to adjust B and C recursively by taking help of A
    tower_of_hanoi(n-1, aux_rod, start_rod, end_rod)

n = int(input('enter the number of disc - '))
tower_of_hanoi(n, 'A', 'B', 'C')