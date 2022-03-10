import re

napis = input("Podaj łańcuch znakowy: ")
napis = napis.lower()

stat = {}
slowa = 0
litery = 0
przestanki = '''.,:;!?-()[]{}'"<>«»'''

napis = re.sub(r'[^\w\s]', ' ', napis)
napis = re.sub(r"\s+", ' ', napis)

if(napis[0] == " "):
    slowa -= 1
if(napis[-1] != " "):
    slowa += 1

for i in napis:
    if i == ' ':
        slowa += 1
    else:
        litery += 1
        if i in stat:
            stat[i] += 1
        else:
            stat[i] = 1

print("Wyrazów jest:", slowa)
print("Liter jest:", litery)
print("Rozkład:", stat)
