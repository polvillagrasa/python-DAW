nom = input("introdueix el teu nom: ")
cognoms = input("introdeuix els teus cognoms: ")
data_de_naixement = input("introdeueix la teva data de naixement: ")
ciutat = input("introdueix la teva ciutat: ")
codi_postal = int(input("introdeuix el teu codi postal: "))
nom_usuari = input("introdueix el nom d'usuari que el vulguis posar: ")
contrasenya = input("introdeuix la contrasenya que et vulguis posar: ")
estudiant = input("ets estudiant? Si/No: ")
edat = input("cuants anys tens?")
major_edat = input("ets major d'edat? Si/No")

print("el registre s'ha completat correctement")

print("\n comencem amb el inici de sessio: ")
nom_usuari2 = input("introduei el teu nom d'usuari: ")
contrasenya2 = input("introdueix la teva contrasenya: ")
if nom_usuari == nom_usuari2 and contrasenya == contrasenya2:
    print("el inici de sessio ha estat correcte")
else:
    print("inici de sessió incorrecte.")

print("resum de dades")
print(f"Nom complet: {nom} {cognoms} \n edat: {edat} \n major d'edat: {major_edat} \n estudiant: {estudiant} ")
