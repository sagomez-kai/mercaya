from procesar import buscar
from procesar import crearLista
from procesar import continuarLista
from salida import imprimirBaratos

def main():
    print('¡Bienvenido a Mercaya!\n\nIngrese el filtro que desea:')
    print('1. Buscar y mostrar opciones más baratas\n2. Buscar y mostrar opciones más cercanas (NO IMPLEMENTADO)')
    opcion = input('> ')
    print('\nAhora ingrese un producto que desee buscar.')
    resultado = buscar(input('> ')) #Buscar productos...
    print('\nSeleccione los productos que quiera añadir a su lista.')
    lista = crearLista(resultado) #Crear lista de mercado...
    while True: #Continuar búsqueda y expandir lista...
        print('\n¿Desea añadir más productos?\n1. Sí\n2. No')
        if (input('> ') == '1'):
            print('\nIngrese producto a buscar:')
            resultado = buscar(input('> '))
            continuarLista(resultado, lista)
        else:
            break
    imprimirBaratos(lista)
#    print('Seleccione una opción')
#    print('¿Qué desea ver?\n1. Tiendas más baratas\n2. Tiendas más cercanas')

main()
