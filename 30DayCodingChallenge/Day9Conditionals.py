'''age = int(input("What is your age: "))

if age >= 18:
    print("You are old enough to drive")
else:
    missing_age = 18 - age
    print(f"You are {age}, you are missing {missing_age} years to drive ")
'''

'''
#Excercie 9.2.1
CPU_age = 23
user_age = int(input("What is your age: "))
if CPU_age > user_age:
    difference_age = CPU_age - user_age
    print(f"CPU is {difference_age} years older")
elif CPU_age  < user_age:
    user_difference = user_age - CPU_age
    print(f"You are {user_difference} years older")
else:
    print(f"We are both {CPU_age} years old")
'''
    # Exercise 9.3.1

person1={
    'first_name': 'Zachary',
    'last_name': 'Scheer',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#Middle skill
if 'skills' in person1:
    middle_index = len(person1['skills']) // 2
    print("Middle skill:", person1['skills'][middle_index])

# 2. Check for Python skill
if 'skills' in person1:
    search_python = 'Python' in person1['skills']
    print("Has Python:" , search_python)

# 3. Developer title
skills = person1.get('skills', [])
if skills == ['JavaScript', 'React']:
    print("Front end developer")
elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")
else:
    print("Unknown title")


# 4. Married and lives in Finland
if person1.get('is_marred') and person1.get('country') == 'Finland':
    print(f"{person1['first_name']} {person1['last_name']} lives in Finland. He is married.")


