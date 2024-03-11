# En el archivo AlgoritmoFacial.py
from datetime import datetime

class AlgoritmoFacial:
    def __init__(self, camara, registro):
        self.camara = camara
        self.registro = registro

    def reconocer_rostro(self, nombre_usuario, accion=None):
        foto_rostro = self.camara.capturar_rostro()
        hora_actual = datetime.now()
        usuario = self.registro.obtener_usuario(nombre_usuario)

        if accion == "salida":
            usuario.marcar_salida(hora_actual)
            print("Usuario {} ha salido del bazar.".format(nombre_usuario))
        else:
            usuario.marcar_entrada(hora_actual)
            print("Usuario {} ha entrado al bazar.".format(nombre_usuario))
