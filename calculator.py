#!/usr/bin/python3

# This is a Simple Calculator written in python

import sys

def addnum(num1,num2):
  return num1 + num2

def subnum(num1,num2):
  return num1 - num2

def multnum(num1,num2):
  return num1 * num2

def divnum(num1,num2):
  return num1 / num2

def main():
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
    result = addnum(num1,num2)
    print("\nAnswer is: {}".format(result))
  elif choice == '2':
    result = subnum(num1,num2)
    print("\nAnswer is: {}".format(result))
  elif choice == '3':
    result = multnum(num1,num2)
    print("\nAnswer is: {}".format(result))
  elif choice == '4':
    result = divnum(num1,num2)
    print("\nAnswer is: {}".format(result))
  else:
    print("Invalid Choice!")
    sys.exit()
  
  return 0
	
if __name__ == '__main__':
  main()
