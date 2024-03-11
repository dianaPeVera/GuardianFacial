class Seguridad:
    def __init__(self, registro):
        self.registro = registro

    def visualizar_usuarios(self):
        print("Usuarios que han ingresado:")
        for registro in self.registro.registros:
            print("- Usuario: {}, Hora de entrada: {}, Hora de salida: {}".format(registro['usuario'].nombre, registro['hora_entrada'], registro['hora_salida']))

    def denegar_acceso(self, usuario):
        print("Acceso denegado para el usuario {}.".format(usuario.nombre))

    def buscar_usuario(self, nombre):
        for registro in self.registro.registros:
            if registro['usuario'].nombre == nombre:
                print("Usuario {} encontrado. Hora de entrada: {}, Hora de salida: {}".format(registro['usuario'].nombre, registro['hora_entrada'], registro['hora_salida']))
                return
        print("Usuario {} no encontrado.".format(nombre))

    def eliminar_usuario(self, nombre):
        for registro in self.registro.registros:
            if registro['usuario'].nombre == nombre:
                self.registro.registros.remove(registro)
                print("Usuario {} eliminado correctamente.".format(nombre))
                return
        print("Usuario {} no encontrado en los registros.".format(nombre))
