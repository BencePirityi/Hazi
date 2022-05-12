def osszeg():
    osszeg = sum(szamok)
    return osszeg

def atlag():
    atlag = sum(szamok) / len(szamok)
    return atlag

def paros_paratlan():
    paros = []
    paratlan = []
    for elem in szamok:
        if elem % 2 == 0:
            paros.append(elem)
        else:
            paratlan.append(elem)

    return paros, paratlan

szamok = []

while True:
    szam = input("Egész számokat kérek, kilépés 0-val: ")

    try:
        szam = int(szam)
        if szam == 0:
            break
        else:
            szamok.append(szam)
    except:
        print("\n[Hiba] Csak számokat lehet megadni!\n")

print("A számok összege:", osszeg())
print("A számok átlaga:", atlag())

paros = paros_paratlan()[0]
paratlan = paros_paratlan()[1]

print("\nLegkisebb páros szám:", min(paros))
print("Legnagyobb páros szám:", max(paros))
print("Páros számok:", len(paros), "db")
print("Páros számok növekvő sorrendbe:", sorted(paros))

print("\nLegkisebb páratlan szám:", min(paratlan))
print("Legnagyobb páratlan szám:", max(paratlan))
print("Páratlan számok:", len(paratlan), "db")
print("Páratlan számok:", paratlan)