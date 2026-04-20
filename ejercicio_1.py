print(".: Calculadora de Promedio Movil :.")
print()

lista_numeros = [12, 24, 43, 96]

def promedio_movil(lista_numeros):
    lista_promedio = []
    promedio = 0
    for i in range(len(lista_numeros)):
        if i != 0:
            valor_actual = lista_numeros[i]
            valor_anterior = lista_numeros[i - 1]
            promedio = float((valor_actual + valor_anterior) / 2)
            lista_promedio.append(promedio)
    return lista_promedio

resultado = promedio_movil(lista_numeros)

print(f"> La lista de numeros es: {lista_numeros}")
print()
print(f"> La lista de promedio movil es: {resultado}")
