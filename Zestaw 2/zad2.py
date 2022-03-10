def isCorrect():
    year = int(input("Podaj rok: "))
    if(year < 1900 or year > 100000):
        print("Zły zakres dat")
        return False
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    return False


print(isCorrect())
