from src.ejercicio23 import correo

def test_correo():
    email = 'aalbertopinerolabrador@gmail.com'
    assert correo(email) == 'aalbertopinerolabrador@ceu.es'