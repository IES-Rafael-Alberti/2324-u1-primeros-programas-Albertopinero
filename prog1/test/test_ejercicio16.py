from src.ejercicio16 import panaderia

def test_panaderia():
    num_panes = 37
    assert panaderia(num_panes) == "El coste de una barra fresca es 3.49 €, el descuento sobre una barra no fresca es 60.0 €, el coste final a pagar es 51.65 €"