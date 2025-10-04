from src.calculator import suma
from src.database import guardar_resultado, obtener_resultado

def ejecutar_flujo():
    print("Iniciando ejecución de la aplicación...\n")

    resultado = suma(5, 7)
    print(f"Resultado del cálculo: {resultado}")


    guardar_resultado("suma_1", resultado)
    recuperado = obtener_resultado("suma_1")

    print(f"Resultado recuperado desde la base de datos: {recuperado}\n")

    print("Ejecución completada correctamente")


if __name__ == "__main__":
    ejecutar_flujo()
