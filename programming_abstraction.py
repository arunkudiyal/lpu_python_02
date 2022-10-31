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
# n = 15
# if n == 1:
#     print(1)
# elif n == 2:
#     print(1, 2)
# elif n < 0:
#     print('Enter a positive number to get the series...')
# else:
#     first = 0
#     second = 1
#     print(first, end=" ")
#     print(second, end=" ")
#     index = 2
#     while(index < n):
#         third = first + second
#         print(third, end=" ")
#         first = second
#         second = third
#         index += 1
#     print("\n")


# Q- Armstrong Number
# 153 = 1^3 + 5^3 + 3^3 
# 1 + 125 + 27 =  153

# Q - for a given number, find HCF


# TUPLES - (  )
# myList = [ 10, 20, 30, 40 ]
# print(myList[-2])
# print(myList[2])
# # LISTS ARE MUTABLE (CHANGABLE)
# myList.append(100)
# print(myList)
# print(type(myList))

# myTuple = ( 10, 20, 30, 40 )
# print(myTuple[-2])
# print(myTuple[2])
# # TUPLE ARE IMMUNATBLE (NON_CHANGABLE)
# myTuple[3] = 400 # --> DONOT DO THIS
# print(myTuple)
# print("The length of the Tuple is:", len(myTuple))
# print(type(myTuple))

# Duplicate data can be put in a Tuple
# myTuple = (100, 200, 100, True, (2+3j), "Tuple")
# print(myTuple)

# mySmallTuple = ("Tuple",)
# print(type(mySmallTuple))

# myNewTuple = tuple(("Apple", "Banana", "Pears", "Watermelon"))
# print(myNewTuple)
# print(type(myNewTuple))


# OPERATIONS ON TUPLES

# 1. Tuple Contactenation
# tup1 = ("Val1", "Val2", "Val3")
# tup2 = ("Val4", "Vala5")

# tup3 = tup1 + tup2
# print(tup3)
# print(type(tup3))


# 2. Tuple Nesting
# nestedTuple = ( (10, 20, 30), ("Val1", "val2", "Val3"), (True, False) )
# print(nestedTuple)

# tup1 = ("Val1", "Val2", "Val3")
# tup2 = ("Val4", "Vala5")
# newNestedTuple = ( tup1, tup2 )
# print(newNestedTuple)


# 3. Repitive Tuples
# myNewTuple = ('0',) * 10
# print(myNewTuple)

# 4. Deleting a Tuple
# myNewTuple = ('0',) * 10
# print(myNewTuple)
# del myNewTuple
# print(myNewTuple)

# 5. Convert a list into a tuple
# myList = [10, 20, 30, 40, True, "Hello"]
# print(myList)
# print(type(myList))
# myConvertedTuple = tuple(myList)
# print(myConvertedTuple)
# print(type(myConvertedTuple))

# myTuple = (10, 20, 30, 40, True, "Hello")
# myConvertedList = list(myTuple)
# print(myConvertedList)

# Dictionary
# Dict --> key: item
# key -> String, item -> Any DT
# myUser = { "name": "Arun Kudiyal", "email": "arun@example.com", "designation": "SDE-2", "age": 24, "isAdult": True }
# print(myUser)
# print(type(myUser))

# myPerson = {
#     "name": "Yash Sindhu",
#     "email": "yash@example.com",
#     "designation": "SDE - II",
#     "address": {
#         "street": "Street - 102",
#         "city": "Chandigarh"
#     },
#     "comapny": "Microsoft",
#     "hobbies": ["Cycling", "Gaming", "Playing Chess"],
#     "age": 20,
#     "isAdult": True,
#     "marks": [98, 91, 87, 67, 71]
# }

# print(myPerson)

# Access each keys and item pair
# print("The designation of the person is", myPerson["designation"])
# print("The address of the person is", myPerson["address"])
# print("The hobbies of the person is", myPerson["hobbies"])
# print("The marks of the person is", myPerson["marks"])

# print("The designation of the person is", type(myPerson["designation"]))
# print("The address of the person is", type(myPerson["address"]))
# print("The hobbies of the person is", type(myPerson["hobbies"]))
# print("The marks of the person is", type(myPerson["marks"]))

# # Value of Gaming
# print("One of the hobbies of the person is", myPerson["hobbies"][1])
# print("City of the person is", myPerson["address"]["city"])

# Value of Playing Chess
# print("One of the hobbies of the person is", myPerson["hobbies"][2])
# print("One of the marks of the person is", myPerson["marks"][3])
# print(type(myPerson["hobbies"]))

# METHODS -> 
# 1. get() -> dict[""]
# print(myPerson.get("hobbies"))
# print(myPerson.get("hobbies")[1])

# 2. keys()
# print(myPerson.keys())
# myKeys = myPerson.keys()
# print(myKeys[2]) --> DONOT DO THIS | This isn;t a list -> dict_keys

# # Q -> If a person donot have a "company" key, then print that "no company listed".
# if "company" in myPerson.keys():
#     print('Company Exists')
# else:
#     print('Company not listed!')

# 3. setdefault("key", item)
# Q -> If a person has a listed company, I will print "Company Exists", if not then create a key called "company" with a default value of 'Microsoft.
# DICTONARIES ARE MUTABLE...
# if "company" in myPerson.keys():
#     print('Company Exists')
# else:
#     myPerson.setdefault("company", "Microsoft")

# print(myPerson)

# 4. items()
# print(myPerson.items()) # -> dict_items 


# 5. values() -> returns all the item values
# print(myPerson.values())

# print(myPerson.items())
# if "Microsoft" in myPerson.values():
#     print('Microsoft is the listed company')
# else:
#     print('Microsoft is NOT the listed company')

# 6. update()
# myPerson.update( {"designation": "SDE - Intern"} )
# print(myPerson)

# myPerson["designation"] = "SDE - I"
# print(myPerson)

# 7. pop("key")
# myPerson.pop("email")
# print(myPerson)

''' 
This is a
multi-line comment
'''

# SETS 
# 1. Its unordered -> Indices will not work
# 2. Duplicates are not allowed in a set
# 3. Sets are mutate

# mySet = { "This", "is", "a", "Set", "is", "This" }
# print(mySet)
# print(type(mySet))

# setToList = list(mySet)
# print(setToList)
# print(type(setToList))

# SET METHODS - 
# mySetOne = { 10, 50, 100 }
# mySetTwo = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 }

# 1. add()
# mySetOne.add("Python")
# print(mySetOne)

# 2. difference --> Insection of two sets
# print( mySetTwo.difference(mySetOne) ) 

# 3. discard() --> Delete a value of any specified elt
# mySetOne.discard("is")
# print(mySetOne)

# 4. issuperset -> True or False
# print( mySetTwo.issuperset(mySetOne) )

# 5. union()
# print( mySetOne.union(mySetTwo) )

# mySetTwo.difference_update(mySetOne)
# print(mySetTwo)