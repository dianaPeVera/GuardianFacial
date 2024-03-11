# En el archivo Usuario.py

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hora_entrada = None
        self.hora_salida = None
        self.dentro_del_bazar = False

    def marcar_entrada(self, hora_entrada):
        self.hora_entrada = hora_entrada
        self.dentro_del_bazar = True

    def marcar_salida(self, hora_salida):
        self.hora_salida = hora_salida
        self.dentro_del_bazar = False
