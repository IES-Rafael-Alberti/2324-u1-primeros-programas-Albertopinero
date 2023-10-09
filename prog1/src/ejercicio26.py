def compra(cesta):
    return (cesta.replace(',', '\n'))

if __name__ =="__main__":
    cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
    print(compra(cesta))

