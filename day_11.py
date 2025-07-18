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


#Ejercicios Nivel 2

#1
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")
evens_and_odds(100)

#2
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))

#3
def is_empty(param):
    return not bool(param)
print(is_empty([]))
print(is_empty(""))
print(is_empty([1]))

#4
from collections import Counter

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst = sorted(lst)
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    return lst[mid]

def calculate_mode(lst):
    freq = Counter(lst)
    max_count = max(freq.values())
    return [k for k, v in freq.items() if v == max_count]

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

numbers_list = [1, 2, 3, 4, 5, 5]
print(calculate_mean(numbers_list))
print(calculate_median(numbers_list))
print(calculate_mode(numbers_list))
print(calculate_range(numbers_list))
print(calculate_variance(numbers_list))
print(calculate_std(numbers_list))


#Ejercicios Nivel 3

#1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))

#2
def are_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_items_unique([1, 2, 3]))
print(are_items_unique([1, 2, 2]))

#3
def are_same_type(lst):
    return all(type(i) == type(lst[0]) for i in lst)
print(are_same_type([1, 2, 3]))
print(are_same_type([1, 'a', 3]))

#4
def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)
print(is_valid_variable("variable1"))
print(is_valid_variable("1variable"))
print(is_valid_variable("for"))

#5
def most_spoken_languages(data, top_n=10):
    lang_counter = Counter()
    for country in data:
        lang_counter.update(country['languages'])
    return lang_counter.most_common(top_n)

data = [
    {'name': 'USA', 'population': 331000000, 'languages': ['English']},
    {'name': 'Mexico', 'population': 126000000, 'languages': ['Spanish']},
    {'name': 'India', 'population': 1380000000, 'languages': ['Hindi', 'English']},
    {'name': 'China', 'population': 1440000000, 'languages': ['Chinese']},
    {'name': 'Canada', 'population': 38000000, 'languages': ['English', 'French']},
]
print(most_spoken_languages(data, 3))


def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]
print(most_populated_countries(data, 3))