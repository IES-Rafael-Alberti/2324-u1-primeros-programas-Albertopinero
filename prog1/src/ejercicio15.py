def ahorros(inversion):
    interes = 0.04
    balance1 = inversion * (1 + interes)
    balance2 = balance1 * (1 + interes)
    balance3 = balance2 * (1 + interes)
    return f"Balance tras el primer año:  {round(balance1, 2)} Balance tras el segundo año: {round(balance2, 2)} Balance tras el tercer año: {round(balance3, 2)}"

if __name__ =="__main__":
    inversion = float(input("Introduce la inversión inicial: "))
    print(ahorros(inversion))
    