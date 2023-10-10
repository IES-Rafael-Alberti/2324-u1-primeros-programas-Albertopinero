from src.ejercicio24 import producto

def test_producto():
    precio = "17.98"
    assert producto(precio) == "17 euros y 98 céntimos."