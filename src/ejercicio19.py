def nombre(name):
    mayus = name.upper()
    longitud = len(name)
    return f"{mayus} tiene {longitud} letras"

if __name__ =="__main__":
    name = input("¿Cómo te llamas?: ")
    print(nombre(name))