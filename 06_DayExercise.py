#ejercicio 1
print('ejercicio 1, crear un tuple vacio')

tuple_vacio = ()
print(tuple_vacio)
#ejercicio 2
print('ejercicio 2, crear un tuple con valores')
tuple_valores = ('fernanda', 'Sofia', 'Lucy')
print(len(tuple_valores))
#ejercicio 3
print('ejercico 3, unir los tuples con nombres de hermanos')
tuple_hermanos = ('Angel', 'Fer', 'Luis')
resultado = tuple_valores + tuple_hermanos
print(resultado)
#ejercicio 4
print('ejercicio 4, cuantos cara cteres tiene?')
print(len(resultado))
#ejercicio 5
print('ejercicio 5')
papis = ('Mami','papi')
family_members = resultado + papis
print(family_members)

#parte 2
#ejercicio 1
print('ejercicio 1')
a, b, c, d, e, f, h,i = family_members
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(h)
print(i)
#ejercicio 2
print('ejercicio 2')
frutas = ('manzana', 'platano', 'uva')
verduras = ('tomate', 'papa', 'zanahoria')
animales = ('perro', 'gato', 'pez')
food_stuff_tp = frutas + verduras + animales
print(food_stuff_tp)
#ejercicio 3
print('ejercicio 3')
lista = list(food_stuff_tp)
print(lista)
#ejercicio 4
print('ejercicio 4')
centro = len(lista)//2
print(centro)
#ejercicio 5
print('ejercicio 5')
quitar= lista[3:][:-3]
print(quitar)
#ejercicio 6
print('ejercicio 6')
del food_stuff_tp
#ejercicio 7
print('ejercicio 7')
print('mami' in family_members)
#ejercicio 8
print('ejercicio 8')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
