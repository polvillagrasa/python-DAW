from Script2 import demanar_dades, validar_inici_sessio

def programa_principal():
    pass

def main():
    print("=== Inici de sessió (Script3) ===")
    usuari, contrasenya = demanar_dades()

    if validar_inici_sessio(usuari, contrasenya):
        print("Accés concedit! Benvingut/da,", usuari)
        programa_principal()
    else:
        print("Accés denegat. Si us plau, torna-ho a provar.")

if __name__ == "__main__":
    main()
