from src.ejercicio19 import nombre

def test_nombre():
    name = 'alberto'
    assert nombre(name) == "ALBERTO tiene 7 letras"