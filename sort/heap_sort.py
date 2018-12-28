# encoding = 'utf-8'
def big_endian(arr, start, end):
    parent = start
    while True:
        child = parent * 2 + 1  # lchild

        if child > end:
            break

        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        if arr[parent] < arr[child]:
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
        else:
            break


def heap_sort(arr):
    # build a max heap
    for start in range(len(arr) // 2 - 1, -1, -1):
        big_endian(arr, start, len(arr) - 1)

    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        big_endian(arr, 0, end - 1)

    return arr


l = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
print(heap_sort(l))
