import math
#Functions
'''
#1.1

def add_two_numbers(num1, num2):
    sum = num2 + num1
    return sum


print(add_two_numbers(1,3))

#1.2
def area_circle(radius):
    area = radius *radius * math.pi
    return area

print(area_circle(4))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int,float)):
            return "All arguments mist be numbers"
        total = num + total
    return  total
print(add_all_nums(2,5,8658,446,89))


def convert_celsius_to_fahrenheit(c):
    return (c*9/5)+32

print(convert_celsius_to_fahrenheit(10))

def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'

print(check_season("april"))

def calculate_slope(x1,y1,x2,y2):
    if x2 - x1 == 0:
        return "Undefined slope"
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(2,5,3,8))

def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No real solution"
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return x1, x2


def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

def capitalize_list_items(lst):
    new_list = []
    for item in lst:
        new_list.append(item.upper())
    return new_list
'''


#Exercise 2
def evens_and_odds(even_number):
    even =0
    odds = 0
    if even_number < 0:
        print('invalid number, must be 0 or greater')
    for i in range(even_number +1):
        if i % 2 == 0:
            even += 1
        else:
            odds += 1
    return f"The number of odds are {odds}. The number of evens are {even}."

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def is_empty(value):
    return value == "" or value == [] or value == {}

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    return lst[mid]

def calculate_mode(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return max(freq, key=freq.get)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))




