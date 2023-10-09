def palabra(frase):
    return f"{frase[::-1]}"

if __name__ =="__main__":
    frase = input("Introduce una frase: ")
    print(palabra(frase))