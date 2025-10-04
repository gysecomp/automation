def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        raise ValueError("División por cero no permitida")
    return a / b


def division2(a, b):
    if b == 0:
        raise ValueError("División por cero no permitida")
    return round(a / b)