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




