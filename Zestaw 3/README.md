# **Język Python** <br/> **Zestaw 3**
<br>
<div style="text-align: right"><b>Przemysław Pawlik</b></div>

## **1.**
Rekurencyjne liczenie ciągu Fibonacciego jest naturalnym algorytmem, niemniej, wyliczanie każdego kolejnego wyrazu ciągu „od początku” jest niepotrzebne. O wiele wydajniejszą metodą byłoby zastosowanie czegoś w rodzaju buforu – pamięci podręcznej, w której zapamiętywalibyśmy poprzednio (wcześniej) wyliczone wyrazy i z nich korzystali. Znacząco przyspieszy to obliczenia. 

Proszę napisać (uzupełnić poniższy szkielet) kod tak, żeby właśnie powstawał słownik – pamięć podręczna z poprzednimi wyliczonymi wartościami i z nich korzystać, a wyliczać nowe tylko gdy jeszcze nie były policzone wcześniej. Słownik proszę zrobić w dekoratorze.

```py
import functools

def pamiec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # tu powinien być kod tworzący słownik (element - wartość), który jest sprawdzany
        # do obliczeń wyrazów ciągu - które by były wyliczane rekurencyjnie i wpisywane
        # do słownika tylko gdy wcześniej nie były obliczone
        # normalnie bez buforowania by było return func(*args, **kwargs)

    return wrapper

@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

for i in range(100):
    print(fibonacci(i))
```

----------
<br>

## **2.**
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji. 

Przykładowa sekwencja `[[],[4],(1,2),[3,4],(5,6,7)]`, spodziewany wynik `[0,4,3,7,18]`.

----------
<br>

## **3.**
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [`funkcja roman2int()`].

----------
<br>

## **4.**
Napisać funkcję `odwracanie(L, left, right)` odwracającą kolejność elementów na liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

----------
<br>

## **5.**
W ramach zapoznania się z klasami, proszę napisać klasę o nazwie `Bug` taką, żeby zawierała licznik wskazujący aktualną liczbę powołanych do życia obiektów, identyfikator (lokalną zmienną obiektu, do której przypiszemy aktualny powiększony licznik). Licznik powinien rosnąć wraz z wywołaniem `__init__` oraz maleć z wywołaniem `__del__` (uwaga: współdzielony licznik będziemy używać w zapisie `Bug.licznik`). Proszę też zdefiniować `__str__` wypisującą licznik i bieżące id. 

Finalnie, niech dla kodu:

```py
bugs = []

for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
```

wypisują się licznik, identyfikator, a przy niszczeniu obiektu w `__del__` niech będzie też print informacji typu `‘Koniec’`, licznik, identyfikator.

----------
<br>
