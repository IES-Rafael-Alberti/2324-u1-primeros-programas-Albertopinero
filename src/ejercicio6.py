def producto(precio):
    iva = (10 * precio) / 100
    total = precio + iva
    return f"El precio del producto es {total} €"

if __name__ =="__main__":
    precio = int(input("Escribe el precio del producto: "))
    print(producto(precio))