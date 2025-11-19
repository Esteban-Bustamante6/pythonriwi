def borrar(id):
    input("ingrese el id del estudiante")
    estudiante_encontrado = estudiante.query.get(id)
    if not estudiante_encontrado:
        print("Usuario no encontrado")
        return
    try:
        db.session.delete(estudiante_encontrado)
        db.session.commit()
        print("Eliminación realizada con éxito")

    except Exception as e:
        db.session.rollback()
        print("Error al eliminar. Vuelve a intentarlo.")
        print(f"Detalle del error: {e}")

    