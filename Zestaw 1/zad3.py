while True:
    x = input("Podaj liczbę: ")
    if(x == "stop"):
        break
    try:
        x = float(x)
        print(x, pow(x, 3))
    except:
        print("Niepoprawne dane")
