def partition(a, start, end):
    i = start
    for j in range(start, end):
        if a[j] <= a[end]:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    return i


def quick_sort(array, start, end):
    if start < end:
        x = partition(array, start, end)
        # print(x)
        quick_sort(array, start, x - 1)
        quick_sort(array, x + 1, end)


def quick_sort1(array):
    if len(array) < 2:
        return array
    base = array[0]
    less = []
    greater = []
    eq = []
    for i in array:
        if i < base:
            less.append(i)
        elif i > base:
            greater.append(i)
        else:
            eq.append(i)

    return quick_sort1(less) + eq + quick_sort1(greater)


a = [2, 8, 7, 1, 3, 5, 6, 4]
# quick_sort(a, 0, len(a) - 1)
print(quick_sort1(a))
