#ejercicio 1
print('ejercicio 1')

n1 = 'thirty'
n2 = 'days'
n3 = 'of'
n4 = 'python'
full = n1 + n2 + n3 + n4
print(full)
print(len(full))

#ejercicio 2
print('ejercicio 2')
f1 = 'coding'
f2 = 'for'
f3 = 'all'
all = f1 + f2 + f3
print(all)
print (len(all))
#ejercicio 3
print('ejercicio 3')

empresa = 'coding for all'
# ejercicio 4
print('ejercicio 4')
print(empresa)
#ejercicio 5
print('ejercicio 5')

#ejercicio 6
print('ejercicio 6')
print(empresa.upper())

#ejercicio 7
print('ejercicio 7')
print(empresa.lower())


#ejercicio 8
print('ejercicio 8')
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

#ejercicio 9
print('ejercicio9')
palabraa = empresa.replace('coding','')
print(palabraa)

#ejercicio 10
print('ejercicio 10')
print(empresa.find('coding'))
print(empresa.index('coding'))

#ejercicio 11
print('ejercicio 11')
palabra = empresa.replace('coding for python','')
print(palabra)

#ejercicio 12
print('ejercicio 12')

cambi = 'paython for everyone'
camvio = cambi.replace('python for all','')
print (camvio)

#ejercicio 13
print('ejercicio 13')
ddd = 'coding for all'
ccc = ddd.split()
print(ccc)

#ejercicio 14
print('ejercicio 14')
ttt = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
www = ttt.split()
print(www)

#ejercicio 15
print('ejercicio 15')
first_index = ddd[0]
print(first_index)

#ejercicio 16
print('ejrcicio 16')
last_index = ddd[-1]
print(last_index)

#ejercicio 17
print ('ejercicio 17')
numero10 = ddd[10]
print(numero10)

#ejercicio 18
print('ejercicio 18')
sss = "python for everyone"
acronimo = "".join(word[0] for word in sss.split())
print(acronimo)

#ejercicio 19
print('ejercicio 19')
lll = 'Coding for all'
acronimo2 = "".join(word[0] for word in lll.split())
print(acronimo2)

#ejercicio 20
print('ejercicio 20')
eee = 'Coding For All'
print(eee.find('C'))

#ejercicio 21
print('ejercicio 21')
print(eee.find('F'))

#ejercicio 22
print('ejercicio 22')
qqq = 'coding for all people'
print(qqq.rfind('l'))

#ejercicio 23
print('ejercicio 23')
iii = 'You cannot end a sentence with because because because is a conjunction'
print (iii.find('because'))

#ejercicio 24
print('ejercicio 29')
print(iii.rindex('because'))

#ejercicio 25
print('ejercicio 25')
sas = iii.replace('because because because','')
print(sas)
#ejercicio 26
print('ejercicio 26')
print(iii.index('because'))

#ejercicio 27
print('ejercicio 27')
sas = iii.replace('because because because','')
print(sas)

#ejercicio 28
print('ejercicio 28')
sus = 'Coding For All'
if sus.find('') == 0:
    print('Si esta en la cadena')
else:
    print('No esta en la cadena')


#ejercicio 29
print('ejercicio 29')
if sus.find('') == -1:
    print("si termina asi")

else: print('no termina asi')

#ejercicio 30
print('ejercicio 30')
rrrr = '   Coding For All      '
sssss = rrrr.replace("   ",'')
print(sssss)

#ejercicio 31
print('ejercicio 31')
variable1 = '30DaysOfPython'
variable2 = 'thirty_days_of_python'
print(variable1.isidentifier())
print(variable2.isidentifier())

#ejercicio 32
print('ejercicio 32')
cadena = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
ferz = 'Carlos'.join(cadena)
print(ferz)


#ejercicio 33
print('ejercicio 33')
print('\n:I \n:am \n:enjoying \n:this \n:challenge')

#ejercicio 34
print('ejercicio 34')
print("\t:Name      \t:Age     \t:Country   \t:City \t:Asabeneh  \t:250     \t:Finland   \t:Helsinki")

#ejercicio 35
radius = 10
area = 3.14 * radius ** 2
# Formateando con f-string
formatear = f"The area of a circle with radius {radius} is {area} meters square."
print(formatear)

#ejercicio 36
masformateointenso = f"Las operaciones aritmeticas de 8 y 6 son su suma de {8+6},\n su resta es {8-6}, la multiplicación de \n{8*6}, su division de {8%6}, su {8//6} y su potencia de {8**6} "
print(masformateointenso)