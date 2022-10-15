# PROGRAMMING ABSTRACTIONS

# 1. conditional stamenets

# num1 = 50
# num2 = 20
# if num1 < num2:
#     print(num1, "is less than ", num2)
#     print('Hello...')
# else:
#     print(num1, "is greater than ", num2)


# Q: - Given a number, print the square of the number if the number is greater than 5
# number = 4
# if number > 5:
#     print(number * number)
# print('Hello... The code ended here!')

# Q: - Voting System
# gender = M, age is greater or equals to 21 -> He can vote
# gender = F, age is greater or equals to 18 -> She can vote


# EXPLAINATION - = -> Assignment Operator || == -> Compartive Operator 

# gender = 'm'
# age = 21

# if gender == 'M':
#     if age > 21:
#         print('He can vote!')
#     else:
#         print('Sorry! He, cannot vote!')
# elif gender == 'F':
#     if age > 18:
#         print('She can vote!')
#     else:
#         print('Sorry! She cannot vote!')
# else:
#     print('ERROR! Please write correct values of gender or age!')

# if ( gender == 'm' or gender == 'M' ) and ( age >= 0 and age >= 21 ):
#     print('He can vote!')
# elif ( gender == 'm' or gender == 'M' ) and ( age >= 0 and age < 21 ):
#     print('He cannot vote')
# elif ( gender == 'f' or gender == 'F' ) and ( age >= 0 and age >= 18 ):
#     print('She can vote')
# elif ( gender == 'f' or gender == 'F' ) and ( age >= 0 and age < 18 ):
#     print('She cannot vote')
# else:
#     print('Please input the correct values of age or gender')



# LOOPS in Python
# When you want to perform the same actions or code over multiple times

# range(integer)
# print( range(10) )  # range(0, 10)
# range(0, n-1) --> range(10) - range(0-9); range(32) -> range(0, 31)

# 1. for Loop
# for variableName in range() :
# NOTE - Everytime the loop excutes, the range changes 
# for num in range(10):
#     print(num)

# range(start, end) -> start (inc) but end (exc)
# for num in range(5, 10):
#     print(num)

# for num in range(0, 11, 2):
#     print(num)

# Q -> Check whether a given number is a prime or not
# 2, 3, 5, 7, 11, 13, ...

# num = 2999
# # 7 --> 1, 2, 3, 4, 5, 6, 7
# # count = 0 -> 1 --> 2
# counter = 0
# for index in range(1, num+1):
#     if num % index == 0:
#         counter = counter + 1

# if counter == 2:
#     print(num, "is a PRIME number")
# else:
#     print(num, "is NOT a PRIME number")


# 1. while Loop --> You donot know where the loop ends

# num = 10
# for i in range(10, 0, -1):
#     print(i)

# num = 10
# while(num > 0):
#     print(num)
#     num = num - 1

# Q - Reverse a number
# num = 1012356478
# revresed_number = 0

# while(num > 0):
#     # Step 1 - Get the last digit (num % 10 = remainder)
#     last_digit = num % 10
#     #Step 2 - Re-create the reversed_number
#     revresed_number = (revresed_number * 10) + last_digit
#     #Step 3 - Remove each last_digit from the number
#     num = num // 10

# print(revresed_number)


# Q- 1: print frist 10 even numbers
# for num in range (2, 21, 2):
#     print(num)

# num = 2
# while(num <= 20):
#     print(num)
#     # num = num + 2
#     num += 2

# Q - While Loop statemnet to print --> 105, 98, 91, ..., 7
# num = 105
# while(num >= 7):
#     print(num)
#     num -= 7

# Q- code to add first n natural number
# Q- odd / nums to n numbers
# Q- Revese a number
# Q- Print the table of a given number
# Q- Fibonaci Series till n from the user
# 0 1 1 2 3 5 8 13 19 .... n
n = 15
if n == 1:
    print(1)
elif n == 2:
    print(1, 2)
elif n < 0:
    print('Enter a positive number to get the series...')
else:
    first = 0
    second = 1
    print(first, end=" ")
    print(second, end=" ")
    index = 2
    while(index < n):
        third = first + second
        print(third, end=" ")
        first = second
        second = third
        index += 1
    print("\n")


# Q- Armstrong Number
# 153 = 1^3 + 5^3 + 3^3 
# 1 + 125 + 27 =  153

# Q - for a given number, find HCF

# Q - For a given decimal number, print the binary number
num = 10
binary = 0
n = num
while(n > 0):
    remainder = n % 2                       # reiander = 0, 1
    binary = (binary * 10) + remainder      # binary = 0
    n = n/2                                 # n = 5

print(binary)