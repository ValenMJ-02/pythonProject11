from usuario import Usuario
from proyecto import Proyecto

class PlataformaGestion:
    def __init__(self):
        self.usuarios = []
        self.proyectos = []

    def iniciar_sesion(self, usuario):
        for u in self.usuarios:
            if u.nombre == usuario:
                print(f"{u.nombre} ha iniciado sesión.")
                return u
        print("Usuario no registrado.")
        return None

    def registrar_usuario(self, nombre, rol):
        usuario = Usuario(nombre, rol)
        self.usuarios.append(usuario)
        print(f"Usuario {nombre} registrado exitosamente.")
        return usuario

    def crear_proyecto(self, nombre, cliente):
        proyecto = Proyecto(nombre, cliente)
        self.proyectos.append(proyecto)
        print(f"Proyecto '{nombre}' creado exitosamente.")
        return proyecto
