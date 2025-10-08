from car import Car

car1 = Car("BMW", 2025, "Baby Blue", False)
car2 = Car("Ford Mustang", 1968, "Black", True)
car3 = Car("Toyota Prius", 2022, "Silver", False)

# Print statements for all three cars:

# 1. Original Car (BMW)
print(car1.model + ", " + car1.color + ", " + str(car1.year) + ", FOR SALE: " + str(car1.for_sale))

# 2. New Car (Mustang)
print(car2.model + ", " + car2.color + ", " + str(car2.year) + ", FOR SALE: " + str(car2.for_sale))

# 3. New Car (Prius)
print(car3.model + ", " + car3.color + ", " + str(car3.year) + ", FOR SALE: " + str(car3.for_sale))
car1.stop()
car1.drive()