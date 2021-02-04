"""write a program to perform basic mathematical operations based on user input with validation.
 User input should be 2 numbers and operation sign(+ or - or * or /).."""


import re
regex_expressions=re.compile("[+,-,*,/,%,//,**]")

try:
    num1=float(input(f"Enter first number: "))
    num2 =float(input(f"Enter second number: "))
except:
    print("Please enter only numbers")
    exit()
operator = input("Enter operator: ")
if regex_expressions.search(operator) is None:
    print("Please enter operators like (+,-,*,/,%,//,**)")
    exit()

result = ""
if  operator == "+":
     result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result == num1 % num2
elif operator == "**":
    result = num1 ** num2
elif operator == "//":
    result= num1//num2

print(f"Output:- {result}")
