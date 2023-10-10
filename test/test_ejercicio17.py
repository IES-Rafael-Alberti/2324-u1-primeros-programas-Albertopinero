from src.ejercicio17 import nombre

def test_nombre():
    name = 'alberto'
    num = 5
    assert nombre(name,num) == "alberto\nalberto\nalberto\nalberto\nalberto\n"