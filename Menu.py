from Listapersonas import Listapersonas
import os

class Menu:
    def __init__(self):
        self.lista = Listapersonas()

    def limpiar(self):
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_menu(self):
        while True:
            self.limpiar()
            print("--- MENÚ PRINCIPAL ---")
            print("1. Registrar persona:")
            print("2. Buscar persona por número de documento:")
            print("5. Salir:")
            
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.limpiar()
                self.lista.registrar_persona()
                input("Presione ENTER para continuar...")

            elif opcion == "2":
                self.limpiar()
                self.lista.buscar_por_documento()
                input("Presione ENTER para continuar...")

            elif opcion == "5":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
                input("Presione ENTER para continuar...")

menu = Menu()
menu.mostrar_menu()



#hola como estas jdfbjfbnfgjfbnfunfv