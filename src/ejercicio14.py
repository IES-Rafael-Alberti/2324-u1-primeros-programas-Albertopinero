def productos(payasos,muñecas):
    peso_payaso = 112
    peso_muñeca = 75
    peso_total = peso_payaso * payasos + peso_muñeca * muñecas
    return f"El peso total del paquete es de {peso_total} kg"

if __name__ =="__main__":
    payasos = int(input("Introduce el número de payasos a enviar: "))
    muñecas = int(input("Introduce el número de muñecas a enviar: "))
    print(productos(payasos,muñecas))
