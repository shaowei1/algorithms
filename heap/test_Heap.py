from heap.Heap import swap, Heap


def test_swap():
    data = [1, 2, 3]
    swap(data, 0, 2)
    assert data == [3, 2, 1]


def test_math():
    assert 2 / 2 == 1.0


def test_heap():
    given = [33, 17, 21, 16, 13, 15, 9, 5, 6, 7, 8, 1, 2, 22]

    heap = Heap(capacity=len(given))
    for key in given:
        heap.insert(key)
    assert heap.a == [0, 33, 17, 22, 16, 13, 15, 21, 5, 6, 7, 8, 1, 2, 9]
    heap.remove_max()
    assert heap.a == [0, 22, 17, 21, 16, 13, 15, 9, 5, 6, 7, 8, 1, 2, 9]
    heap.show()
    sort_given = [0, 33, 17, 21, 16, 13, 15, 9, 5, 6, 7, 8, 1, 2, 22]
    Heap().sort(sort_given, len(sort_given) - 1)
    assert sort_given == [0, 1, 2, 5, 6, 7, 8, 9, 13, 15, 16, 17, 21, 22, 33]


if __name__ == '__main__':
    test_heap()
