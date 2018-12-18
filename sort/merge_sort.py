# T(n) = O(nlogn)
# S(n) = O(n)

def merge(left, right):
    l = 0
    r = 0
    result = []
    while True:
        if l == len(left):
            result += right[r:]
            break
        if r == len(right):
            result += left[l:]
            break

        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    return result


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        mid = int(len(a) / 2)
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])
        return merge(left, right)


a = [2, 4, 6, 8, 9, 1, 3, 5, 7, 10, 11, 12, 13]
print(merge_sort(a))
