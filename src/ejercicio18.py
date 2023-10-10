def nombre(name):
    uno = name.lower()
    dos = name.upper()
    tres = name.title()
    return f"{uno}\n{dos}\n{tres}"

if __name__ =="__main__":
    name = input("¿Cómo te llamas? ")
    print(nombre(name))