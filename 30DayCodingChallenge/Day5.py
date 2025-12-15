lst = list()
print(len(lst))

empty_list = []
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
"""print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
"""


listy = ["item1", "Item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9", "item10", "item11", "item12"]
listy.append("Item13")
print(listy)

listy.insert(1, "inserted Item")
print(listy) # 'item1, 'insertedItem', item2 ...
listy.remove("inserted Item")
print(listy)

listy.pop(2)
print(listy)
listy.pop(7)
print(listy)
listy.clear()

