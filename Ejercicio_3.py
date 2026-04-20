print(".: Inversión de Frases :.")
print()

frase = input("Escriba una frase: ")

def invertir_frase(frase):
    inversion = frase.split(' ')
    inversion.reverse()
    return inversion

def imprimir(frase_invertida):
    print()
    print(f"> La frase original es: {frase}")
    print()
    print(f"> La frase invertida es: {frase_invertida}")

if frase != "":
    frase_invertida = invertir_frase(frase)
    imprimir(frase_invertida)
else:
    print("No se ingresó frase...")
