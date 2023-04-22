def imprimirResultados(resultados): # Imprimir resultados de búsqueda
    i = 1
    print('')
    for entrada in resultados:
        print(str(i) + ' ' + entrada[0] + '\t' + 'disponible en: ' 
              + entrada[1] + '\t')
        i += 1

def imprimirTienda(datosTienda): # Imprimir la mejor tienda para el usuario
    print('\nPara conseguir la mayor cantidad de productos al mejor precio, debería comprar en: ')
    print(datosTienda['tienda'])
    print('Por un total de: ' + str(datosTienda['total']))
