# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
Aa = {19, 22, 24, 20, 25, 26}
Ba = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#ejercicio 1
print('ejercicio 1')
print(len(it_companies))
#ejercicio 2
print('ejercicio 2')
it_companies.add('Twitter')
print(it_companies)
#ejercicio 3
print('ejercicio 3')
it_companies.update(['Linkedin', 'Uber'])
print(it_companies)
#ejercicio 4
print('ejercicio 4')
it_companies.remove('Facebook')
print(it_companies)
if 'Twitter' in it_companies:
    it_companies.discard('Twitter')
print(it_companies)
#Parte 2
#ejercicio 1
print('ejercicio 1')
unir = Aa.union(Ba)
print(unir)
#ejercicio 2
print('ejercicio 2')
print(Aa.intersection(Ba))
#ejercicio 3
print('ejercicio 3')
print(Aa.issubset(Ba))
#ejercicio 4
print('ejercicio 4')
print(Aa.isdisjoint(Ba))
#ejercicio 5
print('ejercicio 5')
ayb = Aa.union(Ba)
bya = Ba.union(Aa)
print(ayb)
print(bya)
#ejercicio 6
print('ejercicio 6')
print(Aa.symmetric_difference(Ba))
#ejercicio 7
print('ejercicio 7')
del Aa,Ba

#PARTE3 
#EJERCICIO 1
print('ejercicio 1')
st = {12,13,14,15,16}
sit = [13,14,15,16,17]
len(st)
len(sit)
if len(st) == len(sit):
    print('son iguales')
elif len(st) > len(sit):
    print('st es mayor')
else:
    print('sit es mayor')
#EJERCICIO 2
print('ejercicio 2')
##Cadena: Es una secuencia fija de caracteres usada para representar texto, como palabras o frases.

#Lista: Es una colección ordenada de elementos que pueden cambiarse o modificarse.

#Tupla: Es como una lista, pero sus elementos no pueden ser modificados después de su creación.

#Conjunto: Es una colección de elementos únicos y desordenados, donde no se permiten duplicados
#EJERCICIO 3
print('ejercicio 3')
list = ['I am a teacher and I love to inspire and teach people']
texto = list.pop()
print(texto)
print(len(texto))

