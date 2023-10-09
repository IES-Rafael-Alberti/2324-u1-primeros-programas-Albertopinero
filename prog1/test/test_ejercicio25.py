from src.ejercicio25 import nacimiento

def test_nacimiento():
    fecha = '25/06/2004'
    assert nacimiento(fecha) == 'Día:25 Mes:06 Año:2004'