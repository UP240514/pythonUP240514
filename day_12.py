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

#Ejercicios nivel 2:


#1

def list_of_hexa_colors(n):
    return ["#" + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]

#2

def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

#3

def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return []

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

#Ejercicios nivel 3:

#1
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([1, 2, 3, 4, 5]))

#2

def generate_unique_random_numbers():
    return random.sample(range(10), 7)

print(generate_unique_random_numbers())