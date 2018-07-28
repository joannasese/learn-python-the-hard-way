# import is how you add modules to script
# argv is the argument variable
# from sys import argv
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# $ python3.6 ex13.py first 2nd 3rd
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd

# from sys import argv
# script, mom, dad, sister = argv
#
# print("Mom's name is:", mom)
# print("Dad's name is:", dad)
# # print("Her name is:", sister)
# print(f"Sister's name is {sister}.")

from sys import argv
script, retort = argv

response = input("What do you say to that?\n")
print(f'Well I say "{retort}" instead of "{response}".')
