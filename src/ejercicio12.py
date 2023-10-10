def masa(peso,estatura):
    imc = round(float(peso)/float(estatura)**2,2)
    return f"Tu índice de masa corporal es {imc}"

if __name__ =="__main__":
    peso = input("Escribe el peso (kg): ")
    estatura = input("Escibe la estatura (m): ")
    print(masa(peso,estatura))