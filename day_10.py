#Ejercicios nivel 1:

#1
numbers = [0,1,2,3,4,5,6,7,8,9,10] #For,
for number in numbers: 
    print(number)

count = 0 #While.
while count <10: #A diferencia del for, el while tiene que tener un valor en especifico y no una lista.
    print(count)
    count = count +1

#2
numbers = [10,9,8,7,6,5,4,3,2,1,0]
for number in numbers:
    print(number)

count = 10
while count <0:
    print(count)
    count = count - 1

#3
calls = "#"
while calls < "########":
    print(calls)
    calls= calls + "#"

#4
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
    
#5
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [1,2,3,4,5,6,7,8,9,10]
for num1,num2 in zip(num1,num2):
    print(f"{num1} x {num2} =", num1*num2)

#6
lenguajes_programacion  =['Python', 'Numpy','Pandas','Django', 'Flask']
for lenguajes in lenguajes_programacion :
    print( lenguajes)

#7
for num in range(0, 101):
    if num % 2 == 0:
        print(num)

#8
for num in range(0, 101):
    if num % 2 != 0:
        print(num)

#Ejercicios nivel2:

#1
num = 0
for i in range(101):
    num = num + i 
    print(num)

#2
suma_pares = 0
suma_impares = 0

for num in range(0, 101):  
    if num % 2 == 0: 
        suma_pares += num
    else: 
        suma_impares += num

print("La suma de todos los números pares es:", suma_pares)
print("La suma de todos los números impares es:", suma_impares)


#Ejercicios de nivel 3:

#1
import countries as p
paises = p.countries
paises_con_land = []
for pais in paises:
    if 'land' in pais:
        paises_con_land.append(pais)
print("Los paises que terminan con Land son:", paises_con_land)

#2
frutas = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(frutas)-1, -1, -1):
    print(frutas[i])


#3
import countries_data as cd
number_of_lenguaje = cd.paises
lenguajes = set()
for pais in number_of_lenguaje:
    for idioma in pais['languages']:
        lenguajes.add(idioma)
print("El total de idiomas es:", len(lenguajes))

#3.2
setLanguages = set()
dictLanguages = {}

for country in cd.paises:
    for language in country['languages']:
        setLanguages.add(language)

for language in setLanguages:
    dictLanguages[language] = 0

for language in dictLanguages:
    for country in cd.paises:  
        if language in country['languages']:
            dictLanguages[language] += country['population']

sortValuesLanguagesPopulation = sorted(dictLanguages.values(), reverse=True)
sorfKeysLanguagesPopulation = sorted(dictLanguages, key=dictLanguages.get, reverse=True)

print('Los 10 idiomas más hablados en el mundo son:')
for i in range(10):
    print(" El Idioma es:",  sorfKeysLanguagesPopulation[i])
    print("Cantidad de personas que lo hablan:", sortValuesLanguagesPopulation[i])

#3.3
paises = cd.paises
paises_poblacion = {}
for pais in paises:
    paises_poblacion[pais['name']] = pais['population']
paises_poblacion_ordenados = sorted(paises_poblacion.items(), key=lambda x: x[1], reverse=True)
print("Los 10 países más poblados del mundo son:")
for i in range(10):
    print(paises_poblacion_ordenados[i][0], ":", paises_poblacion_ordenados[i][1])


    
print("revisado")











