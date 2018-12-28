def partition(a, start, end):
    x = a[end]
    i = start
    for j in range(start, end - 1):
        if a[j] <= x:
            # i += 1
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i ], a[end] = a[end], a[i ]
    return i


def quick_sort(arr, start, end):
    if start < end:
        x = partition(arr, start, end)
        print(x)
        quick_sort(arr,start,x)
        quick_sort(arr,x,end)


a = [2, 8, 7, 1, 3, 5, 6, 4]
quick_sort(a, 0, len(a) - 1)
print(a)
