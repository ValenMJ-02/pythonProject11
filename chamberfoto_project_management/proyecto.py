from equipo import Equipo

class Proyecto:
    def __init__(self, nombre, cliente):
        self.nombre = nombre
        self.cliente = cliente
        self.equipo = []
        self.equipo_audiovisual = []
        self.tareas = []
        self.progreso = 0
        self.presupuesto = 0

    def asignar_miembro_equipo(self, miembro):
        self.equipo.append(miembro)
        print(f"Miembro '{miembro.nombre}' asignado al proyecto '{self.nombre}'.")

    def asignar_equipo_audiovisual(self, equipo_item):
        equipo = Equipo(equipo_item)
        self.equipo_audiovisual.append(equipo)
        print(f"Equipo '{equipo_item}' asignado al proyecto '{self.nombre}'.")

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "completada": False}
        self.tareas.append(tarea)
        print(f"Tarea '{descripcion}' agregada al proyecto '{self.nombre}'.")

    def monitorear_progreso(self):
        completadas = sum(1 for tarea in self.tareas if tarea["completada"])
        self.progreso = (completadas / len(self.tareas)) * 100 if self.tareas else 0
        print(f"Progreso del proyecto '{self.nombre}': {self.progreso}%")

    def controlar_presupuesto(self, monto):
        self.presupuesto += monto
        print(f"Presupuesto del proyecto '{self.nombre}' actualizado a {self.presupuesto}")

    def generar_informe(self):
        informe = {
            "nombre": self.nombre,
            "cliente": self.cliente,
            "progreso": self.progreso,
            "presupuesto": self.presupuesto,
            "tareas": [t["descripcion"] for t in self.tareas]
        }
        print("Informe del proyecto:", informe)

    def sugerir_mejoras(self):
        print(f"Sugerencias de mejora para el proyecto '{self.nombre}': Explorar nuevas tendencias audiovisuales.")
