'''
un diccionario es una estructura de datos
o una coleccion de datos 
que se puede modificar
'''

persona = {
    'nombre':'jose apaza',
    'edad':28,
    'altura':1.73,
    'es_casado':False,
    'gustos':['helado','fultbol','ajedrez'],
    'fecha':(19,"marzo",1996),
    'direccion':{
        'zona':'villa el carmen',
        'calle':'america',
        'numero':3165,
    }
}

#tamaño del diccionario
print( len(persona) )

#acceso a los datos
print( persona['nombre'] )
print( persona['edad'] )
print( persona['altura'] )
print( persona['es_casado'] )
print( persona['gustos'][1] )
print( persona['fecha'][1] )
print( persona['direccion'] )

#agregar mas informacion al diccionario
persona['celular'] = 7253654
persona['gustos'].append('lenteja')
print( persona )

#modificar los datos del diccionario
persona['edad'] = 30
persona['nombre'] = 'juan perez'
print( persona )

#eliminar los datos del diccionario
persona.popitem()
persona.pop('altura')
del persona['fecha']
print( persona )

#limpiar los datos del diccionario
del persona
