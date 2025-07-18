#Ejercicios nivel 1:

#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = [x for x in numbers if x <= 0]
print(result)

#2
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [x for sublist in list_of_lists for x in sublist]
print(result)

#3
tuples_list = [(i, i, i, i, i, i) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000, 100000]]
print(tuples_list)

#4
countries = [['Finland', 'Helsinki'], ['Sweden', 'Stockholm'], ['Norway', 'Oslo']]
output = [item for sublist in countries for item in sublist] + ['FIN', 'HELSINKI', 'SWEDEN', 'SWE', 'STOCKHOLM', 'NORWAY', 'NOR', 'OSLO']
print(output)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]
print(result)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = [' '.join((first, last)) for sublist in names for (first, last) in sublist]
print(result)


#7
linear_calc = lambda x1, y1, x2, y2, calc_type='slope': (y2 - y1) / (x2 - x1) if calc_type == 'slope' else y1 - ((y2 - y1) / (x2 - x1)) * x1

slope = linear_calc(1, 2, 3, 4, 'slope')
print(slope)

y_intercept = linear_calc(1, 2, 3, 4, 'intercept')
print(y_intercept)