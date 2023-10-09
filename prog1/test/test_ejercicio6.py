from src.ejercicio6 import producto

def test_producto():
    precio = 37
    assert producto(precio) == "El precio del producto es 40.7 €"