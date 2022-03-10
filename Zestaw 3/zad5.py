class Bug:
    licznik = 0

    def __init__(self):
        Bug.licznik += 1
        self.id = Bug.licznik

    def __str__(self):
        return "Licznik: " + str(Bug.licznik) + " ID: " + str(self.id)

    def __del__(self):
        print("Koniec licznik: " + str(Bug.licznik) + " ID: " + str(self.id))
        Bug.licznik -= 1
        del self


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])

print()
