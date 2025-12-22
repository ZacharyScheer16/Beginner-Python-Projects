from countries import countries
'''

1.1
count = 0
while count < 5:
    count = count + 1
    print(count)
    if count == 3:
        break


for i in range(0,11):
    print(i)


i =0
while i<= 10:
    print(i)
    i = i+1


1.2
for i in range(10, -1, -1):
    print(i)


i = 10
while i >=0:
    print(i)
    i = i-1



1.3
i =1
while i <=7:
    print(i * '#')
    i = i+1


for i in range(1,8):
    print(i* '#')
    i = i+1


for row in range(8):
    for col in range(8):
        print("#", end= " ")
    print()


for i in range(0,11):
    answer = i*i
    print(f"{i} * {i} = {answer}\n")
    

skills = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for skill in skills:
    print(skills)
    '''

countries_with_land = []
#3.1
for country in countries:
    if 'land' in country.lower():
        countries_with_land.append(country)

print(countries_with_land)

#3.2

fruit_list = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit = []

for i in range(len(fruit_list)-1,-1,-1):
    reversed_fruit.append(fruit_list[i])

print(reversed_fruit)



