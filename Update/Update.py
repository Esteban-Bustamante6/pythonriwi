id2 = int(input("id"))

estudiante = {
    'id': id2,
    'nombre': "esteban",
    'apellido': "lose",
    'grado': "12",
}
print(estudiante)

def updateEstudiante ():
    while True:
        id = int(input("digite el id del estudiante que desea modificar : "))

        if id in estudiante :
            print("indice invalido")
            continue
        else :
            if estudiante["id"] == id:
                nombre = input(f" Ponga el nuevo nombre al estudiante {id}")
                apellido = input(f" digite el apellido nuevo")
                grado = int(input("Digite el nuevo grado del estudiante "))
                
                estudianteNuevo = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "grado": grado
                }
                estudiante.update(estudianteNuevo)
                print(estudiante)

                break
            else :
                continue

updateEstudiante()


