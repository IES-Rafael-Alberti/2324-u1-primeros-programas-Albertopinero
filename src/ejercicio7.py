def sumar(uno,dos,tres):
    total = uno + dos + tres
    return f"La suma de estos números es {total}"

if __name__ =="__main__":
    uno = int(input("Dime el primer número: "))
    dos = int(input("Dime el segundo número: "))
    tres = int(input("Dime el tercer número: "))
    print(sumar(uno,dos,tres))