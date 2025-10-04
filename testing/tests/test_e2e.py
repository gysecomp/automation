import subprocess

def test_app_e2e():

    result = subprocess.run(
        ["python", "app.py"],      
        capture_output=True,
        text=True
    )

    print("\n--- SALIDA DE LA APLICACIÓN ---")
    print(result.stdout)
    print("--------------------------------\n")

    # Verifica que el flujo completo se haya ejecutado correctamente
    assert "Resultado del cálculo: 12" in result.stdout
    assert "Resultado recuperado desde la base de datos: 12" in result.stdout
    assert "Ejecución completada correctamente" in result.stdout
