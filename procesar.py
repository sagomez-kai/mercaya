import sqlite3
from salida import verResultados

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

class Producto: #Objeto de producto
    def __init__(self, arr):
        self.nombre = arr[0]
        self.tienda = arr[1]
        self.precio = arr[2]

def buscar(entrada): #Buscar entrada del usuario en la base de datos
    query = 'SELECT * FROM productos WHERE lower(nombre) LIKE "%{}%"'.format(entrada) #Ignorar mayúsculas 
    cursor.execute(query)
    resultado = cursor.fetchall()
    if (resultado): #Solo hacer esto si lo que se buscó está en la base de datos
        verResultados(resultado)
        return resultado
    else: #Hay que arreglar esto para que detenga el programa o pida entrada de nuevo, pero luego
        print('No se encontró el producto buscado. Intente de nuevo.')

def crearLista(entrada): #Crear la lista de mercado del usuario
    lista = list() #Crear lista vacía
    while True:
        print('Ingrese un número o "t" para terminar su lista.')
        selec = input('> ')
        if (selec == 't'):
            break
        else:
            i = 0
            menor = ()
            producto = entrada[int(selec) - 1]
            query = 'SELECT * FROM precios WHERE lower(nombre) LIKE "%{}%"'.format(producto[0])
            cursor.execute(query)
            resultado = cursor.fetchall()
            for dato in resultado:
                if (i == 0):
                    menor = dato
                    i += 1
                    continue
                elif (dato[2] < resultado[i - 1][2]):
                    menor = dato
                    i += 1
                else:
                    i += 1
            lista.append(Producto(menor)) #Hacer un arreglo de objetos con cada producto
    return lista
            
def continuarLista(entrada, lista): #Añadir más productos a la lista. Esto es una copia de lo anterior
    print('')
    while True:
        print('Ingrese un número o "t" para terminar su lista.')
        selec = input('> ')
        if (selec == 't'):
            break
        else:
            i = 0
            producto = entrada[int(selec) - 1]
            query = 'SELECT * FROM precios WHERE lower(nombre) LIKE "%{}%"'.format(producto[0])
            cursor.execute(query)
            resultado = cursor.fetchall()
            for dato in resultado:
                if (i == 0):
                    menor = dato
                    i += 1
                    continue
                elif (dato[2] < resultado[i - 1][2]):
                    menor = dato
                    i += 1
                else:
                    i += 1
            lista.append(Producto(menor)) #Hacer un arreglo de objetos con cada producto
