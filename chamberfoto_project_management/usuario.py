class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        return f"Usuario: {self.nombre} - Rol: {self.rol}"
