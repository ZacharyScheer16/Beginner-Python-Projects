#python calc

def add(a, b):
    return int(a+b)

def remove(num1, num2):
    return int(num1-num2)



operator = input("Enter an operator + - * /: ")

num1 = float(input(("enter the 1st num: ")))
num2 = float(input("enter the second number: "))

if operator == "+":
    print(add(num1,num2))
elif operator == "-":
    print(remove(num1,num2))





