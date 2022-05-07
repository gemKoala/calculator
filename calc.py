#calculator
#import libraries
import math
import cmath

print("Calculator")
#creating variables
num1 = float(input("Enter first number:"))
operation = input("Enter operation:")
if operation == "!":
    num1 = int(num1)
    num3 = math.factorial(num1)
    print("Answer:",num3)
    input("Press any key to exit")
    
elif operation == "square":
    num3 = num1 ** 2
    print("Answer:",num3)
    input("Press any key to exit")
    
elif operation == "cube":
    num3 = num1 ** 3
    print("Answer:",num3)
    input("Press any key to exit")
    
elif operation == "square root":
    num3 = cmath.sqrt(num1)
    print("Answer:±",num3)
    if num1 < 0:
        print("Answer:",num3,"i")
    input("Press any key to exit")
    
elif operation == "cube root":
    num3 = num1 ** (1/3)
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "sin":
    num3 = math.sin(num1)
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "cos":
    num3 = math.cos(num1)
    print("Answer:",num3)
    input("Press any key to exit")
    
elif operation == "tan":
    num3 = math.tan(num1)
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "ctan":
    num3 = math.ctan(num1)
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "arctan":
    num3 = math.arctan(num1)
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "log":
    num3 = math.log(num1)
    print("Answer:",num3)
    input("Press any key to exit")
else:
    num2 = float(input("Enter second number:"))
    
num3 = float
#operations
if operation == "+":
    num3 = num1 + num2
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "-":
    num3 = num1 - num2
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "*":
    num3 = num1 * num2
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "/":
    num3 = num1 / num2
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "^":
    num3 = num1 ** num2
    print("Answer:",num3)
    input("Press any key to exit")
elif operation == "%":
    num3 = num1 /100 * num2
    print("Answer:",num3)
    input("Press any key to exit")
