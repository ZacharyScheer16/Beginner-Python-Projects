'''dct = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(len(dct)) # 7

#access dictionary items
print(dct['first_name'])
print(dct.get("country"))
print(dct.get("skills"))
print(dct['skills'][3])

dct.pop('country')#removes country
'''
from prompt_toolkit.shortcuts import clear

#challenge
#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "German short-haired Pointer"
dog['legs'] = 4
dog['age'] = 6

student = {
    "first_name": "Zachary",
    "last_name": "Scheer",
    'gender':'male',
    'age': 20,
    'married': True,
    "skills": ['python', 'git commands', 'bashing/scripting', 'java', 'springboot'],
    'country': 'USA',
    'city': 'Phoenix',
    "address": "19007 M 34th ave "
}

print(len(student))
print(type('skills'))
print(student.get('skills'))
student["skills"].append('docker')
student["skills"].append("AWS")
values_list= list(student.values())
keys_list  = list(student.keys())

print(values_list , '\n', keys_list)

convertedToList = list(student.items())
print(convertedToList)

del student['married']
del dog


