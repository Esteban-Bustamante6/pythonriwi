
def eliminar(estudiantes):
    if not estudiantes:
        print("No hay estudiantes para eliminar.")
        return

    try:
        id_buscar = int(input("Ingrese el ID del estudiante a eliminar: "))
    except ValueError:
        print("Debe ingresar un número entero.")
        return

    encontrado = False
    for est in estudiantes:
        if est["id"] == id_buscar:
            encontrado = True
            print(f"Estudiante encontrado: {est}")

            confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ")

            if confirmacion.lower() == 's':
                estudiantes.remove(est)
                print("Estudiante eliminado correctamente.")
            else:
                print(" Operación cancelada.")
            break

    if not encontrado:
        print("No existe un estudiante con ese ID.")