from src.database import guardar_resultado, obtener_resultado, db

def test_guardar_resultado_unitario():
    db.clear()  
    guardar_resultado("suma", 15)
    assert "suma" in db
    assert db["suma"] == 15

def test_obtener_resultado_unitario():
    db.clear()
    db["suma"] = 20
    assert obtener_resultado("suma") == 20
    assert obtener_resultado("resta") is None
