def demanar_dades():
    usuari = input("Nom d'usuari: ")
    contrasenya = input("Contrasenya: ")
    return usuari, contrasenya

def validar_inici_sessio(usuari, contrasenya):
    if usuari == "admin" and contrasenya == "1234":
        return True
    else:
        return False

def main():
    print("=== Inici de sessió (Script2) ===")
    usuari, contrasenya = demanar_dades()

    if validar_inici_sessio(usuari, contrasenya):
        print(f"Inici de sessió correcte! Benvingut/da {usuari}")
    else:
        print("Nom d'usuari o contrasenya incorrectes.")

if __name__ == "__main__":
    main()
