print(".: Filtro de Nombres :.")
print()

lista_nombres = ["Matias", "Eros", "Ulises", "Cristian", "Nicolas", "Diego", "Antonio"]

def filtrar_nombres(lista_nombres):
    nombres_filtrados = []
    vocales = ["a", "e", "i", "o", "u"]
    for i in range(len(lista_nombres)):
        letras = list(lista_nombres[i].lower())
        for j in range(len(vocales)):
            if vocales[j] in letras[0]:
                if len(lista_nombres[i]) > 5:
                    nombres_filtrados.append(lista_nombres[i])
    return nombres_filtrados

resultado = filtrar_nombres(lista_nombres)

print(f"La lista con los nombres filtrados es: {resultado}")