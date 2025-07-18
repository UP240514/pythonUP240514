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
from collections import Counter
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