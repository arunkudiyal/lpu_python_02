# Programming paradigm (way) of solving problems using the concepts of classes and objects

# Class --> A template using which you can create real-life entities (Object)

# A class and object has 'IS-A' relationship

class Dog:
    # Properties related to the classs being built

    # Constructor --> Help you define properties for each object being created
    def __init__(self, name, breed, noOfLegs, color):
        # Defining the properties
        # self.propName = parameter

        self.dogName = name
        self.dogBreed = breed
        self.dogLegs = noOfLegs
        self.dogColor = color

    # Functionalities that each object will perform -> Functions --> Methods
    def getDetails(self):
        print('This is a {}. Its name is {}, and his color is {}'.format(self.dogBreed, self.dogName, self.dogColor) )

    def walk(self):
        print('{} is walking'.format(self.dogName))

    def bark(self):
        print('{} is barking...'.format(self.dogName))

# How to create an Object
# SYNTAX --> ObjectName = ClassName(values to the properties)

germanShepheard = Dog('Jack', 'GSD', 4, 'Brown')
print(germanShepheard)
germanShepheard.getDetails()
germanShepheard.bark()
germanShepheard.walk()

bullDog = Dog('Jill', 'Bull Dog', 4, 'Black')
print(bullDog)
bullDog.getDetails()
bullDog.bark()
bullDog.walk()

# Principles of OOPs