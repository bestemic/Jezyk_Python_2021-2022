def roman2int(liczba):
    wynik = 0

    for i in range(len(liczba)-1):
        if rzym[liczba[i]] >= rzym[liczba[i+1]]:
            wynik += rzym[liczba[i]]
        else:
            wynik -= rzym[liczba[i]]

    wynik += rzym[liczba[-1]]

    return wynik

# różne sposoby
rzym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# rzym = dict(I=1, V=5, X=10, L=50, C=100,D=500, M=1000)

list1 = ["I", "V", "X", "L", "C", "D", "M"]
list2 = [1, 5, 10, 50, 100, 500, 1000]

# rzym = dict()
# for i in range(len(list1)):
#     rzym[list1[i]] = list2[i]

# rzym = dict(zip(list1, list2))

print(roman2int("IX"))  # 9
print(roman2int("XC"))  # 90
print(roman2int("CM"))  # 900
print(roman2int("DCCXXIX"))  # 729