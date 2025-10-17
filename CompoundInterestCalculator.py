principle = 0
rate = 0
time = 0
interestPerYear = 0

def calculator(principle, rate, time,interestPerYear ):
    return principle *(1+ (rate/interestPerYear))**(interestPerYear*time)

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cant be less than or equal to 0")

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("Rate cant be less than or equal to 0")

while time <= 0:
    time = float((input("Enter the time : ")))
    if time <= 0:
        print("Time cant be less than or equal to 0")

while interestPerYear <= 0:
    interestPerYear = float(input("Enter the interestPerYear : "))
    if interestPerYear <= 0:
        print("interestPerYear cant be less than or equal to 0")

result = calculator(principle,rate,time,interestPerYear)
print(f"Total cost for {time} days and {rate}% with a principle amount of {principle}: result = {result}" )