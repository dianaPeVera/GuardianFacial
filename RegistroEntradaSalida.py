# En el archivo Registro.py
from Usuario import Usuario

class Registro:
    def __init__(self):
        self.usuarios = []

    def agregar_registro(self, usuario_nombre):
        usuario = Usuario(usuario_nombre)
        self.usuarios.append(usuario)

    def buscar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                return True
        return False

    def obtener_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                return usuario
