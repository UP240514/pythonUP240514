#Día 5
#Ejercicios: nivel 1

lista_vacia=list()

frutas=['Fresas', 'Piñas', 'Mangos', 'Sandía', 'Uvas']
print("Largo de la lista frutas: ", len(frutas))
print("First item: ", frutas[0])
print("Middle item: ", frutas[2])
print("Last item: ", frutas[4])

mixed_data_types=['Alison', 18, 1.59, 'Single', 'Hermanos Galeana']
print("Lista de tipos de datos distintos: ", mixed_data_types)

it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("Lista de compañias: ", it_companies)
print("Número de compañias: ", len(it_companies))
print("First company: ", it_companies[0])
print("Middle company: ", it_companies[3])
print("Last company: ", it_companies[6])
print("Lista antes de modificar: ", it_companies)
it_companies.insert(7, 'Alphabet')
it_companies.insert(3, 'Nvidia')
it_companies.remove('Amazon')
it_companies.append('AMAZON')
string=['Accenture']
it_companies.extend(string)
does_exist= 'IBM' in it_companies
print("Existe la compañía IBM en la lista? ", does_exist)
it_companies.sort()
print("Lista usando el sort method: ", it_companies)
it_companies.sort(reverse=True)
print("Lista en reversa: ", it_companies)
first_three=it_companies[0:3]
print("Primeras tres compañías de la lista: ", first_three)
last_three=it_companies[7:10]
print("Ultimas tres compañias de la lista: ", last_three)
middle_companies=it_companies[4:6]
print("Compañias del centro de la lista: ", middle_companies)
del it_companies[0]
print("Lista con la primera compañia de la lista eliminada: ", it_companies)
del it_companies[4]
print("Lista con la compañia del centro eliminada: ", it_companies)
del it_companies[7]
print("Lista con la ultima compañia eliminada: ", it_companies)
it_companies.clear()
del it_companies

front_end=['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end=['Node', 'Express', 'MongoDB']
print("Lista front end: ", front_end)
print("Lista back end: ", back_end)
front_end_copy=front_end.copy()
back_end_copy=back_end.copy()
full_stack= front_end_copy+back_end_copy
print("Lista full stack: ", full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print("Lista full stack con dos elementos extra: ", full_stack)

#Exercises: level 2

ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
edad_minima=min(ages)
edad_maxima=max(ages)
print("Edad minima de la lista: ", edad_minima)
print("Edad maxima de la lista: ", edad_maxima)
ages.append(edad_minima)
ages.append(edad_maxima)
print(ages)
median_age=(ages[5]+ages[6])/2
print("La edad media es: ", median_age)
average_age=(ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11])/12
print("Average age: ", average_age)
rango=edad_maxima-edad_minima
print("Rango de edad: ", rango)
valor1=abs(edad_minima-average_age)
valor2=abs(edad_maxima-average_age)
print("Comparación: ¿El valor ", valor1, " es >= al valor ", valor2, "? ", valor1>=valor2)