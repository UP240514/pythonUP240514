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