def medidas(ancho,alto):
    primero = ancho / 2
    segundo = ancho // 2
    tercero = alto / 3
    cuarto = 1 + 2 * 3
    return f"1-{primero} 2-{segundo} 3-{tercero} 4-{cuarto}"

if __name__ =="__main__":
    ancho = 17
    alto = 12
    print(medidas(ancho,alto))