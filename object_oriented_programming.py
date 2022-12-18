# Programming paradigm (way) of solving problems using the concepts of classes and objects
# Functional Programming --> Define a function or group of functions to achieve/solve a given problem statement 

# Class --> A template using which you can create real-life entities (Object)

# A class and object has 'IS-A' relationship

# class Dog:
#     # Attributes / Properties / Data Members -> data related to the classs being built

#     # Constructor ( __init__() ) --> Help you define properties for each object being created
#     # self --> Class Reference
#     def __init__(self, name, breed, noOfLegs, color):
#         # Defining the properties
#         # self.propName = parameter

#         self.dogName = name
#         self.dogBreed = breed
#         self.dogLegs = noOfLegs
#         self.dogColor = color

#     # Functionalities that each object will perform -> Functions --> Methods
#     def getDetails(self):
#         print('This is a {}. Its name is {}, and his color is {}'.format(self.dogBreed, self.dogName, self.dogColor) )

#     def walk(self):
#         print('{} is walking'.format(self.dogName))

#     def bark(self):
#         print('{} is barking...'.format(self.dogName))

# # How to create an Object
# # SYNTAX --> ObjectName = ClassName(values to the properties)

# germanShepheard = Dog('Jack', 'GSD', 4, 'Brown')
# print(germanShepheard)
# germanShepheard.getDetails()
# germanShepheard.bark()
# germanShepheard.walk()

# bullDog = Dog('Jill', 'Bull Dog', 4, 'Black')
# print(bullDog)
# bullDog.getDetails()
# bullDog.bark()
# bullDog.walk()

# Number --> num1, num2
# Operations -> sum, diff, product, division, modulous, power, ...

# 1. Encapsulation --> To build a single unit, a unit which conatins all the properties and methods called a class.
class Number:
    # Default Constructor --> which does not accept any parameter while create the object
    # def __init__(self):
    #     self.propertyOne = 100
    #     self.propertyTwo = 200

    # Parameterized Constructor --> which is taking parameters while creating objects 
    def __init__(self, num1, num2):
        self.__add = 0
        self.num1 = num1
        self.num2 = num2

    # Methods defined the class
    def sum(self):
        self.__add = self.num1 + self.num2
        return self.__add

    def differnce(self):
        return self.num1 - self.num2

    def product(self):
        return self.num1 * self.num2

    def __completeDivide(self):
        return self.num1 // self.num2

    def divide(self):
        return self.__completeDivide()

    def modulous(self):
        return self.num1 % self.num2

    def power(self):
        return self.num1 ** self.num2
    
# Creating the Object
myObject = Number(45, 5)
print( myObject.sum() )
# print( myObject.add )
print( myObject.differnce() )
print( myObject.product() )
print( myObject.divide() )
print( myObject.__completeDivide() )
print( myObject.modulous() )
print( myObject.power() )

# Principles of OOPs | 4 Pillars of OOPs

# 1. Encapsulation
# 2. Abstraction
# 3. Polymorphism
# 4. Inheritance