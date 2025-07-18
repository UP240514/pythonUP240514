#ejercicios
dog={'name':'tilin',
    'color':'brown',
    'breed':'boxer',
    'legs':4,
    'age':5}

student={'first_name':'calimba',
        'last_name':'perez',
        'gender':'male',
        'age':19,
        'marital_status':'abcd',
        'skills':['tufting'],
        'country':'mexico',
        'city':'monterrey',
        'address':'moreloko'}
student['skills']='videogames','music'
key=student.keys()
values=student.values()
del dog['name']
print(dog)
print(type(student['skills']))
print(key)
print(values)
print(len(student))
print(student.items())
print(student) 
del dog