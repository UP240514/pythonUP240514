print("Hola mundo")
a=int(input("ingrese el primer digito entero: "))
b=int(input("ingrese el segundo digito entero: "))
multi= a*b
sum=a+b
res=a-b
div=a/b
exp=a**b
print("la multiplicacion entre: " ,a, "y ",b," es igual a: ", multi)
print("la divicion entre: ", a, "y ",b," es igual a: ", div)
print("la suma entre: ", a, "y ",b," es igual a: ", sum)
print("la resta entre: ", a, "y ",b," es igual a: ", res)
print(f"la exponencial entre: {a} y {b} es igual a {exp}")


texto_random="CASA"
print(len(texto_random))
print(texto_random.index("CASA"))
ult_dig=texto_random[-1]
print(ult_dig)
prim_dig=texto_random[0]
print(prim_dig)
prim_dos=texto_random[0:2]
ult_dos=texto_random[2:]
print(prim_dos)
print(ult_dos)
print(texto_random.capitalize())
print(texto_random.lower())
print(texto_random.upper())
print(texto_random.replace("S", "C"))

#area y perimetro de figuras
c=float(input("ingresa la base de el cuadrado:"))

area_cuadrado=print(f"el area del cuadrado es de: {c*c}" )
perimetro_cuadrado=print(f"el perimetro del cuadrado es de: {c+c+c+c}")

r=float(input("ingresa el radio del circulo: "))

area_circulo=print(f"el area del circulo es igual a: {float(3.1416*r**2)} ")
perimetro_circulo=print(f"el perimetro del circulo es igual a: {float(2*r*3.1416)} ")

frase="tilineitor  garcia  perez"
acronimo=""
for palabra in frase.split():
    acronimo += palabra[0].upper()
print(acronimo) 

n=10
n+=18
print(n)

l="holaholaholah"
ll= l[0:13:4]

