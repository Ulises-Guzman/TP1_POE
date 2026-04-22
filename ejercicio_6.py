print(".: Coversor de binario a decimal :.")
print()

numero_binario = input("Ingrese un número binario: ")
lista_numero_binario = list(numero_binario)
numero_decimal = 0

for i in reversed(lista_numero_binario):
    if i == '1':
        numero_decimal += int(i)**2

print()
print(f"> Coversión a decimal: {numero_decimal}")