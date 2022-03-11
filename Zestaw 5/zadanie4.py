from functools import singledispatch, singledispatchmethod
from math import ceil

class Multiply:
    @singledispatchmethod
    def multi(self, arg):
        return "Nieznane przeładowanie"

    @multi.register(list)
    def _(self, arg):
        wynik = 1
        for i in arg:
            wynik *= i
        return wynik

    @multi.register(set)
    def _(self, arg):
        wynik = 1
        for i in arg:
            wynik *= i
        return wynik

    @multi.register(tuple)
    def _(self, arg):
        wynik = 1
        for i in range(len(arg)):
            wynik *= int(arg[i])
        return wynik

    @multi.register(dict)
    def _(self, arg):
        wynik = 1
        for i in arg:
            wynik *= int(i)+arg[i]
        return wynik


multiplier = Multiply()

print(multiplier.multi("napis"))
print(multiplier.multi([1, 2, 3, 4, 5]))
print(multiplier.multi({1, 2, 3, 4})) 
print(multiplier.multi(("2", "10", "5"))) 
print(multiplier.multi({"2": 4, "1": 9, "0": 2}))


print("\n----------------\n")

@singledispatch
def pole(arg):
    return "Nieznane przeładowanie"

@pole.register
def _(a:int, b:int):
    return a*b

@pole.register
def _(a:float, b:float):
    return ceil(a)*ceil(b)

@pole.register
def _(a:tuple):
    return int(a[0])*int(a[1])

print(pole("pies"))
print(pole(12, 10))
print(pole(12.1, 10.0))
print(pole(('5', '3')))