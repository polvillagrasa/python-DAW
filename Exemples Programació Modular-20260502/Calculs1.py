try:
    t1 = float(input("Temperatura matí: "))
except ValueError:
    print("Valor no vàlid. Assigno 0.")
    t1 = 0.0

try:
    t2 = float(input("Temperatura tarda: "))
except ValueError:
    print("Valor no vàlid. Assigno 0.")
    t2 = 0.0

print("Mitjana temperatura:", (t1 + t2) / 2)

try:
    h1 = float(input("Humitat matí: "))
except ValueError:
    print("Valor no vàlid. Assigno 0.")
    h1 = 0.0

try:
    h2 = float(input("Humitat tarda: "))
except ValueError:
    print("Valor no vàlid. Assigno 0.")
    h2 = 0.0

print("Mitjana humitat:", (h1 + h2) / 2)


