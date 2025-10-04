from src.calculator import division, division2

def test_regresion_division():
    casos = [(10, 2), (9, 3), (5, 2)]
    for a, b in casos:
        resultado_original = division(a, b)
        resultado_nueva = division2(a, b)
        assert resultado_original == resultado_nueva, (
            f"Regressión detectada: {a}/{b} cambió de "
            f"{resultado_original} a {resultado_nueva}"
        )