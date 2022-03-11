from multipledispatch import dispatch


class Figura(object):
    def __init__(self):
        print("Figura init")


class Prostokat(Figura):
    x=0
    y=0
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Kwadrat(Prostokat):
    def __init__(self, x):
        super().__init__(x, x)


@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0


@dispatch(Prostokat)
def pole(arg):
    print("Pole: Prostokat")
    return arg.x*arg.y


@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, a, b):
    tmp = Prostokat(a, b)
    return pole(tmp)


@dispatch(Kwadrat)
def pole(arg):
    print("Pole: Kwadrat")
    return arg.x*arg.y

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, a):
    tmp = Kwadrat(a)
    return pole(tmp)



# testy
a, b, c = Figura(), Prostokat(2, 4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i))  # polymorphism at runtime


polaPowierzchni([a, b, c])
