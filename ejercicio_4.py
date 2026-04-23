print(".: Buscador de duplicados :.")
print()

lista = ["motor", "rueda", "puerta", "chasis", "rueda", "parabrisas", "butaca", "motor", "chasis"]
# lista = ["motor", "caja", "transmision"] # Para verificar por la via de no duplicados

def encontrar_duplicado(lista):
    lista_duplicado = []
    aux = ""
    for i in range(len(lista)):
        aux = lista[i]
        for j in range(i + 1, len(lista)):
            if aux.lower() == lista[j].lower():
                lista_duplicado.append(lista[j])
    return lista_duplicado

def imprimir(resultado):
    print(f"> Existen duplicados, la lista es: {resultado}")

resultado = encontrar_duplicado(lista)

if resultado:
    imprimir(resultado)
else:
    print("> No se encontraron duplicados")