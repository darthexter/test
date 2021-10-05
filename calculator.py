#!/usr/bin/python3

# This is a Simple Calculator written in python

import sys

print("This is a Simple Calculator\n")

try:
  num1 = int(input("Please enter a number: "))
  num2 = int(input("Please enter a second number: "))
except:
  print("Please enter a valid number!")
  sys.exit()

menu = '''
1. Addition
2. Subtraction
3. Multiplication
4. Division
'''

print(menu)

choice = input("\nEnter choice: ")

if choice == '1':
	result = num1 + num2
	print("\nAnswer is: {}".format(result))
else:
	pass

