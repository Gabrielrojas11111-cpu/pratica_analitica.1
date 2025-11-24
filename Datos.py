class Datos:
    def __init__(self, nombre, apellido, tipo_doc, documento):
        # Constructor de la clase Datos
        # Aquí se inicializan los atributos básicos de una persona

        # Nombre de la persona
        self.nombre = nombre

        # Apellido de la persona
        self.apellido = apellido

        # Tipo de documento (ejemplo: CC, TI, Pasaporte)
        self.tipo_doc = tipo_doc

        # Número de documento (validado como par en Listapersonas)
        self.documento = documento
