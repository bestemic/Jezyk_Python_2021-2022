x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
z = int(input("Podaj z: "))
n = int(input("Podaj n: "))

if(x < 0 or y < 0 or z < 0 or n < 0):
    print("Podano niepoprawne dane")
    exit()

wynik = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if(i+j+k != n):
                wynik.append([i, j, k])

print(wynik)
