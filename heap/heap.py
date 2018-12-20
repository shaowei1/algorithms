# indexing start from 1

class Heap:
    def __init__(self, l=[]):
        placeholder = 0
        self._heap = [placeholder]
        self._heap.extend(l)

    def __setitem__(self, key, value):
        self._heap[key] = value

    def __getitem__(self, item):
        return self._heap[item]

    def __len__(self):
        return len(self._heap) - 1

    def __repr__(self):
        return str(self._heap[1:])

    def lchild(self, pos):
        return 2 * pos + 1

    def rchild(self, pos):
        return 2 * pos

    def parent(self, pos):
        return pos // 2

    def max_heapify(self, i):
        l = self.lchild(i)
        r = self.rchild(i)

        if l <= self.__len__() and self[l] > self[i]:
            max = l
        else:
            max = i
        if r <= len(self) and self[r] > self[max]:
            max = r
        # print(max, i)
        if max != i:
            self[i], self[max] = self[max], self[i]
            # print(heap, max)
            self.max_heapify(max)

    def build_max_heap(self):
        for i in range(len(self) // 2, 0, -1):
            self.max_heapify(i)

    def heap_sort(self):
        for i in range(len(self) // 2, 0, -1):
            self.max_heapify(i)

        heap_size = len(self)
        for i in range(heap_size, 1, -1):
            self.max_heapify(i)
            self[1], self[i] = self[i], self[1]
            self.max_heapify(i)


if __name__ == '__main__':
    heap = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
    heap.max_heapify(2)
    print(heap)
