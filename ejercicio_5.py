print(".: Simulador de Carrito de Compras :.")
print()

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: $"))

producto_mayor = producto
precio_mayor = precio

total_gastado = 0.0

while producto.lower() != "fin":

    total_gastado += precio

    if precio > precio_mayor:
        precio_mayor = precio
        producto_mayor = producto

    print()
    producto = input("Ingrese el nombre del producto: ")
    if producto.lower() != "fin":
        precio = float(input("Ingrese el precio del producto: $"))

print()
print(".: Detalle :.")
print()
print(f"> El total gastado es : ${total_gastado}")
print()
print(f"> El producto más caro es: {producto_mayor} y su precio es: ${precio_mayor}")
print()