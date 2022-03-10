n = int(input("Podaj nieparzystą liczbe: "))
if(n % 2 == 0):
    print("Liczba była parzysta")
    exit


for i in range(n, 0, -2):
    s = int((n-i)/2)
    print(' '*s+"*"*i)
