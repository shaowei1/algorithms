# T(n) = O(n^2)
# S(n) = O(1)

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = list(range(10, 0, -1))
bubble_sort(a)
print(a)
