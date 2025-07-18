#Ejercicios Nivel 2
import math
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
