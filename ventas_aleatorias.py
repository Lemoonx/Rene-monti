import random
import globales

def ventas_aleatorias():
    ventas = globales.leer_archivo_json('ventas.json')
    productos = ["Cafe Americano","Te Chai","Croissant","Jugo Naranja","Panini de Pavo y Queso","Pastel de Zanahoria","Espresso Doble","Batido de Frutas","Muffin","Ensalada","Chocolate Caliente","Tarta de Frambuesa","Sandwich de Huevo","Galletas de Avena","Frappé de Caramelo"]
    for producto in productos:
        nombre = producto
        precio = random.randint(20, 100)*100
        iva = precio *0.19

        nueva_venta = {
            "nombre": nombre,
            "precio": precio,
            "iva": iva
        }
        ventas.append(nueva_venta)
    globales.guardar_archivo_json('ventas.json', ventas)
    input("ventas cargadas")




    
        