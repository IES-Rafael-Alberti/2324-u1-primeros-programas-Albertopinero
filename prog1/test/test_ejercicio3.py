from src.ejercicio3 import medidas

def test_medidas():
    ancho = 17
    alto = 12
    assert medidas(ancho,alto) == "1-8.5 2-8 3-4.0 4-7"