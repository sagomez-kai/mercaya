import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Objeto de producto
# Tal vez pruebe ser innecesario, pero por ahora el programa funciona con él
class Producto:
    def __init__(self, arr):
        self.nombre = arr[0]
        self.tienda = arr[1]
        self.precio = arr[2]

def crearLista(entrada): # Crear la lista de mercado del usuario
    lista = [] # Crear lista vacía
    while True:
        print('Ingrese un número o "t" para terminar su lista.')
        selec = input('> ')
        if (selec == 't'):
            break
        else:
            producto = entrada[int(selec) - 1] # Esto escoge un producto de
            # los resultados que da imprimirResultados
            query = 'SELECT nombre, tienda, precio FROM precios WHERE lower(nombre) LIKE "%{}%"'.format(producto[0])
            cursor.execute(query)
            resultado = cursor.fetchall()
            for dato in resultado:
                lista.append(Producto(dato)) # Hacer un arreglo de objetos de
                # tipo Producto (ver arriba) con cada resultado
    return lista
            
def continuarLista(entrada, lista):
    # Esta función es igual a la de arriba, pero sin un return
    # Tampoco crea una lista, sino que usa la existente
    print('')
    while True:
        print('Ingrese un número o "t" para terminar su lista.')
        selec = input('> ')
        if (selec == 't'):
            break
        else:
            producto = entrada[int(selec) - 1]
            query = 'SELECT nombre, tienda, precio FROM precios WHERE lower(nombre) LIKE "%{}%"'.format(producto[0])
            cursor.execute(query)
            resultado = cursor.fetchall()
            for dato in resultado:
                lista.append(Producto(dato))

def calcularBarato(lista):
    lista.sort(key=lambda x: x.tienda) # Organizar la lista de objetos por
    # tienda
    opciones = []
    precioTienda = 0 # El precio total de los productos elegidos de una tienda
    numProductos = 0 # Cuántos productos seleccionados tiene una tienda
    tienda = lista[0].tienda
    for i in lista: # Obtener los datos de arriba y ponerlos en diccionarios
        if (tienda == i.tienda):
            precioTienda += i.precio
            numProductos += 1
            razon = precioTienda / numProductos
        else:
            opciones.append({'tienda': tienda, 'total': precioTienda,
                             'num': numProductos, 'razon': razon})
            tienda = i.tienda
            precioTienda = i.precio
            numProductos += 0
    opciones.append({'tienda': tienda, 'total': precioTienda,
                     'num': numProductos, 'razon': razon})
    mejor = opciones[0]
    for i in opciones: 
        # Calcular la tienda más barata
        # Esto usa una razón precio a producto para evitar casos ridículos
        # como que una tienda tenga 1000 productos por un total de 100 pesos 
        # y que otra tenga 10 productos a 1 peso.
        # Si no usáramos razones, el programa
        # organizaría por precio y creería que la segunda tienda es mejor, pero
        # obviamente es mejor la tienda con más productos
        if (i['razon'] < mejor['razon']):
            mejor = i
        elif (i['razon'] == mejor['razon']):
            if (i['num'] > mejor['num']):
                mejor = i
            else:
                continue
        else:
            continue
    return mejor
