def odwracanie_iter(L, left, right):
    # Sprawdzenie poprawności miejsc
    if right < left:
        left, right = right, left

    i = 0
    end = (right - left) // 2
    while(i <= end):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
        i += 1

def odwracanie_rek(L, left, right):
    L[left], L[right] = L[right], L[left]
    if left < right:
        odwracanie_rek(L, left + 1, right - 1)



L = [1, 2, 3, 4, 5, 6, 7, 8]
left = 1
right = 5
print(L)

odwracanie_iter(L, left, right)
print(L)

odwracanie_rek(L, left, right)
print(L)
