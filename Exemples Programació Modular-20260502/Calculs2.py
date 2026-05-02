def demanar_float(text):
    try:
        return float(input(text))
    except ValueError:
        print("Valor no vàlid. Assigno 0.")
        return 0.0

def mitjana(a, b):
    return (a + b) / 2

t1 = demanar_float("Temperatura matí: ")
t2 = demanar_float("Temperatura tarda: ")
print("Mitjana temperatura:", mitjana(t1, t2))

h1 = demanar_float("Humitat matí: ")
h2 = demanar_float("Humitat tarda: ")
print("Mitjana humitat:", mitjana(h1, h2))