import time
import json
import csv

total_estudiantes = []

ARCHIVO_JSON = "estudiantes.json"
ARCHIVO_CSV = "estudiantes.csv"

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
    with open(ARCHIVO_CSV, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["id", "nombre", "apellido", "grado"])  # encabezados
        for est in total_estudiantes:
            writer.writerow([est["id"], est["nombre"], est["apellido"], est["grado"]])

    print("\n[OK] Datos exportados a estudiantes.csv\n")

# * Funcion crear estudiantes
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
                    break  # ID válido, salir del ciclo y seguir

            # ? --- VALIDAR NOMBRE ---
            while True:
                nombre = input('Ingrese el nombre del estudiante: ')
                if nombre.isalpha():
                    break
                print("[ERROR]: El nombre solo debe contener letras.")

            # ? --- VALIDAR APELLIDO ---
            while True:
                apellido = input('Ingrese el apellido del estudiante: ')
                if apellido.isalpha():
                    break
                print("[ERROR]: El apellido solo debe contener letras.")

            while True:
                try:
                    grado = int(input('Ingrese el grado del estudiante: '))
                    if grado <= 0:
                        print("[ERROR]: grado invalido.")
                        continue
                    elif grado > 11:
                        print("[ERROR]: grado invalido.")
                        continue
                    else:
                        break
                except ValueError:
                    print('[ERROR]: Valores no válidos, ingrese nuevamente los datos.\n')

            estudiante = {
                'id': id,
                'nombre': nombre,
                'apellido': apellido,
                'grado': grado
            }

            total_estudiantes.append(estudiante)
            guardarJSON()
            print("\nEstudiante agregado:", estudiante)

            while True:
                salir = input('Desea agregar otro estudiante? (s/n): ')
                if salir.lower() == "s":
                    print(f'\nTotal de estudiantes: {total_estudiantes}')
                    break
                elif salir.lower() == "n":
                    return

        except ValueError:
            print('[ERROR]: Valores no válidos, ingrese nuevamente los datos.\n')

# * Funcion eliminar
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
                guardarJSON()
                print("Estudiante eliminado correctamente.")
            else:
                print(" Operación cancelada.")
            break

    if not encontrado:
        print("No existe un estudiante con ese ID.")

# * Funcion Actualizar
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

            # Nuevos datos
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            grado = int(input("Ingrese el nuevo grado: "))

            est["nombre"] = nombre
            est["apellido"] = apellido
            est["grado"] = grado

            print("\nEstudiante actualizado correctamente:")
            print(est)
            guardarJSON()
            break

    if not encontrado:
        print("[ERROR]: No existe un estudiante con ese ID.")


# * Funcion mostrar valores
def leer(estudiantes):
    if not estudiantes:
        print("No hay información")
    else:
        print("\n----- Lista de estudiantes -----")
        for est in estudiantes:
            print(f"id: {est['id']}, nombre: {est['nombre']}, apellido: {est['apellido']}, grado: {est['grado']}")
        print("--------------------------------\n")

# ! -------- Funcion Menu ---------------!
def menu():
    while True:
        try:
            opcion = int(input(f'!------------------ Menu Principal ------------------!\n1.Crear estudiante\n2.Eliminar estudiante\n3.Actualizar estudiante\n4.Mostrar estudiantes\n5.Exportar a csv\n6.Salir\nOpcion: '))

            if(opcion == 1):
                crearEstudiante()
            elif(opcion == 2):
                eliminar(total_estudiantes)
            elif(opcion == 3):
                actualizar(total_estudiantes)
            elif(opcion == 4):
                leer(total_estudiantes)
            elif(opcion == 5):
                exportarCSV()
                guardarJSON()
            elif opcion == 6:
                print()
                for tiempo in range(3, 0, -1):
                    print(f"Cerrando el programa en: {tiempo}...")
                    time.sleep(1)
                print("[AVISO]: El programa se cerró.")
                break
            else:
                print("[ERROR]: Seleccione una opción válida del (1 al 5).")
        except ValueError:
            print('Mensaje de error')
            continue

print(total_estudiantes)
total_estudiantes = cargarJSON()
menu()