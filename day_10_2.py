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
