from Datos import Datos

class Listapersonas:
    def __init__(self):
        self.lista = [] 

    def registrar_persona(self):
        print("=== REGISTRAR PERSONA ===")

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        tipo_doc = input("Tipo de documento: ")
        documento = int(input("Número de documento (solo pares): "))

        if documento % 2 != 0:
            print("\n ERROR: El documento es impar. No se puede registrar.\n")
            return

        persona = Datos(nombre, apellido, tipo_doc, documento)
        self.lista.append(persona)

        print("\n Persona registrada correctamente.\n")

    def buscar_por_tipo_documento(self):
        print("=== BUSCAR PERSONAS POR TIPO DE DOCUMENTO ===")
        tipo = input("Tipo de documento a buscar: ")

        encontrados = False

        print("\n--- RESULTADOS ---")
        for p in self.lista:
            if p.tipo_doc.lower() == tipo.lower():
                print(f"{p.nombre} {p.apellido} - Documento: {p.documento}")
                encontrados = True

        if not encontrados:
            print("No se encontraron personas con ese tipo de documento.\n")

    def agregar_persona(self):
        print("=== AGREGAR PERSONA ===")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        tipo_doc = input("Tipo de documento: ")
        documento = int(input("Número de documento: "))

        persona = Datos(nombre, apellido, tipo_doc, documento)
        self.lista.append(persona)

        print("\n Persona agregada correctamente.\n")

    def eliminar_persona(self):
        print("=== ELIMINAR PERSONA ===")
        documento = int(input("Ingrese el número de documento de la persona a eliminar: "))

        for p in self.lista:
            if p.documento == documento:
                self.lista.remove(p)
                print(f"\n Persona con documento {documento} eliminada correctamente.\n")
                return

        print("\n No se encontró ninguna persona con ese documento.\n")
