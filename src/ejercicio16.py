def panaderia(num_panes):
    pan = 3.49
    descuento = 0.6
    coste = num_panes * pan * (1 - descuento)
    return f"El coste de una barra fresca es {pan} €, el descuento sobre una barra no fresca es {descuento * 100} €, el coste final a pagar es {round(coste, 2)} €"

if __name__ =="__main__":
    num_panes = int(input("Introduce el número de barras vendidas que no son frescas: "))
    print(panaderia(num_panes))