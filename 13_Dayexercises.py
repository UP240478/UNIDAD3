# EJERCICIO 1
print('Ejercicio 1')
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]

numeros_negativos = [n for n in numeros if n <= 0]
print(numeros_negativos)

# EJERCICIO 2
print('Ejercicio 2')
listas =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_plana = [numero for sublista in listas for numero in sublista]
lista_plana_2 = [numero for sublista in lista_plana for numero in sublista]
print(lista_plana_2)

# EJERCICIO 3
print('Ejercicio 3')

tuplas = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuplas)

# EJERCICIO 4
print('Ejercicio 4')
paises = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
paises_planos = [[pais.upper(), pais[:3].upper(), capital.upper()] 
                 for sublista in paises for (pais, capital) in sublista]
print(paises_planos)

# EJERCICIO 5
print('Ejercicio 5')
diccionario_paises = [{'pais': pais.upper(), 'ciudad': ciudad.upper()} 
                      for sublista in paises for (pais, ciudad) in sublista]
print(diccionario_paises)

# EJERCICIO 6
print('Ejercicio 6')

nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [[nombre + " " + apellido] for sublista in nombres for (nombre, apellido) in sublista]
nombres_completos = [i for n in nombres_completos for i in n]
print(nombres_completos)

# EJERCICIO 7
print('Ejercicio 7')
pendiente = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
print(pendiente(3, 5, 4, 1))
