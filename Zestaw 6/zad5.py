from itertools import product

K, M = map(int, input().split())

matrix=[]

for i in range(K):
    x = list(map(int, input().split()))
    matrix.append(x[1:])

matrix = list(product(*matrix))
    
maxs = []
for i in matrix:
    maxs.append(sum(map(lambda x: x**2, i))%M)
    
wynik = max(maxs)

print(wynik)
