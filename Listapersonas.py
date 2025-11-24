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
            print("ERROR: El documento es impar. No se puede registrar.")
            return

        persona = Datos(nombre, apellido, tipo_doc, documento)
        self.lista.append(persona)

        print("Persona registrada correctamente.")

    def buscar_por_documento(self):
        print("=== BUSCAR PERSONA POR DOCUMENTO ===")
        try:
            doc = int(input("Ingrese el número de documento: "))
        except:
            print("\nERROR: Debe ingresar un número.\n")
            return

        print("\n--- RESULTADOS ---")
        for p in self.lista:
            if p.documento == doc:
                print(f"{p.nombre} {p.apellido} - Tipo: {p.tipo_doc} - Documento: {p.documento}")
                return
        
        print("No se encontró ninguna persona con ese documento.\n")
 
