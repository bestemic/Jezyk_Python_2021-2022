def fun(N):
    bin = []
    if(N == 0):
        bin.append(0)

    while(N != 0):
        bin.append(N % 2)
        N = int(N/2)

    bin.reverse()
    space = 0
    tmp = 0

    for i in bin:
        if(i == 0):
            tmp += 1
        else:
            space = max(space, tmp)
            tmp = 0

    return space


N = 1547
print(fun(N))
