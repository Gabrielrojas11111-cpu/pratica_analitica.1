from Datos import Datos

class Listapersonas:
    def __init__(self):
        # Inicializa la lista vacía donde se almacenarán las personas registradas
        self.lista = [] 

    def registrar_persona(self):
        # Permite registrar una nueva persona en la lista
        print("=== REGISTRAR PERSONA ===")

        # Se solicitan los datos básicos de la persona
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        tipo_doc = input("Tipo de documento: ")
        documento = int(input("Número de documento (solo pares): "))

        # Validación: el documento debe ser par
        if documento % 2 != 0:
            print("ERROR: El documento es impar. No se puede registrar.")
            return

        # Se crea un objeto de tipo Datos y se agrega a la lista
        persona = Datos(nombre, apellido, tipo_doc, documento)
        self.lista.append(persona)

        print("Persona registrada correctamente.")

    def buscar_por_documento(self):
        # Permite buscar una persona en la lista por su número de documento
        print("=== BUSCAR PERSONA POR DOCUMENTO ===")
        try:
            doc = int(input("Ingrese el número de documento: "))
        except:
            # Manejo de error si el usuario no ingresa un número válido
            print("ERROR: Debe ingresar un número.")
            return

        print("--- RESULTADOS ---")
        # Se recorre la lista buscando coincidencias
        for p in self.lista:
            if p.documento == doc:
                print(f"{p.nombre} {p.apellido} - Tipo: {p.tipo_doc} - Documento: {p.documento}")
                return
        
        # Si no se encuentra la persona
        print("No se encontró ninguna persona con ese documento.")

    def editar_persona(self):
        # Permite editar los datos de una persona existente
        print("=== EDITAR PERSONA ===")
        try:
            doc = int(input("Ingrese el número de documento de la persona a editar: "))
        except:
            print("ERROR: Debe ingresar un número.")
            return

        # Se busca la persona en la lista
        for p in self.lista:
            if p.documento == doc:
                print(f"Editando a {p.nombre} {p.apellido}...")
                # Si el usuario deja el campo vacío, se conserva el valor anterior
                p.nombre = input(f"Nuevo nombre (actual: {p.nombre}): ") or p.nombre
                p.apellido = input(f"Nuevo apellido (actual: {p.apellido}): ") or p.apellido
                p.tipo_doc = input(f"Nuevo tipo de documento (actual: {p.tipo_doc}): ") or p.tipo_doc
                try:
                    nuevo_doc = input(f"Nuevo número de documento (actual: {p.documento}): ")
                    if nuevo_doc:
                        nuevo_doc = int(nuevo_doc)
                        # Validación: el documento debe ser par
                        if nuevo_doc % 2 != 0:
                            print("ERROR: El documento debe ser par. No se actualizó.")
                        else:
                            p.documento = nuevo_doc
                except:
                    print("ERROR: Documento inválido. No se actualizó.")
                print("Persona editada correctamente.")
                return
        
        print("No se encontró ninguna persona con ese documento.")

    def eliminar_persona(self):
        # Permite eliminar una persona de la lista por su documento
        print("=== ELIMINAR PERSONA ===")
        try:
            doc = int(input("Ingrese el número de documento de la persona a eliminar: "))
        except:
            print("ERROR: Debe ingresar un número.")
            return

        # Se busca la persona en la lista y se elimina
        for p in self.lista:
            if p.documento == doc:
                self.lista.remove(p)
                print(f"Persona con documento {doc} eliminada correctamente.")
                return
        
        # Si no se encuentra la persona
        print("No se encontró ninguna persona con ese documento.")
