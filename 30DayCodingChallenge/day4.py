# Concatenate strings
from numpy import character

first_string = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
second_string = ' '.join(['Coding', 'For', 'All'])

print(first_string)   # Output: Thirty Days Of Python
print(second_string)  # Output: Coding For All

# Declare variable company
company = "Coding For All"

# Print the variable
print(company)

print(len(company))

companyUpper = company.upper()
print(company.upper())

print(second_string.title())
print(second_string.capitalize())
print(second_string.swapcase())

first_word = company[6:10]
first_word_method2 = company.split()[2]
print(first_word)
print(first_word_method2)
print("Coding" in company)
print(company.index("Coding"))

replace_String = company.replace("Coding","Python")
print(replace_String)

FAANG ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
splitFAANG= FAANG.split(",")

print(splitFAANG)

jf = company[0]
print(jf)
last = company[-1]
print(last)

var10 = company[9]
print(var10)

text = "Python For Everyone"
acronym = "".join(word[0] for word in text.split())
print(acronym)
cod = "Coding for all"
acr = "".join(words[0] for words in cod.split())
print(acr)