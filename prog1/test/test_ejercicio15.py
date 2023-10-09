from src.ejercicio15 import ahorros

def test_ahorros():
    inversion = 45
    assert ahorros(inversion) == "Balance tras el primer año:  46.8 Balance tras el segundo año: 48.67 Balance tras el tercer año: 50.62"