import time
import json
import csv

ARCHIVO_JSON = "estudiantes.json"
ARCHIVO_CSV = "estudiantes.csv"

total_estudiantes = []

# -------------------------------------------------------
#   FUNCIONES PARA JSON Y CSV
# -------------------------------------------------------

# ✔ Guardar en JSON
def guardarJSON():
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(total_estudiantes, archivo, indent=4)
    print("\n[OK] Datos guardados en estudiantes.json\n")


# ✔ Cargar desde JSON
def cargarJSON():
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return []   # si no existe, lista vacía


# ✔ Exportar a CSV
def exportarCSV():
    with open(ARCHIVO_CSV, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["id", "nombre", "apellido", "grado"])  # encabezados
        for est in total_estudiantes:
            writer.writerow([est["id"], est["nombre"], est["apellido"], est["grado"]])

    print("\n[OK] Datos exportados a estudiantes.csv\n")


# -------------------------------------------------------
#   FUNCIÓN CREAR ESTUDIANTE
# -------------------------------------------------------
def crearEstudiante():
    while True:
        try:
            # --- VALIDAR ID ÚNICO ---
            while True:
                id = int(input('Ingrese el ID del estudiante: '))
                repetido = False

                for estudiante in total_estudiantes:
                    if estudiante['id'] == id:
                        repetido = True
                        print("[ERROR]: Este ID ya existe, ingrese otro.")
                        break

                if not repetido:
                    break

            # --- VALIDAR NOMBRE ---
            while True:
                nombre = input('Ingrese el nombre del estudiante: ')
                if nombre.isalpha():
                    break
                print("[ERROR]: El nombre solo debe contener letras.")

            # --- VALIDAR APELLIDO ---
            while True:
                apellido = input('Ingrese el apellido del estudiante: ')
                if apellido.isalpha():
                    break
                print("[ERROR]: El apellido solo debe contener letras.")

            grado = int(input('Ingrese el grado del estudiante: '))

            estudiante = {
                'id': id,
                'nombre': nombre,
                'apellido': apellido,
                'grado': grado
            }

            total_estudiantes.append(estudiante)
            guardarJSON()  # <<< Guarda cada vez que creas un estudiante
            print("\nEstudiante agregado:", estudiante)

            salir = input('Desea agregar otro estudiante? (s/n): ')
            if salir.lower() == 'n':
                print(f'\nTotal de estudiantes: {total_estudiantes}')
                break

        except ValueError:
            print('[ERROR]: Valores no válidos, ingrese nuevamente los datos.\n')

# -------------------------------------------------------
#   FUNCIÓN ELIMINAR
# -------------------------------------------------------
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


# -------------------------------------------------------
#   FUNCIÓN ACTUALIZAR
# -------------------------------------------------------
def actualizar(estudiantes):
    if not estudiantes:
        print("No hay estudiantes para actualizar.")
        return

    id_buscar = int(input("Ingrese el ID del estudiante a actualizar: "))

    encontrado = False
    for est in estudiantes:
        if est["id"] == id_buscar:
            encontrado = True
            print(f"Estudiante encontrado: {est}")

            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            grado = int(input("Ingrese el nuevo grado: "))

            est["nombre"] = nombre
            est["apellido"] = apellido
            est["grado"] = grado

            guardarJSON()  # <<< Guardar cambios
            print("\nEstudiante actualizado correctamente:")
            print(est)
            break

    if not encontrado:
        print("[ERROR]: No existe un estudiante con ese ID.")


# -------------------------------------------------------
#   FUNCIÓN LEER
# -------------------------------------------------------
def leer(estudiantes):
    if not estudiantes:
        print("No hay información")
    else:
        print("\n----- Lista de estudiantes -----")
        for est in estudiantes:
            print(f"id: {est['id']}, nombre: {est['nombre']}, apellido: {est['apellido']}, grado: {est['grado']}")
        print("--------------------------------\n")


# -------------------------------------------------------
#   MENÚ PRINCIPAL
# -------------------------------------------------------
def menu():
    while True:
        try:
            opcion = int(input(
                f'\n!------------------ Menu Principal ------------------!\n'
                f'1. Crear estudiante\n'
                f'2. Eliminar estudiante\n'
                f'3. Actualizar estudiante\n'
                f'4. Mostrar estudiantes\n'
                f'5. Exportar a CSV\n'
                f'6. Salir\n'
                f'Opcion: '
            ))

            if opcion == 1:
                crearEstudiante()
            elif opcion == 2:
                eliminar(total_estudiantes)
            elif opcion == 3:
                actualizar(total_estudiantes)
            elif opcion == 4:
                leer(total_estudiantes)
            elif opcion == 5:
                exportarCSV()
            elif opcion == 6:
                print()
                for tiempo in range(3, 0, -1):
                    print(f"Cerrando el programa en: {tiempo}...")
                    time.sleep(1)
                print("[AVISO]: El programa se cerró.")
                break
            else:
                print("[ERROR]: Seleccione una opción válida.")
        except ValueError:
            print('[ERROR]: Ingrese solo números.')
            continue


# ---------------------------------------
#   Cargar JSON al iniciar
# ---------------------------------------
total_estudiantes = cargarJSON()

menu()