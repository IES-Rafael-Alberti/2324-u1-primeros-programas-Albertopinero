from src.ejercicio12 import masa

def test_masa():
    peso = 80
    estatura = 1.80
    assert masa(peso,estatura) == "Tu índice de masa corporal es 24.69"