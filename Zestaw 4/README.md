# **Język Python** <br/> **Zestaw 4**
<br>
<div style="text-align: right"><b>Przemysław Pawlik</b></div>

## **1.**
Zmodyfikować kod w taki sposób, żeby piłka (ruszała) przyspieszała w kierunku, w którym wciśnięta jest strzałka. Z prostego wzoru na prędkość „w ruchu jednostajnie przyspieszonym” mamy: `𝑣i = 𝑣0𝑖 + 𝑎𝑖 ∙ 𝑡`, gdzie i to składowa (x, y). 

Oczywiście u nas początkowa prędkość może być (0, 0). Przyspieszenie („umownie”) accel ma jakieś wartości, natomiast poprzez t czas rozumieć należy coś takiego, że jeśli dana strzałka jest wciąż wciśnięta, to zwiększamy prędkość (w tym sensie t może
być równe 1, albo dowolnie inaczej). 

Efekt końcowy ma być taki: żeby piłka, początkowo nieruchoma, mogła być wprawiana w ruch i sterowana we wszystkich kierunkach za pomocą strzałek. Proszę poeksperymentować! 

>Uwaga: piłka w zadaniu 1 i 2 powinna się odbijać „doskonale sprężyście” od granic aktywnego ekranu gry.

----------
<br>

## **2.**
Na bazie kodu zrobimy symulację ruchu w polu grawitacyjnym. 

Proszę zatem ustalić jakieś wartości prędkości początkowej piłki, przyspieszenie ma składową pionową (0, 9.81) (składowe
x, y). I teraz, jeśli piłka jest nieruchoma na początku – to będzie to spadek swobodny (z przyspieszeniem g = 9.81 m/s2), jeśli „rzucona w górę” (`vy > 0`), to rzut pionowy, jeśli „rzucona w bok” (`vx > 0`) to rzut poziomy i ogólnie – rzut ukośny. 

Piłka powinna poruszać się realistycznie (w sensie: należy wyliczać jej prędkości według ruchu przyspieszonego w pionie i jednostajnego w poziomie).

----------
<br>

## **3.**
Najpierw należy przestudiować załączony kod (main.py wszystko w jednym pliku), jest to klasyczna gra w ping-ponga, napisana z użyciem znanej nam biblioteki pygame. Proszę po kolei przestudiować kod, który jest komentowany i choć (ewentualnie) zawiera rzeczy nowe, to można się domyślić o co chodzi. 

W szczególności na początku są definicje dwóch klas `Rakietka` i `Pilka`, które zapisane są jako dziedziczące z klasy `pygame.sprite.Sprite` (proszę zobaczyć w kodzie jak to wygląda). Klasy są dość proste, ich metody dbają o zmianę i sprawdzenie położeń granicznych oraz ustalanie (np. losowanie w pewnym zakresie) wartości prędkości piłki. Program zaczyna się od narysowania ekranu, rakietek, piłki (piłka jest o rozmiarze 10x10 punktów), utworzeniu listy widzialnych w grze obiektów (właśnie odziedziczonych z klasy `Sprite`). 

Sama mechanika ruchów rakietek powinna być już znana z poprzednich zadań, ciekawa jest metoda `collide_mask` sprawdzająca czy dane dwa obiekty nie są ze sobą w styczności / kolizji, jeśli tak jest, to na rzecz piłeczki wołamy metodę `bounce()`, która zmienia (i trochę losuje) składową prędkości piłki po odbiciu. 

**Zadanie**: po przestudiowaniu i uruchomieniu kodu Państwa zadanie będzie polegać na takim jego zmodyfikowaniu, żeby: 
* rakietka była tylko jedna, poruszająca się w poziomie na dole ekranu (w lewo i prawo, strzałkami), 
* piłeczka uruchamiana losowo z góry, punkty mają być naliczane za poprawne odbicie od rakietki, 
* gra ma się zakończyć jeśli piłeczka minie rakietkę i zderzy się ze ścianą – wtedy powinien się wyświetlić wynik
końcowy oraz dotychczasowy najwyższy wynik. 

Oczywiście pionowa linia jest teraz zbędna. Innymi słowy – przerobić to na grę „jednoosobową”.

----------
<br>
