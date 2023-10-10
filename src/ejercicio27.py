def compra(producto,precio,unidades):
    return ('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))

if __name__ =="__main__":
    producto = input('Introduce el nombre del producto: ')
    precio = float(input('Introducde el precio unitario: '))
    unidades = int(input('Introduce el número de unidades: '))
    print(compra(producto,precio,unidades))