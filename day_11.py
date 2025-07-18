#Ejercicios Nivel 1

#1
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 4))

#2
import math
def area_of_circle(r):
    return math.pi * r * r
print(area_of_circle(5))

#3
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los elementos deben ser números."
print(add_all_nums(1, 2, 3, 4))

#4
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(convert_celsius_to_fahrenheit(30))

#5
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Mes inválido'
print(check_season("March"))

#6
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 4))

#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'No hay soluciones reales'
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2
print(solve_quadratic_eqn(1, -3, 2))

#8
def print_list(lst):
    for item in lst:
        print(item)
print_list(['a', 'b', 'c'])

#9
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#10
def capitalize_list_items(lst):
    return [item.upper() for item in lst]
print(capitalize_list_items(['apple', 'banana', 'cherry']))

#11
def add_item(lst, item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#12
def remove_item(lst, item):
    return [x for x in lst if x != item]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#13
def sum_of_numbers(n):
    return sum(range(n + 1))
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#14
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)
print(sum_of_odds(10))

#15
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
print(sum_of_even(10))

