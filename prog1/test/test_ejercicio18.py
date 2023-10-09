from src.ejercicio18 import nombre

def test_nombre():
    name = 'alberto'
    assert nombre(name) == "alberto\nALBERTO\nAlberto"