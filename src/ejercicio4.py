def temperatura(grados):
    formula = (grados * 9 / 5) + 32
    return f"La temperatura en Farhenheit es {formula}"

if __name__ =="__main__":
    grados = int(input("Escribe la temperatura en grados celsius: "))
    print(temperatura(grados))