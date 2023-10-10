def producto(precio):
    return f"{precio[:precio.find('.')] + ' euros y ' + precio[precio.find('.')+1:] + ' céntimos.'}"

if __name__ =="__main__":
    precio = input("Introduce el precio del producto con dos decimales: ")
    print(producto(precio))