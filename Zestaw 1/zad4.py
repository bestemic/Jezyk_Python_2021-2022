rozmiar = int(input("Podaj długość miarki: "))

linijka = "|"
podpis = "0"
for i in range(1, rozmiar + 1):
    linijka += "....|"
    podpis += str(i).rjust(5)

linijka = linijka + "\n" + podpis

print(linijka)
