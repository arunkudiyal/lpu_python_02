# BITWISE OPERATORS - &(AND), |(OR), ~(NOT), ^(XOR)
# a, b = 5, 4

# '''
# 5 -> 0101
# 4 -> 0100

# AND -> 0100 -> 4
# OR -> 0101 -> 5
# NOT -> -(0101 + 1) -> -(0110) -> -6
# XOR -> 0001 -> 1
# '''

# print('Bitwise AND is -> ', a & b)
# print('Bitwise OR is -> ', a | b)
# print('Bitwise NOT is -> ', ~a)
# print('Bitwise XOR is -> ', a ^ b)


# FUNCTIONS
# -> A way to create some re-usable block of code, which can called anytime for proceesing
# SYNTAX - def functionName(parameters):

# Q -> Create a function to add 2 numbers
def addTwoNums(num1, num2):
    return num1 + num2

# Q -> To get two numbers, add them and print the cube
val_one = int(input('enter I value -'))
val_two = int(input('enter II value -'))
sum_val = addTwoNums(val_one, val_two)
print(sum_val * sum_val * sum_val)

# PRIME-PALINDROME
