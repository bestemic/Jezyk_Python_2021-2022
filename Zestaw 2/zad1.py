def search(lista):
    if(any(isinstance(i, list) for i in lista)):
        for i in lista:
            if(isinstance(i, list)):
                i = search(i)
    else:
        x = lista[-1]+1
        return lista.append(x)


list1 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]

search(list1)
print(list1)
