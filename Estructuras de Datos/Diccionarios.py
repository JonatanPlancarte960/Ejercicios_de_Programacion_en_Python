# Diccionarios
"""
Archivos JSON - Ejemplo de diccionario

Los diccionarios son asociativos
se ponen en un conjunto de pares clave : valor
"""

contactos = {
    'clave': 'Valor',
    'nombre': 'Jonatan',
    'apellidos': 'Plancarte',
    'telefono': 'XXXXXXXXXX',
    'edad': 19,
    'idiomas': ['español', 'ingles'],
    'vivo': True,
    'nombre': 'Israel'
}

print(contactos['nombre'])
print(contactos['idiomas'])

del contactos['clave']
print(contactos)

contactos['correo'] = 'jonatanplancarte960is@gmail.com'
print(contactos)

contactos['nombre'] = 'Mari'
print(contactos)

print(list(contactos))
print(sorted(contactos))

contactos = sorted(contactos)
print(contactos)

print('Mari' in contactos) # Solo sirve para claves
print('telefono' in contactos)

print('----------------------------------------------------------')

telefonos = {
    'fabricante': 'Xiaomi',
    'precio': 6499,
    'versiones': {
        'nombre': 'Redmi Note 12 Pro + 5G'
    }
}

celulares = dict([
    ('camara', '50 MP'),
    ('bateria en mAh', 5000),
    ('camara', '70 MP'),
    ('pantalla', 'OLED')
])

print(celulares)

celulares = dict(
    camara = '50MP',
    bateria = 5000,
    pantalla = 'OLED' # No se puede sobreescribir un valor
)

print(celulares)

# Comprension de diccionarios

mi_diccionario = {numero: numero ** 2 for numero in (2, 3, 4, 5)}
print(mi_diccionario)

# Iteracion sobre los diccionarios

pokemones = {
    'charmander': 'fuego',
    'metagross': 'acero',
    'tapu koko': 'electrico'
}

print('-------------------------------------------------')
"""
tipo, tipo_secundario, pokemon, _, _ = ('agua', 'tierra', 'swampert', 'alegre', 'Jonatan')
print(tipo)

print('-------------------------------------------------')
"""

print(pokemones)
print(pokemones.items())
print(pokemones['charmander'])

for nombre, tipo in pokemones.items():
    print(nombre, tipo)

pokemones_datos = pokemones.items()

# Enumerate
# Es una funcion que nos devuelve un objeto enumerador

print(list(enumerate(['gato', 'perro', 'caballo', 'jirafa'])))

for i, v in enumerate(['gato', 'perro', 'caballo', 'jirafa']):
    print(i, v)

# ZIP - Itera sobre varios iterables en paraleto y genera tuplas

pregunta = ['telefono', 'nombre', 'comoda favorita']
respuestas = ['XXXXXXXXXX', 'Jonatan', 'Chocolate', 'Mexico']

asociacion = zip(pregunta, respuestas)
print(asociacion)

for p, r in asociacion:
    print(p, r)

# Funciones de los diccionarios

# Funcion keys
# Obtienes todas las claves del diccionario

print(pokemones.keys())

# Funcion values
# Obtiene todos los valores del diccionario

print(pokemones.values())

# Funcion items
# Devuelve todas las claves y los valores

print(pokemones.items()) # Clave - Valor