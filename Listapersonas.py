from Datos import Datos

class Listapersonas:
    def __init__(self):
        self.lista = []   

    def registrar_persona(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        tipo_doc = input("Tipo de documento: ")
        documento = int(input("Número de documento: "))

        if documento % 2 != 0:
            print("\n El documento es impar. NO se puede registrar.\n")
            return

        persona = Datos(nombre, apellido, tipo_doc, documento)
        self.lista.append(persona)

        print("\n✔ Persona registrada correctamente.\n")

    def buscar_por_tipo_documento(self):
        tipo = input("Ingrese el tipo de documento a buscar: ")

        print("\n--- RESULTADOS ---")
        encontrados = 0
        for p in self.lista:
            if p.tipo_doc.lower() == tipo.lower():
                print(f"{p.nombre} {p.apellido} - Documento: {p.documento}")
                encontrados += 1

        if encontrados == 0:
            print("No se encontraron personas con ese tipo de documento.\n")