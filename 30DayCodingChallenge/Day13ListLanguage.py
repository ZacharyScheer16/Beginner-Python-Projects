'''
language = 'Python'

lst = list(language)
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

lst = [i for i in language]
print(type(lst)) # list
print(lst)    # ['P', 'y', 't', 'h', 'o', 'n']

numbers = [i for i in range(11)]#0 to 10
print(numbers)

squared = [i * i for i in range(11)]
print(squared) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]



x = lambda param3, param4, apram5: param3 + param4+ apram5
print(x(1,4,6))
'''
#1.1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result_neg = [num for num in numbers if num <=0 ]
print(result_neg)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat = [num for sublist in list_of_lists for inner in sublist for num in inner]

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(result)

countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

result = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [[(country, city)]] in countries
]

print(result)


