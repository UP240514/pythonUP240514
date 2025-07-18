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