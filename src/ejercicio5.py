def producto(precio,iva):
    iva = (iva * precio) / 100
    total = precio + iva
    return f"El precio del producto es {total} €"

if __name__ =="__main__":
    precio = int(input("Escribe el precio del producto: "))
    iva = int(input("¿Cuánto IVA quieres aplicarle a tu producto?: "))
    print(producto(precio,iva))