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

        print("\n✔ Persona registrada correctamente.\n")

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