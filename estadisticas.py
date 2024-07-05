import os
import math
import globales

def valor_mas_alto():
    todos_los_productos = globales.leer_archivo_json('ventas.json')
    productos_ordenados= sorted(todos_los_productos, key=lambda x: x['precio'], reverse=True)

    print("| Nombre | Valor | iva ")
    for producto in productos_ordenados[:1]:
        nombre = producto['nombre']
        precio = producto['precio']
        iva = producto['iva']
    print(f"| {nombre} | {precio} | {iva} |")

def valor_iva_mas_bajo():
    todos_los_productos = globales.leer_archivo_json('ventas.json')
    productos_ordenados= sorted(todos_los_productos, key=lambda x: x['iva'], reverse=False)

    print("| Nombre | Valor | iva ")
    for producto in productos_ordenados[:1]:
        nombre = producto['nombre']
        precio = producto['precio']
        iva = producto['iva']
    print(f"| {nombre} | {precio} | {iva} |")


def promedio():
    todos_los_productos = globales.leer_archivo_json('ventas.json')
    suma_precios = 0
    cantidad_precios = 0

    for producto in todos_los_productos:
        suma_precios += producto['precio'] 
        cantidad_precios += 1
    promedio = suma_precios / cantidad_precios

    print(f"El promedio de precios es de {promedio}")

def media():
    todos_los_productos = globales.leer_archivo_json('ventas.json')
    suma_precios = 0
    cantidad_precios = 0

    for producto in todos_los_productos:
        suma_precios += math.log(producto['precio']) 
        cantidad_precios += 1
    promedio = math.exp(suma_precios / cantidad_precios)

    print(f"La media geometrica de precios es de {promedio}")




def estadisticas():
    os.system("cls")
    print("Producto con valor más alto")
    print("")
    valor_mas_alto()
    print("")
    print("Producto con valor del iva mas bajo")
    print("")
    valor_iva_mas_bajo()
    print("")
    print("Promedio valor productos")
    print("")
    promedio()
    print("")
    print("mediageometrica valor productos")
    print("")
    media()
    