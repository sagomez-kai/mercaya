import sqlite3
from salida import imprimirResultados

# La base de datos aún es un desastre, y su mera existencia debería
# considerarse un crimen contra la humanidad

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

def buscar(entrada): #Buscar entrada del usuario en la base de datos
    query = 'SELECT * FROM productosl WHERE lower(nombre) LIKE "%{}%"'.format(entrada) #Ignorar mayúsculas
    cursor.execute(query)
    resultado = cursor.fetchall()
    if (resultado): #Solo imprimir si lo que se buscó está en la BD
        imprimirResultados(resultado)
        return resultado
    else: # Hay que arreglar esto para que no continúe el programa
        print('No se encontró el producto buscado. Intente de nuevo.')
        return None # Esto es temporal, ver arriba

def verDatos(): # Función del modo de desarrollador, aún sin usar ni completar
    query = 'SELECT * FROM productos'
    cursor.execute(query)
    resultado = cursor.fetchall()
    imprimirResultados(resultado)

# Plantillas para otras funciones de desarrollador
#def addDatos():
#    a

#def eliminarDatos():
#    print('Ingrese fila a eliminar')
#    query = 'DELETE FROM productos WHERE id=1'#.format(input('> '))
#    cursor.execute(query)
#    resultado = cursor.fetchall()
