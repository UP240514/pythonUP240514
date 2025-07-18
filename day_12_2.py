#Ejercicios nivel 2:
import random


#1

def list_of_hexa_colors(n):
    return ["#" + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]

#2
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
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
