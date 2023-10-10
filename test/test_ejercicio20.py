from src.ejercicio20 import telefono

def test_telefono():
    tel = "+34-601126714-56"
    assert telefono(tel) == "El número de teléfono es 601126714"