def nacimiento(fecha):
    return ('Día:' + fecha[:2] + ' Mes:' + fecha[3:5] + ' Año:' + fecha[6:])

if __name__ =="__main__":
    fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
    print(nacimiento(fecha))
