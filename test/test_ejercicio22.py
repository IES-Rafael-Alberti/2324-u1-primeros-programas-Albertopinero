from src.ejercicio22 import palabra

def test_palabra():
    frase = 'hola amigo mio'
    vocal = 'o'
    assert palabra(frase,vocal) == 'hOla amigO miO'