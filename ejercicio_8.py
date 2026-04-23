import random

print(".: Análisis de rango de una lista de números:.")
print()

lista_aleatoria = [random.randint(1, 100) for _ in range(10)]

print(f"> La lista aleatoria es: {lista_aleatoria}")
print()

num_max = max(lista_aleatoria)
num_min = min(lista_aleatoria)

resultado = num_max - num_min

print(f"> La diferencia entre el número máximo y mínimo es: {resultado}")