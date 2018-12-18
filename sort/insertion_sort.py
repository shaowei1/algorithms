# T(n) = O(n^2)
# S(n) = O(1)


def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i

        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


l = list(range(10, 0, -1))
insertion_sort(l)
print(l)
