class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

    def __str__(self):
        return f"Equipo: {self.nombre} - Disponible: {'Sí' if self.disponible else 'No'}"

