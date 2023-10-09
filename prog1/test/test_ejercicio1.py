from src.ejercicio1 import nombre

def test_nombre():
    name = "alberto"
    assert nombre(name) == "hola alberto"
