from src.ejercicio27 import compra

def test_compra():
    producto = 'mantequilla'
    precio = 6
    unidades = 50
    assert compra(producto,precio,unidades) == 'mantequilla:  50 unidades x      6.00€ =      300.00€'