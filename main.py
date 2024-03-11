# En el archivo main.py

from datetime import datetime
from Camar import Camar
from Registro import Registro
from AlgoritmoFacial import AlgoritmoFacial

def dar_de_alta(registro):
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    registro.agregar_registro(nombre_usuario)
    print("Usuario dado de alta correctamente.")

def entrar_al_bazar(algoritmo_facial):
    nombre_usuario = input("Ingrese su nombre para entrar al bazar: ")
    algoritmo_facial.reconocer_rostro(nombre_usuario)

def salir_del_bazar(algoritmo_facial):
    nombre_usuario = input("Ingrese su nombre para salir del bazar: ")
    algoritmo_facial.reconocer_rostro(nombre_usuario, "salida")

def visualizar_usuarios_dados_de_alta(registro):
    print("Usuarios dados de alta:")
    for usuario in registro.usuarios:
        print("- Nombre: {}, Hora de entrada: {}, Hora de salida: {}".format(usuario.nombre, usuario.hora_entrada, usuario.hora_salida))

def visualizar_usuarios_en_bazar(registro):
    print("Usuarios dentro del bazar:")
    for usuario in registro.usuarios:
        if usuario.dentro_del_bazar:
            print("- Nombre: {}".format(usuario.nombre))

def menu_principal():
    camara = Camar()
    registro = Registro()
    algoritmo_facial = AlgoritmoFacial(camara, registro)

    while True:
        print("\nMenú Principal:")
        print("1. Dar de alta un usuario.")
        print("2. Entrar al bazar.")
        print("3. Salir del bazar.")
        print("4. Visualizar todos los usuarios dados de alta.")
        print("5. Visualizar usuarios dentro del bazar.")
        print("6. Salir del sistema.")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dar_de_alta(registro)
        elif opcion == "2":
            entrar_al_bazar(algoritmo_facial)
        elif opcion == "3":
            salir_del_bazar(algoritmo_facial)
        elif opcion == "4":
            visualizar_usuarios_dados_de_alta(registro)
        elif opcion == "5":
            visualizar_usuarios_en_bazar(registro)
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_principal()
