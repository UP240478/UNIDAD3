#ejercicio 1
print('ejercicio 1')
dog ={}
#ejercicio 2
print('ejercicio 2')
dog = {'name':'firulais',
    'color':'negro', 
    'raza':'labrador',
    'patas':4, 
    'edad':2}

#ejercicio 3
estdudiante = {'first name':'Carlos',
               'lastname':'Perez',
               'genero':'hombre',
               'edad':19,
               'casado':True,
               'Habilidades':['correr','basquetbol','manejar motos'],
               'pais':'Mexico',
               'Ciudad':'La chona',
               'direccion':['calle:uruguay']}

#ejercicio 4
print('ejercicio 4')
print(len(estdudiante))

#ejercicio 5
print('ejercicio 5')
print(len(estdudiante['direccion']))
print(type(estdudiante['direccion']))

#ejercicio 6
print('ejercicio 6')
estdudiante['Habilidades'].append('Bailar')
print(estdudiante)

#ejercicio 7
print('ejercicio 7')

keys = estdudiante.keys()

print(keys)

#ejercicio 8
print('ejercicio 8')

values = estdudiante.values()

print(values)


#ejercicio 9
print('ejercicio 9')
print(estdudiante.items())

#ejercicio 10
print('ejercicio 10')

print(estdudiante.popitem())

#ejercicio 11
print('ejercicio 11, borrar un diccionario')
del estdudiante
