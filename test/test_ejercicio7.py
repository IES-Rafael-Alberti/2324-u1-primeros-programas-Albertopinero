from src.ejercicio7 import sumar

def test_sumar():
    uno = 4
    dos = 10
    tres = 15
    assert sumar(uno,dos,tres) == "La suma de estos números es 29"