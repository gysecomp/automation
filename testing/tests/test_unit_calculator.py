from src.calculator import suma, resta, division, division2


def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(10, 3) == 7

def test_division_valida():
    assert division(10, 2) == 5

def test_division_valida2():
    assert division2(10, 2) == 5





