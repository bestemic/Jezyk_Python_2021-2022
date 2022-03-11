from math import pi
from abc import ABC, abstractmethod

# podpunkt A)
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo,
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print(f'wykonanie foo({self}, {x})')

    @classmethod
    def class_foo(cls, x):
        print(f'class_foo({cls}, {x})')

    @staticmethod
    def static_foo(x):
        print(f'wykonanie static_foo({x})')


a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

print('\n----------------\n')

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu


class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass


class Prostokat(Figura):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pole(self):
        return self.x*self.y


class Kolo(Figura):
    def __init__(self, r):
        self.r = r

    def pole(self):
        return pi*(self.r**2)


p = Prostokat(5, 7)
print(p.pole())

k = Kolo(3)
print(k.pole())


print('\n----------------\n')

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu


class Bank:
    def __init__(self):
        print("Otwarto bank")
        self._money = 0

    @property
    def money(self):
        print("Stan konta... ", end="")
        return self._money

    @money.setter
    def money(self, money):
        if(money > 0):
            print("Wplacam pieniadze... ", money)
            self._money += money
        else:
            if(self._money > abs(money)):
                print("Wyplacam pieniadze... ", abs(money))
                self._money += money
            else:
                print("Za malo na koncie")


pko = Bank()
print(pko.money)
pko.money = 125
print(pko.money)
pko.money = 25
print(pko.money)
pko.money = -50
print(pko.money)
pko.money = -101
print(pko.money)
