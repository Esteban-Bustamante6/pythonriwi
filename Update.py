id2 = int(input("Ingresa la id del estudiante"))
estudiantes = {
    'id': id2,
    'nombre': "",
    'apellido': "",
    'grado': ""
}
def Update ():
    while True:
        id = int(input("digite el id del estudiante"))

        if id in estudiantes:                    
            print("indice incorrecto")
            continue
        else:
            if estudiantes["id"] == id:
                nombre = str(input("Ingresa el nombre nuevo: "))
                apellido = str(input("Ingresa el apellido nuevo: "))
                grado = int(input("Ingresa el grado nuevo: "))

                estudiantenuevo = {
                    "Nombre": nombre,
                    "Apellido": apellido,
                    "grado": grado
                }

                estudiantes.update(estudiantenuevo)
                print(estudiantes)
                break
            else:
                continue
Update()
