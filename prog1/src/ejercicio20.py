def telefono(tel):
    return ('El número de teléfono es ') + tel[4:-3]

if __name__ =="__main__":
    tel = input("Introduce un número de teléfono con el formato +34-xxxxxxxxx-56: ")
    print(telefono(tel))
