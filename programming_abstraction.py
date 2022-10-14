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

num = 2999
# 7 --> 1, 2, 3, 4, 5, 6, 7
# count = 0 -> 1 --> 2
counter = 0
for index in range(1, num+1):
    if num % index == 0:
        counter = counter + 1

if counter == 2:
    print(num, "is a PRIME number")
else:
    print(num, "is NOT a PRIME number")