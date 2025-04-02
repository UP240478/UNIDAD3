#ejercicio 1
print('ejercicio 1')
def add_two_numbers ():
    num_one = 4
    num_two = 8
    toatal = num_one + num_two
    print(toatal)
add_two_numbers()

#ejercicio 2
print('ejercicio 2')
def area_de_circulo ():
    radio = int(input('Ingresa el radio del circulo'))
    area = (radio * radio)*3.1416
    print(area)
area_de_circulo()

#ejercicio 3
print('ejercicio 3')

def all_numbers(a,b,c,d,e):
    s = a+b+c+d+e
    if s != float:
        return 'todos los numeros son enteros', s
    else: return 'no se puede hacer la suma'
print(all_numbers(1,2,3,4,5))

#ejercicio 4
print('ejercicio 4')
temperatura = int(input('Ingresa la temperatura'))
def convert_celsius_to_fahrenheit():
   tem = (temperatura * 9/5) + 32
   return tem
print(convert_celsius_to_fahrenheit())

#ejercicio 5 
print('ejercicio 5')
def checar_temporada():
     mes = int(input('Ingresa el mes'))
     if mes == ('Noviembre','noviembre','Diciembre','diciembre','Enero','Febrero'):
         print("inviernno")
     elif mes == ('Marzo','Abril','Mayo','Junio'):
         print('Primavera')
     elif mes == ('Julio','Agosto','Septiembre','octubre'):
         print("verano")
     else:print('otono')

print(checar_temporada())

#ejercicio 6
print('ejercicio 6')
def ecuacion():
    x1,y1,x2,y2 = 1,2,3,4
    m = (y2 - y1) / (x2-x1)
    print(m)

print(ecuacion())

#ejercicio 7
print('ejercicio 7')
def ecuacion_cuadratica():
    x = int(input('ingresa el valor de x'))
    a,b,c = 1,2,3
    ecuacionfinal = a*(x)**2 + b*(x) + c
    print(ecuacionfinal)

print(ecuacion_cuadratica())

#ejercicio 8
print('ejercicio 8')
lista = ['coca','mari','fenta']
def imprimirvalore():
    print(lista)

print(imprimirvalore())

#ejercicio 9
print('ejercicio 9')
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# EJERCICIO 10
print('ejercicio 10')
def capitalize_list_items(lista):
    return[item.capitalize() for item in lista]
print(capitalize_list_items(["bazinga", "el pepe", "jose"]))

# EJERCICIO 11
print('ejercicio 11')
def add_item(lista, objeto):
    lista.append(objeto)
    return lista
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 

# EJERCICIO 12
print('ejercicio 12')
def remove_item(lista, objeto):
    lista.remove(objeto)
    return lista
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  

# EJERCICIO 13
print('ejercicio 13')
def sum_of_numbers(num1):
    suma = 0
    for i in range(0,num1 + 1):
        suma += i
    return suma
print(sum_of_numbers(5))  # 15

# EJERCICIO 14
print('ejercicio 14')
def sum_of_odds(odd): #Impares
    suma = 0
    for i in range(0,odd + 1, 2):
       suma += i
    return suma
print(sum_of_odds(100))

# EJERCICIO 15
print('ejercicio 15')
def sum_of_even(sisi):
    suma = 0
    for i in range(0,sisi, 2):
        suma += i
    return suma
print(sum_of_even(100))


# PARTE 2
print('parte 2')
#  EJERCICIO 1
print('ejercicio 1')
def evens_and__odds(numeros):
    suma_pares = 0
    suma_impares = 0
    for i in range(numeros + 1):
        if i %2 == 0:
            suma_pares += 1
        else: suma_impares += 1
    return suma_pares, suma_impares
print(evens_and__odds(100))

# EJERCICIO 2
print('ejercicio 2')
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    result = 1
    for i in range(2, n + 1):  
        result *= i
    return result
print(factorial(5)) 

# EJERCICIO 2
print('ejercicio 2')
def is_empty(value):
    return not bool(value)
print(is_empty(""))      

# EJERCICIO 3
print('ejercicio 3')
from statistics import mean, median, mode, variance
from math import sqrt

def calculate_mean(numbers):
    return mean(numbers)

def calculate_median(numbers):
    return median(numbers)

def calculate_mode(numbers):
    try:
        return mode(numbers)
    except:
        return "No unique mode found"

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    return variance(numbers)

def calculate_std(numbers):
    return sqrt(calculate_variance(numbers))

numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print("media:", calculate_mean(numbers))
print("Mediana:", calculate_median(numbers))
print("Moda:", calculate_mode(numbers))
print("Rango:", calculate_range(numbers))
print("Variación:", calculate_variance(numbers))
print("Desviaci[on Estandar", calculate_std(numbers))

# PARTE 3
print('parte 3')
# EJERCICIO 1
print('ejercicio 1')
def numero_primo(numero):
    if numero in [1, 3, 5, 7, 11, 13]:
        print("Es primo")
    else:
        print("Es falso")
numero_primo(2)  

# EJERCICIO 2
print('ejercicio 2')
def unicos(lst):
    return len(lst) == len(set(lst))
unique_numbers = [1, 2, 3, 4, 5]
print(unicos(unique_numbers))

# EJERCICIO 3
print('ejercicio 3')
def same_data_type(lst):
    return len(set(type(x) for x in lst)) == 1
print(same_data_type([1, 2, 3, 4, 5]))  

# EJERCICIO 4
print('ejercicio 4')
import keyword

def is_valid_variable(name):
    if not isinstance(name, str):
        return False
    if keyword.iskeyword(name):
        return False
    if not name.isidentifier():
        return False
    return True
print(is_valid_variable("variable"))

# EJERCICIO 5
print('ejercicio 5')

def lenguas_más_habladas(n=10):
    language_counts = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Arabe': 600}
    return sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:n]


def paises_mas_importantes(n=10):
    country_population = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Brasil': 212}
    return sorted(country_population.items(), key=lambda x: x[1], reverse=True)[:n]


print("Top 10 idiomas más hablados:")
for idioma, hablantes in lenguas_más_habladas(10):
    print(f"{idioma}: {hablantes} millones de hablantes")


print("\nTop 10 países más importantes:")
for pais, poblacion in paises_mas_importantes(10):
    print(f"{pais}: {poblacion} millones de personas")