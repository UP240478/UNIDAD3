# ejercicio 1
mi_lista = []
#ejercicio 2
lista = [5,4,3,2,1]
print(lista)
#ejercicio 3
print('ejercicio 3')
print(len(lista))
#ejercicio 4
print('ejercicio 4')
primero = lista[0]
medio = lista[2]
ultimo = lista[4]
print(primero)
print(medio)
print(ultimo)
#ejercicio 5
print('ejercicio 5')
mixed_data_types = ['Carlos Eduardo', 19, 1.85, 'single', 'uruguay 210']
print(mixed_data_types)
#ejercicio 6
print('ejercicio 6')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#ejercicio 7
print('ejercicio 7')
print(it_companies)
#ejercicio 8
print('ejercicio 8')
print(len(it_companies))
#ejercicio 9
print('ejercicio 9')
empresas = it_companies[0], it_companies[3], it_companies[5]
print(empresas)
#ejercicio 10   
print('ejercicio 10')
cambio = [company.replace('Facebook','Twitter') for company in it_companies]
print(cambio)
#ejercicio 11
print('ejercicio 11')
it_companies.append('TI')
print(it_companies)
#ejercicio 12
print('ejercicio 12')
it_companies.insert(len(it_companies) // 2, 'TI')
print(it_companies)
#ejercicio 13
print('ejercicio 13')
print(it_companies[3].upper())
#ejercicio 14
print('ejercicio 14')
muchas = '#;'.join(it_companies)
print(muchas)
#ejercicio 15
print('ejercicio 15')
if 'Apple' in it_companies:
    print('Apple esta en la lsita de empresas')
else:
    print('Apple no esta en la lista de empresas')

#ejercicio 16
print('ejercicio 16')
it_companies.sort()
print(it_companies)
#ejercicio 17
print('ejercicio 17')
it_companies.reverse()
print(it_companies)
#ejercicio 18
print('ejercicio 18')
print(it_companies[4:9])
#ejercicio 19
print('ejercicio 19')
print(it_companies[0:3])
#ejercicio 20
print('ejercicio 20')
it_companies.pop(0)
for _ in range(1):
    it_companies.pop(0)
print(it_companies)
#ejercicio 21
print('ejercicio 21')
it_companies.pop(0)
print(it_companies) 
#ejercicio 22
print('ejercicio 22')
it_companies.pop(0)
for _ in range(1):
    it_companies.pop(0)
print(it_companies)
#ejercicio 23
print('ejercicio 23')
corte = it_companies.pop()
print(corte)
#ejercicio 24
print('ejercicio 24')
it_companies.pop()
print(it_companies)
#ejercicio 25
print('ejercicio 25')
it_companies.clear()
print(it_companies)
#ejercicio 26
print('ejercicio 26')

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

#ejercicio 27
print('ejercicio 27')
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)
# ejercicio parte 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
maxima = ages[0]
minima = ages[-1]
print('Edad mínima:',minima)
print('Edad máxima:',maxima)

#ejercicio 2
print('ejercicio 2')
ages.sort()
print(ages)
#ejercicio 3
print('ejercicio 3')
intermedio = ages[len(ages) // 2]
print(intermedio)
#ejercicio 4
print('ejercicio 4')
promedio = len(ages)
promedio2 = sum(ages)
print(promedio2 / promedio)
#ejercicio 5
print('ejercicio 5')
rango = max(ages) - min(ages)
print(rango)

# ejercicio 6
print('ejercicio 6')
average_age = sum(ages) / len(ages)
min_diff = abs(min(ages) - average_age)
max_diff = abs(max(ages) - average_age)
print('Diferencia mínima:', min_diff)
print('Diferencia máxima:', max_diff)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]


#ejercicio 1
print('ejercicio 1')
middle_index = len(countries) // 2
middle_country = countries[middle_index]
print('el pais intermedio es:', middle_country)

#ejercicio 2
print('ejercicio 2')
if len(countries) % 2 == 0:
    first_half = countries[:len(countries) // 2]
    second_half = countries[len(countries) // 2:]
else:
    first_half = countries[:len(countries) // 2 + 1]
    second_half = countries[len(countries) // 2 + 1:]

print('First half:', first_half)
print('Second half:', second_half)


#ejercicio 3
print('ejercicio 3')
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries_list
print('First country:', first)
print('Second country:', second)
print('Third country:', third)
print('Scandic countries:', scandic_countries)

