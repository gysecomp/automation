db = {}

def guardar_resultado(operacion, resultado):
    db[operacion] = resultado

def obtener_resultado(operacion):
    return db.get(operacion, None)

