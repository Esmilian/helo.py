import random

def lanzar_dado():
    print("Simulador de dados")
    print("Lanzando el dado...")
    resultado = random.randint(1, 20)
    print(f"El dado cayó en: {resultado}")

# Llamar a la función para probar
lanzar_dado()