def verResultados(resultados): #Imprimir resultados de búsqueda
    i = 1
    print('')
    for entrada in resultados:
        print(str(i) + ' ' + entrada[0] + '\t' + 'disponible en: ' + str(entrada[1]) + '\t')
        i += 1

def imprimirBaratos(productos):
    print('\nEstas son sus mejores opciones para comprar los productos más baratos:')
    productos.sort(key=lambda x: x.tienda)
    print(('\n{0: <10}' + '\t' + 'TIENDA' + '\t' + 'PRECIO').format('NOMBRE'))
    total = 0
    for i in productos:
        total += i.precio
        print(('{0: <10}' + '\t' + str(i.tienda) + '\t' + str(i.precio)).format(str(i.nombre)))
    print('TOTAL: ' + str(total) + ' pesos.' + '\n')
