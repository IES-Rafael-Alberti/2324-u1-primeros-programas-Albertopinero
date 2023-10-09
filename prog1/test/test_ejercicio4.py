from src.ejercicio4 import temperatura

def test_temperatura():
     grados = 7
     assert temperatura(grados) == "La temperatura en Farhenheit es 44.6"