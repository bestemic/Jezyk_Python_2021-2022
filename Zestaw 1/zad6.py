x = [12, 'c', -1, 'a', 14, "412", 'g', 'g']
y = ['c', 14, -1, 'x', 'a', 'c', 'w', 412]


def a():
    wynik = []
    for i in y:
        if i in x:
            wynik.append(i)
    return wynik


def b():
    wynik = []
    tmp = []
    tmp.extend(x)
    tmp.extend(y)

    for i in tmp:
        if i not in wynik:
            wynik.append(i)
    return wynik


print("a:", a())
print("b:", b())
