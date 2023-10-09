def nombre(name,num):
    return (name + "\n") * num

if __name__ =="__main__":
    name = input("¿Cómo te llamas?: ")
    num = int(input("Introduce un número entero: "))
    print(nombre(name,num))
