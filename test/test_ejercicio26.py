from src.ejercicio26 import compra

def test_compra():
    cesta = 'manzana,huevos,pan,mantequilla'
    assert compra(cesta) == 'manzana\nhuevos\npan\nmantequilla'