def trabajo(horas,precio):
    salario = horas * precio 
    return f"El importe total {salario} es de euros"

if __name__ =="__main__":
    horas = int(input("Cuántas horas de trabajo:"))
    precio = int(input("¿Cuál es el precio por hora?:"))
    print(trabajo(horas,precio))

