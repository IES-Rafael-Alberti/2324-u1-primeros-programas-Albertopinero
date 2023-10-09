from src.ejercicio13 import operacion

def test_operacion():
    n = 11
    m = 5
    assert operacion(n,m) == "La división de 11 entre 5 da un cociente 2 y un resto 1, donde 11 y 5 son los números introducidos por el usuario, y 2 y 1 son el cociente y el resto de la división entera respectivamente"