def operacion(n,m):
    division = int(n / m)
    resto = n - (division*m)
    return f"La división de {n} entre {m} da un cociente {division} y un resto {resto}, donde {n} y {m} son los números introducidos por el usuario, y {division} y {resto} son el cociente y el resto de la división entera respectivamente"

if __name__ =="__main__":
    n = int(input("Dime el primer número: "))
    m = int(input("Dime el segundo número: "))
    print(operacion())