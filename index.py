import time

total_estudiantes = []

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

            grado = int(input('Ingrese el grado del estudiante: '))

            estudiante = {
                'id': id,
                'nombre': nombre,
                'apellido': apellido,
                'grado': grado
            }

            total_estudiantes.append(estudiante)
            print("\nEstudiante agregado:", estudiante)

            salir = input('Desea agregar otro estudiante? (s/n): ')
            if salir.lower() == 'n':
                print(f'\nTotal de estudiantes: {total_estudiantes}')
                break

        except ValueError:
            print('[ERROR]: Valores no válidos, ingrese nuevamente los datos.\n')


def menu():
    while True:
        try:
            opcion = int(input(f'!------------------ Menu Principal ------------------!\n1.Crear estudiante\n2.Eliminar estudiante\n3.Actualizar estudiante\n4.Mostrar estudiantes\n5.Salir\nOpcion: '))

            if(opcion == 1):
                crearEstudiante()
            elif(opcion == 2):
                print('Eliminar estudiante')
            elif(opcion == 3):
                print('Actualizar estudiante')
            elif(opcion == 4):
                print('Mostrar estudiantes')
            elif opcion == 5:
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

menu()