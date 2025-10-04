from src.calculator import suma
from src.database import guardar_resultado, obtener_resultado

def test_integracion_calculo_y_guardado():
    resultado = suma(4, 6)
    guardar_resultado("suma", resultado)
    assert obtener_resultado("suma") == 10
