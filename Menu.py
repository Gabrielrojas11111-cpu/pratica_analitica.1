from Listapersonas import Listapersonas
import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    lista = Listapersonas()

    while True:
        limpiar()
        print("1️Registrar persona")
        print("2️Buscar personas por tipo de documento")
        print("3️Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            lista.registrar_persona()
            input("Presione ENTER para continuar...")

        elif opcion == "2":
            limpiar()
            lista.buscar_por_tipo_documento()
            input("Presione ENTER para continuar...")

        elif opcion == "3":
            limpiar()
            print("Gracias por usar el sistema. Hasta luego.")
            break

        else:
            limpiar()
            print("Opción no válida. Intente nuevamente.")
            input("Presione ENTER para continuar...")