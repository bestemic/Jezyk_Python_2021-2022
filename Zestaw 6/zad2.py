S=list(input())

lower=[]
upper=[]
even=[]
odd=[]

for i in S:
    if i.isalpha():
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    else:
        if int(i)%2 == 0:
            even.append(i)
        else:
            odd.append(i)

upper.sort()
lower.sort()
even.sort()
odd.sort()

wynik = [lower, upper, odd, even]

for j in wynik:
    for i in j:
        print(i, end="")