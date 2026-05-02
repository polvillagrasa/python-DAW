
def llegir_enter(minim, maxim, text):
	n = 0
	while n < minim or n > maxim:
		try:
			n = int(input(text))
		except:
			print(text)

	return n


def crear_llista(n):
	pesos = [0.0]*n

	for i in range(n):
		valor = 0
		while valor < 0.5 or valor > 40.0:
			try:
				valor = int(input("Introdueix el valor"))
			except:
				print("Has d'introduir un valor enter entre 0.5 i 40.0")
		pesos[i] = valor

	return pesos

def trobar_minim(pesos):
	minim = 100
	for p in pesos:
		if p < minim:
			minim = p
	return minim

def trobar_maxim(pesos):
	maxim = -1
	for p in pesos:
		if p > maxim:
			maxim = p
	return maxim


def calcular_mitjana(pesos):
	mitjana = 0
	for p in pesos:
		mitjana+=p

	mitjana = mitjana/len(pesos)

	return mitjana

def per_sobre_mitjana(pesos, mitjana):
	num = 0
	for p in pesos:
		if p > mitjana:
			num+=1

	return num

def trobar_posicio_maxim(maxim,pesos):
	for i in range(len(pesos)):
		if pesos[i] == maxim:
			return i

	return -1

def trobar_incidencies(pesos):
	while n < 5 or n > 40:
		try:
			n = int(input("Introdueix el llindar (entre 10 i 25)"))
		except:
			print("Has d'introduir un valor enter entre 10 i 25.")

	return n

def trobar_incidencies(llindar, pesos):
	posicions = []
	for i in range(len(pesos)):
		if pesos[i] > llindar:
			posicions.append(i)

	return posicions

def trobar_duplicats(pesos):
	duplicats = []
	for i in range(len(pesos)):
		for j in range(i+1, len(pesos)):
			if pesos[i] == pesos[j]:
				duplicats.append(pesos[i])

	return duplicats

def trobar_posicions(valors, pesos):
	for i in range(len(valors)):
		posicions = []
		for j in range(len(pesos)):
			if valors[i]==pesos[j]:
				posicions.append(j+1)
		print(f"El valor {valors[i]} està repetit a les posicions {posicions}")

def main():

	num = llegir_enter(10,25,"Introdueix el valor dels pesos (entre 10 i 25)")
	pesos = crear_llista(num)
	print(pesos)
	minim = trobar_minim(pesos)
	print(f"El mínim és {minim}")
	maxim = trobar_maxim(pesos)
	print(f"El màxim és {maxim}")
	mitjana = calcular_mitjana(pesos)
	print(f"La mitjana és {mitjana}")
	paquets_sobre_mitjana = per_sobre_mitjana(pesos, mitjana)
	print(f"Hi ha {paquets_sobre_mitjana}paquets per sobre de la mitjana.")
	pos_maxim = trobar_posicio_maxim(maxim, pesos)
	llindar = llegir_enter(5,40, "Introdueix el valor del llindar (entre 5 i 40).")
	incidencies = trobar_incidencies(llindar, pesos)
	print(f"Hi ha incidencies a les posicions {incidencies}")
	duplicats = trobar_duplicats(pesos)
	trobar_posicions(duplicats, pesos)

if __name__ == '__main__':
	main()