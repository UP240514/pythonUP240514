#Ejercicios nivel 1:
print("Ejercicios Nivel 1:")
#Ejercicio 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
#You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
print("Ejercicio 1:")
age = int(input("Escribe tu edad:"))
if age >= 18:
    print("You are old enough to learn drive.")
else :
    print(f"you need  {18 - age} more years to learn to drive. ")


#Ejercicio 2.
#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
# to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
print("Ejercicio 2:")
my_age = int(input("Escribe tu edad:"))
your_age = int(input("Escribe tu edad:"))
print("Quien es mas grande tu o yo: ")
if my_age == your_age :
    print("Tenemos la misma edad.")
elif my_age < your_age :
    print(f"Tu eres { your_age - my_age} años mayor que yo.")
else :
    print(f"Yo soy {my_age - your_age} años mayor que tu. ")

#Ejercicio 3.
#Get two numbers from the user using input prompt.
#If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
print("Ejercicio 3:")
numero_a =int(input("Escribe el primer numero :")) 
numero_b = int(input("Escribe el segundo numero:"))
if numero_a == numero_b :
    print("Los numeros son iguales.")
elif numero_a < numero_b :
    print(f"El numero {numero_a} es menor que el {numero_b}.")
else : 
    print(f"El numero {numero_a} es mayor que el {numero_b}.")




print("Ejercicios Nivel 2:")
#Ejercicios Nivel 2:
#Write a code which gives grade to students according to theirs scores:
print("Ejercicio 1:")
scores = int(input("Ingresa la calificacion:")) 

if scores>= 80:
    print('Tu calificacion es: A')
elif scores > 70 and scores < 79:
    print('Tu calificacion es: B')
elif scores > 60 and scores < 69:
    print('Tu calificacion es: C')
elif scores > 50 and scores < 59:
    print('Tu calificacion es: D')
else:
    print('Tu calificacion es: F')





#Ejercicio 2.
#Check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. December, January or February,
#the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
print("Ejercicio 2:")
mes = input('Ingresa el mes:').capitalize()
if mes in ['Septiembre','Octubre','Noviembre']:
    print('La estacion es otoño')
elif mes in ['Diciembre','Enero','Febrero']:
    print('La estacion es invierno')
elif mes in ['Marzo','Abril','Mayo']:
    print('La estacion es primavera')



#Ejercicio 3.
#The following list contains some fruits:
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_si_son_existentes = input("Escriba la fruta que quiera:").lower()
if frutas_si_son_existentes in frutas :
    print("La fruta que buscas si existe en la lista")
else : 
    frutas.append(frutas_si_son_existentes)
    print("La fruta se añadio a la lista: {frutas}")



print("Ejercicios nivel 3:")
#Ejercicios Nivel 3:
#Ejercicio 1
#Here we have a person dictionary. Feel free to modify it!
print("Ejercicio 1:")
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',     'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(person['skills'] [len(person['skills'])//2])

    if 'Python' in person['skills']:
        print(person['skills']) 
if 'skills' in person:
    hab = person['skills']
    if 'JavaScrip'in hab and 'React'in hab:
        print('He is a front end developer')
    elif 'Node' in hab and 'Phyton'in hab and'MongoDB' in hab:
        print('He is a backed developer')
    elif 'React' in hab and 'Node' in hab and 'MongoDB' in hab:
        print('He is a fullstack developer')
    else:
        print('titulo desconocido')
        print('titulo deconocido')

if person['is_marred'] == True and 'Finland' in person['country']:
    print('Asabeneh Yetayeh vive en Finland, y es casado.')

print("Terminados los ejercicios.")

print("revisado")































