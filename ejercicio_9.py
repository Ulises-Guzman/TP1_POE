print(".: Compresión de Datos Básica :.")
print()

lista_datos = ['a', 'a', 'b', 'c', 'c', 'c']
#lista_datos = ['b', 'c', 'a', 'c', 'c', 'a'] Test con la lista desordenada

def comprimir_datos(lista_datos):
    lista_comprimida = []
    lista_ordenada = sorted(lista_datos)
    print(lista_ordenada)
    print()
    for i in range(len(lista_ordenada)):
        cont = 0
        sub_lista = []
        if i == 0:
            cont = lista_ordenada.count(lista_ordenada[i])
            sub_lista.append(lista_ordenada[i])
            sub_lista.append(cont)
            lista_comprimida.append(sub_lista)
        elif lista_ordenada[i] != lista_ordenada[i - 1]:
            cont = lista_ordenada.count(lista_ordenada[i])
            sub_lista.append(lista_ordenada[i])
            sub_lista.append(cont)
            lista_comprimida.append(sub_lista)
    return lista_comprimida

compresion = comprimir_datos(lista_datos)
print(f"> La compresión de datos es la siguiente: {compresion}")