def correo(email):
    return f"{email[:email.find('@')] + '@ceu.es'}"

if __name__ =="__main__":
    email = input("Introduce tu correo electrónico: ")
    print(correo(email))
