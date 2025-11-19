import json


id_estudiante = 1
nombre = "brayhan"
apellido = "barrera"
grado = 11

estudientes = {
    'id' : id_estudiante,
    'nombre' : nombre,
    'apellido' : apellido,
    'grado' : grado,
}
def leer(estudiantes):
        if not estudiantes:
            print("no hay información")
        else:
            print(f"id: {estudiantes['id']}, nombre: {estudiantes['nombre']}, apellido: {estudiantes['apellido']}, grado: {estudiantes['grado']}")
        
leer(estudientes)
