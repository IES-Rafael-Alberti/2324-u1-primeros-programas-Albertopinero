from src.ejercicio5 import producto

def test_producto():
    precio = 5
    iva = 17
    assert producto(precio,iva) == "El precio del producto es 5.85 €"