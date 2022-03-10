w = int(input("Szerokość: "))
h = int(input("Wysokość: "))

wynik = ""

for i in range(h * 2 + 1):
    linia = ""
    for j in range(w * 4 + 1):
        if i % 2 == 0:
            if j % 4 == 0:
                linia += '+'
            else:
                linia += '-'
        else:
            if j % 4 == 0:
                linia += '|'
            else:
                linia += ' '
    wynik = wynik + '\n' + linia
print(wynik)
