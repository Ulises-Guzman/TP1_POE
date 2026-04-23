print(".: Traductor de P o Jeringozo :.")
print()

palabra = input("Ingrese la palabra a traducir: ")
lista_palabra = list(palabra)
vocales = ["a", "e", "i", "o", "u"]
lista_p = []

for i in range(len(lista_palabra)):
    if lista_palabra[i] in vocales:
        lista_p.append(lista_palabra[i])
        lista_p.append("p" + lista_palabra[i])
    else:
        lista_p.append(lista_palabra[i])

traduccion_p = "".join(lista_p)
print(f"> La palabra traducida es: {traduccion_p.lower()}")