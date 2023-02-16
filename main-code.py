# import

import math
import time
import random

# functions

list = []

def all_math():
        num1 = input("First Number: ")
        operator = input("Operator: ")
        num2 = input("Second Number: ")
        num1 = int(num1)
        num2 = int(num2)
        if operator == "*":
            answer = num1 * num2
            print(answer)
        elif operator == "/":
            answer = num1 / num2
            print(answer)
        elif operator == "+":
            answer = num1 + num2
            print(answer)
        elif operator == "-":
            answer = num1 - num2
            print(answer)
        elif operator == "**":
            answer = num1 ** num2
            print(answer)
        else:
            print("I cannot complete this.")

def help():
    split()
    print("Functions")
    print("help! = Help/Instructions")
    print("add = starts adding to list")
    print("[name of list] = prints the list")
    print("create = make your first list")

def split():
    print("---------------------------------")
    print()

# code

split()
print("Data Keeper")
print()
print("Type 'help!' to learn the commands")
print()
split()


while True:
    command = input(">>> ").strip().lower()

    if command == "help!":
        help()
    
    elif command == "create list":
        print("What would you like to name the list?")
        a = input() 
    
    elif command == "add":
        print("Adding to the list " + a)
        print("Type the Input Clearly Below:")
        b = input()
        list.append(b)
    
    elif command == "print":
        print(list)

    elif command == "remove":
        print("Enter the Element you want Removed in")
        print(list)
        remove_element = input()
        list.remove(remove_element)
        print(list)
    
    elif command == "math":
        all_math()

    elif command == "time":
        current_time = time.ctime()
        print(current_time)

    elif command == "location":
        print("Planet Earth")

    else:
        print(command)
