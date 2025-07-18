#Ejercicios nivel 1:

#1
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())

#2

def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    ids = [''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)) for _ in range(num_ids)]
    return '\n'.join(ids)

print(user_id_gen_by_user())

#3

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

