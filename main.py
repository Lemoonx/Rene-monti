import os
import globales
import estadisticas
import ventas_aleatorias


def menu_general():
    while True:
        os.system("cls")
        print("Reportes de venta")
        print("")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadisticas ")
        print("3. Salir del programa")
        
        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            ventas_aleatorias.ventas_aleatorias()
        elif opcion == 2:
            estadisticas.estadisticas()
        elif opcion == 3:
            return
        input()

if __name__ == "__main__":
    menu_general()
