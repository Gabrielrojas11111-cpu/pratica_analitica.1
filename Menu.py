from Listapersonas import Listapersonas
import os

class Menu:
    def __init__(self):
        # Inicializa la clase Menu con una instancia de Listapersonas
        # Aquí se guarda la lista de personas que se manejará en el programa
        self.lista = Listapersonas()

    def limpiar(self):
        # Limpia la pantalla dependiendo del sistema operativo
        
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_menu(self):
        # Muestra el menú principal en un bucle infinito
        # El bucle se rompe únicamente cuando el usuario selecciona la opción "Salir"
        while True:
            self.limpiar()
            print("--- MENÚ PRINCIPAL ---")
            print("1. Registrar persona")
            print("2. Buscar persona por número de documento")
            print("3. Editar persona")
            print("4. Eliminar persona")
            print("5. Salir")
            
            # Se captura la opción ingresada por el usuario
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                # Opción para registrar una nueva persona
                self.limpiar()
                self.lista.registrar_persona()
                input("Presione ENTER para continuar...")

            elif opcion == "2":
                # Opción para buscar una persona por su documento
                self.limpiar()
                self.lista.buscar_por_documento()
                input("Presione ENTER para continuar...")

            elif opcion == "3":
                # Opción para editar los datos de una persona existente
                self.limpiar()
                self.lista.editar_persona()
                input("Presione ENTER para continuar...")

            elif opcion == "4":
                # Opción para eliminar una persona de la lista
                self.limpiar()
                self.lista.eliminar_persona()
                input("Presione ENTER para continuar...")

            elif opcion == "5":
                # Opción para salir del programa
                print("Saliendo...")
                break

            else:
                # Manejo de opciones inválidas
                print("Opción inválida.")
                input("Presione ENTER para continuar...")

# Punto de entrada del programa: se crea una instancia de Menu y se ejecuta
menu = Menu()
menu.mostrar_menu()
