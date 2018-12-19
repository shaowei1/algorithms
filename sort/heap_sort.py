def max_heapify(arr,i):
    l_child = i*2
    r_child = i*2+1
    print(arr[l_child],arr[r_child])
    if l_child <= len(arr) and arr[l_child] > arr[i]:
        max = l_child
    else:
        max = i
    if r_child <= len(arr) and arr[r_child] > arr[max]:
        max = r_child
    print(max,i)
    if max != i:
        arr[i],arr[max] = arr[max],arr[i]
        print(arr,max)
        max_heapify(arr,max)

a = [16,4,10,14,7,9,3,2,8,1]
max_heapify(a,1)
print(a)
