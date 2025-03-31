#ejercicio 1
print('ejercicio 1')
contar = 0
while contar <11:
    print(contar)
    contar += 1

#ejercicio 2
print('ejercocio 2')

for i in range(10, -1, -1):
    print(i)

#ejercicio 3
print('ejercicio 3')
for i in range(1, 8):
    print('#' * i)

#ejercicio 4
print('ejercicio 4')
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

#ejercicio 5
print('ejercicio 5')
for i in range(11):
    print(f'{i} x {i} = {i * i}')
    
#ejercicio 6
print('ejercicio 6')
lista = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lista in lista:
    print(lista)

#ejercicio 7
print('ejercicio 7')
for number in range(101):
    print(number)

#ejercicio 8
print('ejercicio 8')
suma = 0
for i in range(101):
   suma += i
print("La suma es : " , suma)

#eejercicio 9
print('ejercicio 9')
suma_pares = 0  
suma_imparares = 0   

for i in range(101):  
    if i % 2 == 0:  
        suma_pares += i
    else:  
        suma_imparares += i

print("La suma de los pares es: ", suma_pares)
print("La suma de los impares es: ", suma_imparares)

#ejercicio 10
print('ejercicio 10')
frutas = ['banana', 'orange', 'mango', 'lemon']
for i in frutas:
    reversed_i = i[::-1] 
    print(reversed_i)


#ejercicio 11
frutas = ['banana', 'orange', 'mango', 'lemon']
for fruta in frutas:
    fruta_invertida = fruta[::-1]
    print(fruta_invertida)

