# **Język Python** <br/> **Zestaw 2**
<br>
<div style="text-align: right"><b>Przemysław Pawlik</b></div>

## **1.**
Mamy zagnieżdżoną listę, na przykład: `list1 = [1, 2, [3, 4, [5, 6], 5], 3, 4]`. Dodaj element o kolejnej wartości
w najbardziej zagnieżdżonej liście. W tym przypadku 7 w miejscu `[1, 2, [3, 4, [5, 6, 7], 5], 3, 4]`. Napisz program, który zrobi to uniwersalnie, dla dowolnego zagnieżdżenia, np. dla `[1 [2, 3] 4]` chodzi o `[1 [2, 3, 4] 4]`, dla `[3, 4,[2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]` powinno być `[3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7]`.

----------
<br>

## **2.**
Napisz funkcję, która sprawdzi, czy podany (jako parametr wejściowy – funkcja input) rok, z zakresu 1900 – 100000, jest rokiem przestępnym. 

Za taki rok uważa się rok, który jest podzielny przez 4, ale jeśli jest podzielny przez 100, to nie jest to rok przestępny, chyba że jest dodatkowo podzielny przez 400 – to jest to rok przestępny. 

Np. 1900 to nie jest rok przestępny, ale 2000 jest. Proszę zwracać True / False.

----------
<br>

## **3.**
Dla dowolnego podanego łańcucha znakowego wypisać: - ile jest w nim słów (poprzez słowo rozumiemy ciąg co najmniej jednego znaku innego niż znak przestankowy, https://pl.wikipedia.org/wiki/Interpunkcja), ile liter, oraz wypisać statystykę częstości występowania poszczególnych liter.

----------
<br>

## **4.**
Mamy trzy liczby całkowite, x, y, zreprezentujące wymiary prostopadłościanu, oraz pewną liczbę naturalną n. Wypisz listę wszystkich możliwych współrzędnych (i, j, k) na trójwymiarowej siatce, gdzie i+j+k nie jest równe n. 

> Warunki: 0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z. 

Rozwiązanie zapisz w postaci list składanych (list comprehesion), ale można zacząć od zagnieżdżonych pętli. 

**Przykład** 

Niech x = 1, y = 1, z = 2, n = 3. Lista wszystkich permutacji trójek [i, j, k] w tym przykładzie: `[[0,0,0], [0,0,1], [0 0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]]`. Elementy, które nie sumują się do 3 to: `[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]]`. Parametry x,y,z,n wczytać na początku za pomocą funkcji `input()`.

----------
<br>

## **5.**
Mamy liczbę naturalną N w zapisie binarnym (czyli składa się tylko z 0 i 1). Binarna przerwa to sekwencja zer otoczonych z lewej i prawej strony 1. 

Na przykład liczba 9 (decymalnie) binarnie wynosi 1001 i posiada jedną binarną przerwę długości 2. Liczba 529 ma binarną reprezentację 1000010001, zatem ma dwie binarne przerwy, o długości 4 i 3. Liczba 20 ma reprezentację 10100 zawiera zatem jedną binarną przerwę o długości 1. Liczba 15 ma reprezentację 1111, a zatem żadnej binarnej przerwy. 

Napisz funkcję:
```py
def fun(N)
```

która dla podanej liczby naturalnej N (uwaga: liczby w systemie dziesiętnym) zwraca długość jej najdłuższej
binarnej przerwy, albo 0, jeśli nie ma ani jednej przerwy. 

**Przykład** 

Dla N = 1041, które binarnie jest 10000010001, ma najdłuższą przerwę binarną 5. Należy przyjąć, że argument N może być z przedziału [1..2147483647]. 

>Wskazówka: warto skorzystać z operatora przesunięcia bitowego >> Generalnie można podejrzeć jak wygląda liczba w zapisie binarnym poprzez rzutowanie `bin(N)`.

----------
<br>
