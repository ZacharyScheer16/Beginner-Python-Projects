#python calc

def add(a, b):
    return int(a+b)

def remove(num1, num2):
    return int(num1-num2)

def mult(n, b):
    return int(n*b)



operator = input("Enter an operator + - * /: ")

num1 = float(input(("enter the 1st num: ")))
num2 = float(input("enter the second number: "))


def divide(num1, num2):
    return float(num1/num2)


if operator == "+":
    print(add(num1,num2))
elif operator == "-":
    print(remove(num1,num2))
elif operator == "*":
    print(mult(num1,num2))
elif operator == "/":
    print(divide(num1,num2))
else:
    print(f"{operator} is not valid")





