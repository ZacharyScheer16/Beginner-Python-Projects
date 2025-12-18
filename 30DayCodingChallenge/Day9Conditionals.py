'''age = int(input("What is your age: "))

if age >= 18:
    print("You are old enough to drive")
else:
    missing_age = 18 - age
    print(f"You are {age}, you are missing {missing_age} years to drive ")
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
