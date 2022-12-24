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
# class Number:
#     # Default Constructor --> which does not accept any parameter while create the object
#     # def __init__(self):
#     #     self.propertyOne = 100
#     #     self.propertyTwo = 200

#     # Parameterized Constructor --> which is taking parameters while creating objects 
#     def __init__(self, num1, num2):
#         self.__num1 = num1
#         self.__num2 = num2

#     # Methods defined the class
#     def sum(self):
#         return self.__num1 + self.__num2

#     def differnce(self):
#         return self.__num1 - self.__num2

#     def product(self):
#         return self.__num1 * self.__num2

#     # def __completeDivide(self):
#     #     return self.__num1 // self.__num2

#     def divide(self):
#         return self.__num1 / self.__num2

#     def modulous(self):
#         return self.__num1 % self.__num2

#     def power(self):
#         return self.__num1 ** self.__num2
    
# # Creating the Object
# myObject = Number(45, 5)
# print( myObject.sum() )
# # print( myObject.add )
# print( myObject.differnce() )
# print( myObject.product() )
# print( myObject.divide() )
# print( myObject.modulous() )
# print( myObject.power() )

# Principles of OOPs | 4 Pillars of OOPs

# 1. Encapsulation --> To build a single unit, a unit which conatins all the properties and methods called a class.

# 2. Abstraction --> Your user should be restricted to access certain properties & certain methods bu hiding the details from the user by making them private (__)

# 3. Inheritance --> An ability of a class to inherit the public properties & public methods from the parent class to the child class.

# 4. Polymorphism

# Parent Class
class Person:
    def __init__(self, userName, userAge):
        self.__name = userName
        self.__age = userAge

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, newName):
        self.__name = newName

    def setAge(self, newAge):
        self.__age = newAge

# Child Class --> Inherit/Access all the properties / methods from the Parent Class
class User(Person):
    # Take value from user -> Parameterised Constructor
    def __init__(self, userName, userAge, userHobbies, userAddress):
        # key = value
        # properties = values
        # call the parent constructor
        super().__init__(userName, userAge)
        self.__hobbies = userHobbies
        self.__address = userAddress

    # Getters & Setters
    # Getters --> Helps user to access the keys/properties of the class (BUT NOT DIRECTLY)
    def getAddress(self):
        return self.__address

    def getHobbies(self):
        return self.__hobbies

    # Setters --> Help user to update the keys/properties of the class (BUT NOT DIRECTLY)
    def setHobbies(self, newHobbies):
        self.__hobbies = newHobbies

    def setAddress(self, newAddress):
        self.__address = newAddress

    def getUserDetails(self):
        return 'Hello, my name is {}. I am {} years old. And my hobbies are {} and {}. I live in the {} city'.format(super().getName(), super().getAge(), self.__hobbies[0], self.__hobbies[1], self.__address.get('city'))

# Create Objects
# userOne = User("User One", 23, ['Playing Chess', 'Playing Soccer'], {'city': 'Chandigarh', 'state': 'Chandigarh'})
# print( userOne.getUserDetails() )
# # Updated the details
# userOne.setName("New User One")
# userOne.setAge(24)
# userOne.setHobbies(["Playing Guitar", "Attending Coding Contest"])
# userOne.setAddress({'city': 'Delhi', 'state': 'Delhi'})
# # Print new details
# print( userOne.getUserDetails() )

# userTwo = User("User Two", 20, ['Coding', 'Attending Hackathons'], {'city': 'Dehradun', 'state': 'Uttarakhand'})
# print(userTwo.name)

# Multiple Inheritance
class Father:
    def __init__(self, propOne):
        self.propertyOne = propOne
    
    def show(self):
        return 'Value - {}'.format(self.propertyOne)

class Mother:
    def __init__(self, propTwo):
        self.propertyTwo = propTwo
    
    def show(self):
        return 'Value - {}'.format(self.propertyTwo)

    
class Child(Mother, Father):
    def __init__(self, propOne, propTwo, propThree):
        Father.__init__(self, propOne)
        Mother.__init__(self, propTwo)
        self.propertyThree = propThree

    def showChild(self):
        return 'Value - {}'.format(self.propertyThree)

childOne = Child('Father Property', 'Mother Property', 'Child Property')
print( childOne.show() )