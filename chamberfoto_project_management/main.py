from chamberfoto_project_management.usuario import Usuario
from plataforma_gestion import PlataformaGestion

plataforma = PlataformaGestion()
usuario_actual = None
proyecto_actual = None

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Crear proyecto")
    print("4. Asignar miembro al proyecto")
    print("5. Asignar equipo audiovisual al proyecto")
    print("6. Agregar tarea al proyecto")
    print("7. Monitorear progreso del proyecto")
    print("8. Controlar presupuesto del proyecto")
    print("9. Generar informe del proyecto")
    print("10. Sugerir mejoras")
    print("11. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        rol = input("Ingrese el rol del usuario: ")
        plataforma.registrar_usuario(nombre, rol)

    elif opcion == "2":
        nombre = input("Ingrese el nombre de usuario para iniciar sesión: ")
        usuario_actual = plataforma.iniciar_sesion(nombre)

    elif opcion == "3":
        if usuario_actual:
            nombre_proyecto = input("Ingrese el nombre del proyecto: ")
            cliente = input("Ingrese el nombre del cliente: ")
            proyecto_actual = plataforma.crear_proyecto(nombre_proyecto, cliente)

    elif opcion == "4":
        if usuario_actual and proyecto_actual:
            nombre_miembro = input("Ingrese el nombre del miembro del equipo: ")
            miembro = Usuario(nombre_miembro, "Equipo")
            proyecto_actual.asignar_miembro_equipo(miembro)

    elif opcion == "5":
        if usuario_actual and proyecto_actual:
            equipo_item = input("Ingrese el equipo audiovisual a asignar: ")
            proyecto_actual.asignar_equipo_audiovisual(equipo_item)

    elif opcion == "6":
        if usuario_actual and proyecto_actual:
            descripcion_tarea = input("Ingrese la descripción de la tarea: ")
            proyecto_actual.agregar_tarea(descripcion_tarea)

    elif opcion == "7":
        if usuario_actual and proyecto_actual:
            proyecto_actual.monitorear_progreso()

    elif opcion == "8":
        if usuario_actual and proyecto_actual:
            monto = float(input("Ingrese el monto a agregar al presupuesto: "))
            proyecto_actual.controlar_presupuesto(monto)

    elif opcion == "9":
        if usuario_actual and proyecto_actual:
            proyecto_actual.generar_informe()

    elif opcion == "10":
        if usuario_actual and proyecto_actual:
            proyecto_actual.sugerir_mejoras()

    elif opcion == "11":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intente nuevamente.")
