def operacion(n):
    suma = (n*(n+1)/2)
    return f"El resultado de la operacion es: {suma}"

if __name__ =="__main__":
    n= int(input("Escribe un número: "))
    print(operacion(n))