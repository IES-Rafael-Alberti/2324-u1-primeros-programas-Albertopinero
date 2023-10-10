from src.ejercicio14 import productos

def test_ejercicio14():
    payasos = 50
    muñecas = 35
    assert productos(payasos,muñecas) == "El peso total del paquete es de 8225 kg"