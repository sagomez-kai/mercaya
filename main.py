from procesar import crearLista, calcularBarato, continuarLista
from persistencia import buscar
from salida import imprimirTienda

# Este código fue inspirado por un déficit crónico de sueño

def main():
    print('¡Bienvenido a Mercaya!\n\nIngrese el filtro que desea:')
    print('1. Buscar y mostrar opciones más baratas\n' 
          + '2. Buscar y mostrar opciones más cercanas (NO IMPLEMENTADO)')
    opcion = input('> ') # Esta entrada por ahora no hace nada sino ocasionar
    # un error; solo está ahí ahora para darle al usuario la ilusión de tener
    # libre albedrío y control sobre su destino terrenal
    if (opcion == 'desarrollador'): # Modo de desarrollador aún no implementado
        mainDev()
    else:
        print('\nAhora ingrese un producto que desee buscar.')
        resultado = buscar(input('> ')) #Buscar productos en la BD
        print('\nSeleccione la ID del producto que desee añadir a su lista.')
        lista = crearLista(resultado) # Crear la lista de mercado
        while True: # Continuar búsqueda y expandir lista
            print('\n¿Desea añadir más productos?\n1. Sí\n2. No')
            if (input('> ') == '1'):
                print('\nIngrese producto a buscar:')
                resultado = buscar(input('> '))
                continuarLista(resultado, lista)
            else:
                break
        barato = calcularBarato(lista)
        imprimirTienda(barato)

# La función de opciones de desarrollador. Falta implementar esto, tal vez
# sea en la próxima entrega
#def mainDev():
#    print('\nUsted es un desarrollador\nSeleccione su acción')
#    print('1. Eliminar entradas en BD\n2. Añadir entradas a BD\n' 
#          + '3. Ver entradas de BD')
#    match input('> '):
#        case '1':
#            persistencia.eliminarDatos()
#        case '2':
#            persistencia.addDatos()
#        case '3':
#            persistencia.verDatos()

main()
