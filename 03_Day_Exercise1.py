import math

Edad = 19
Altura = 1.85
Complejo = 1 + 1j

base = int (input('Ingresa la base del triangulo'))
altura = int (input('ingresa la altura del triangulo'))
area = int (0.5*base*altura)
print('El area es de:', area)

#numero 5
lado1 = int(input('Ingresa la longitud de un lado'))
lado2 = int(input('ingrese el segundo lado'))
lado3 = int(input('ingresa el tercer lado'))
perimetro = lado1+ lado2 + lado3
print('El perimetro es de:', perimetro)


#area y perimetro de un rectangulo (numero 6)
l1 = int(input('ingrese la altura del rectangulo'))
l2 = int(input('ingrese la base del rectangulo'))
Area = l1*l2
Perimetro = 2 *(l1 + l2)
print('el area del rectangulo es de:', Area)
print ('El perimetro del retangulo es de:', Perimetro)

#Circulo(numero 7)

Radio = int (input('ingresa el radio del circulo'))
Pi = 3.14
AREA = Pi * Radio * Radio
Circunferencia = 2 * Pi * Radio

print('El area del circulo es de:', AREA)
print('La circunferencia del circulo es de:', Circunferencia)


# ejercicio 8


# z = 2q - 2  q = X Z = y
q1, z1, q2, z2 = 2,2,6,10
First_slope = (z2 - z1) / (q2 - q1)
print ('La pendiente es:', First_slope)

# ejercico 9
x1,y1,x2,y2 = 2,2,6,10 
Second_slope = (y2 - y1) / (x2 - x1)
print ('La sedunda pendiente es:', Second_slope)
distancia_ecudiliana = math.sqrt((x2 -x1) **2 + (y2 - y1)**2)
print('la distancia ecudiliana es:', distancia_ecudiliana)

#ejercicio 10
if (First_slope == Second_slope):
    print('Son iguales')
else: print('no son iguales,ESTAS MAL')

# ejercicio 11
x = int (input ('Ingrese el valor de x'))
Y = int (x^2 + 6*x + 9) 
print ('el valor de y es:', Y)

#ejercico 12
palabra1 = len('Python')
palabra2 = len('Dragon')
if (palabra1 == palabra2):
    print ('Las palabras son iguales')
else: print('las palabras son diferentes')

#ejercicio 13

if 'on' in 'dragon' and 'on' in 'python':
    print('SI esta en las palabras')
else: print('si se encuentra')

# ejercicio 14

if 'jargon'in'I hope this course is not full of jargon':
    print('si se encuentra la palbra en la oracion')
else:
    print('no se encuentra en la oracion') 


#ejercicio 15

if 'on' in 'python' and 'dragon':
    print('La palabra si se encuentra')
else:
    print('La palabra no se encuentra')


#ejercicio 16 
print(len('python'))