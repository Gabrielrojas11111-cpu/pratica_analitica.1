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
            print("1. Registrar persona")
            print("2. Buscar personas por tipo de documento")
            print("3. Agregar persona")
            print("4. Eliminar persona")
            print("5. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.limpiar()
                self.lista.registrar_persona()
                input("\nPresione ENTER para continuar...")

            elif opcion == "2":
                self.limpiar()
                self.lista.buscar_por_tipo_documento()
                input("\nPresione ENTER para continuar...")

            elif opcion == "3":
                self.limpiar()
                self.lista.agregar_persona()
                input("\nPresione ENTER para continuar...")

            elif opcion == "4":
                self.limpiar()
                self.lista.eliminar_persona()
                input("\nPresione ENTER para continuar...")

            elif opcion == "5":
                self.limpiar()
                print("Gracias por usar el sistema. Hasta luego.")
                break

            else:
                self.limpiar()
                print("Opción no válida. Intente nuevamente.")
                input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()
