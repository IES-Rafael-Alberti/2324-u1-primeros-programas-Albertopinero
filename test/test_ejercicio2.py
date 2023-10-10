from src.ejercicio2 import trabajo

def test_trabajo():
    horas = 4
    precio = 10
    assert trabajo(horas, precio) == "El importe total 40 es de euros"