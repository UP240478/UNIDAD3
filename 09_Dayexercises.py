#ejercicio 1
print('ejercicio 1')
edad = int (input('ingresa tu edad'))
if edad > 18:
    print("Ya puedes manejar")
else:
    print('No puedes manejar',18 - edad,'años faltantes')

#ejercicio 2
print('ejercicio 2')
tu_edad = int(input('ingresa tu edad'))
if tu_edad > 19:
    print("eres mayor que yo por ", tu_edad - 19,'años')
elif tu_edad == 19:
    print('tenemos la misma edad')
else:
    print('soy mayor que tu por ',19 - tu_edad,'años')

#ejercicio 3
print('ejercicio 3')
a = int(input('ingresa un numero'))
b = int(input('ingresa otro numero'))
if a > b:
    print('El numero',a,'es mayor que',b)
elif a == b:
    print('Los numeros son iguales')
else:
    print('El numero',b,'es mayor que',a)

#ejercicio 4
print('ejercicio 4')

calificacion = int(input('Ingresa tu calificacion'))
if calificacion >= 80 and calificacion <=100:
    print('tienes una A')
elif calificacion >=70 and calificacion<=79:
    print('Tienes una B')
elif calificacion >=60 and calificacion<=69:
    print('Tienes una C')
elif calificacion >=50 and calificacion<=59:
    print('Tienes una D')
else:
    print('Tienes una F')


#ejercicio 5
print('ejercicio 5')
mes = int(input('Ingresa el mes'))

if mes == ('Septiembre','septiembre','Octubre', 'ovtubre','Noviembre','noviembre'):
    print('Es otoño')
elif mes == ('Diciembre','diciembre','Enero','enero','Febrero','febrero'):
    print('Es invierno')
elif mes == ('Marzo','marzo','Abril','abril','Mayo','mayo'):
    print('Es primavera')
else: mes == ('Junio', 'junio', 'Julio','julio','Agosto','agosto')
print("Es verano")


#ejercicio 6
print('ejercicio 6')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = int(input('Ingresa tu fruta'))
if fruta not in fruits:
    print('No tenemos esa fruta')
    print('Agregar fruta')
    print(fruits.append(fruta))
else:
    print('Tenemos esa fruta')
    print(fruits)

#ejercicio 7
print('ejercicio 7')

person={
    'first_name': 'Carlos',
    'last_name': 'Perez',
    'age': 19,
    'country': 'Mexico',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Uruguay',
        'zipcode': '47270'
    }
    }
#Verifique si el diccionario de personas tiene una clave de habilidades, si es así imprima la habilidad del medio en la lista de habilidades.
if 'skills' in person:
    print('Si esta')
else:
    print('No esta')

#ejercicio 8
print('ejercicio 8')
#* Verifique si el diccionario de personas tiene una clave de habilidades, si es así, verifique si la persona tiene la habilidad 'Python' e imprima el resultado.
if 'skills' in person and 'Python' in person['skills']:
    print('Si esta en las habilidades')
else:
    print('No esta')


#ejercicio 9
print('ejercicio 9')
if 'JavaScript' and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' and 'Node' and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:print('unknown title') 


#ejercicio 10
print('ejercicio 10')
if 'is_married' == True and 'country'== 'Finlandia' in person:
    print('Esto es verdadero esta csado y es de Finlandia')
else:
    print('No esta casado y no es de Finlandia','Esta casado pero vive en Mexico')

    

