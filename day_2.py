#Day 2: 30 Days of python programming

#Declare a first name variable and assign a value to it
nombre='angel'
print('nombre: ',nombre)
#Declare a last name variable and assign a value to it
apellido='salazar'
print('apellido: ',apellido)
#Declare a full name variable and assign a value to it
nombre_completo= 'angel salazar' 
print('nombre completo: ',nombre_completo)
#Declare a country variable and assign a value to it
pais='mexico'
print('pais: ',pais)
#Declare a city variable and assign a value to it
ciudad='aguascalientes'
print('ciudad: ',ciudad)
#Declare an age variable and assign a value to it
edad='18' 
print('edad: ',edad)
#Declare a year variable and assign a value to it
year='2006'
print('año: ',year)
#Declare a variable is_married and assign a value to it
esta_casado=False
print('casado?',esta_casado)
#Declare a variable is_true and assign a value to it
its_true=True
print('true?: ',its_true)
#Declare a variable is_light_on and assign a value to it
its_light_on=True
print('esta prendido?',its_light_on)
#Declare multiple variable on one line
cancion, banda, artista= 'dead bodies everywhere','korn','jhonatan davis'
print('cancion: ',cancion, 'banda: ',banda, 'artista: ',artista)


#clases de las variables utilizadas
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(year))
print(type(esta_casado))
print(type(its_true))
print(type(its_light_on))


print("longitud del nombre: ", len(nombre))

print("longitud del primer nombre:", len(nombre), "y la ", "longitud del apellido: ", len(apellido))

num_one=5
num_two=4
total=num_one+num_two
print(total)
diff=num_one-num_two
print(diff)
multi=num_one*num_two
print(multi)
div=num_one/num_two
print(div)
exp=num_one**num_two
print(exp)
flo_div=num_one//num_two
print(flo_div)
modulus=num_one%num_two
print(modulus)

print("el radio del circulo es de 30")
area_of_circle=30*(3.14**2)
print(area_of_circle)
circum_of_circle= 3.14*(30*2)
print(circum_of_circle)
print("nuevo circulo")
radio=input("ingrsa el radio del circulo: ")
area=int(radio)*(3.14**2)
print("el area del circulo es: ",area)
nombree, apellidoo, edaad, paiss = input("ingresa tu nombre, apellido, edad y pais").split()
print("tu nombre es: ",nombree, "tu apellido es: ",apellidoo,"tu edad es: ",edaad,"y tu pais de origen es",paiss)