import mymodule
import string
import random

print(mymodule.generate_full_name("Zachary", "Scheer"))

def random_user_id():
    chars = string.ascii_letters + string.digits
    user_id = ""
    for _ in range(6):
        user_id += random.choice(chars)
    return user_id

def user_id_gen_by_user():
    chars = string.ascii_letters + string.digits

    length = int(input("Enter number of characters: "))
    count = int(input("Enter number of IDs: "))

    for _ in range(count):
        user_id = ""
        for _ in range(length):
            user_id += random.choice(chars)
        print(user_id)

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        colors.append(rgb_color_gen())
    return colors


def list_of_hexa_colors(n):
    colors = []
    hex_chars = "0123456789abcdef"

    for _ in range(n):
        color = "#"
        for _ in range(6):
            color += random.choice(hex_chars)
        colors.append(color)

    return colors
def generate_colors(color_type, n):
    if color_type == "hexa":
        return list_of_hexa_colors(n)
    elif color_type == "rgb":
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type"



def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        colors.append(rgb_color_gen())
    return colors
def shuffle_list(lst):
    shuffle_list = list[:]
    random.shuffle(shuffle_list)
    return shuffle_list

def unique_random_numbers():
    numbers = []
    while len(numbers) < 7:
        num = random.randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    return numbers

print(unique_random_numbers())
