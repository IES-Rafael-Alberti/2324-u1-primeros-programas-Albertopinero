def palabra(frase,vocal):
    return f"{frase.replace(vocal, vocal.upper())}"

if __name__ =="__main__":
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal en minúscula:  ")
    if vocal in 'aieou':
        print(palabra(frase,vocal))
    else:
        print("Inténtalo otra vez")
