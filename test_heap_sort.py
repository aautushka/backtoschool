import pytest

# given:
# 1 9 2 8 3 7 4 6 5
#
# iterations:
# 1: [1 9] 2 8 3 7 4 6 5
# 2: [1 2 9] 8 3 7 4 6 4
# 3: [1 2 8 9] 3 7 4 6 5
# 4: [1 2 3 8 9] 7 4 6 5
# 5: [1 2 3 7 8 9] 4 6 5
# 6: [1 2 3 4 7 8 9] 6 5
# 7: [1 2 3 4 6 7 8 9] 5
# 8: [1 2 3 4 5 6 7 8 9]
#
# best O(n)
# worst O(n^2)

def left(root):
    return root * 2 + 1

def right(root):
    return root * 2 + 2

def inplace_heapify(arr, root, depth):
    l = left(root)
    r = right(root)
    largest = root

    if l < depth and arr[l] > arr[largest]:
        largest = l

    if r < depth and arr[r] > arr[largest]:
        largest = r

    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        inplace_heapify(arr, largest, depth)

def heapify(arr, root):
    inplace_heapify(arr, root, len(arr))
    return arr

def test_heapify_one():
    assert [1] == heapify([1], 0)

def test_heapify_two():
    assert [2, 1] == heapify([2, 1], 0)
    assert [2, 1] == heapify([1, 2], 0)

def test_heapify_three():
    assert [3, 2, 1] == heapify([3, 2, 1], 0)
    assert [3, 1, 2] == heapify([3, 1, 2], 0)
    assert [3, 1, 2] == heapify([2, 1, 3], 0)
    assert [3, 2, 1] == heapify([2, 3, 1], 0)
    assert [3, 2, 1] == heapify([1, 2, 3], 0)
    assert [3, 1, 2] == heapify([1, 3, 2], 0)

def test_heapify_four():
    assert [4, 3, 2, 1] == heapify([4, 3, 2, 1], 0)
    assert [3, 2, 1, 4] == heapify([1, 2, 3, 4], 0)

def inplace_heap_sort(arr):
    for i in xrange(len(arr) - 1, -1, -1):
        inplace_heapify(arr, i, len(arr))
    
    print arr
    for i in xrange(len(arr) - 1, -1, -1):
        print "swap"
        arr[0], arr[i] = arr[i], arr[0]
        print arr
        print "heap"
        inplace_heapify(arr, 0, i)
        print arr
        print ""

def heap_sort(arr):
    inplace_heap_sort(arr)
    return arr

def test_one():
    assert [1] == heap_sort([1])

def test_two():
    assert [1, 2] == heap_sort([1, 2])
    assert [1, 2] == heap_sort([2, 1])

def test_three():
    assert [1, 2, 3] == heap_sort([1, 2, 3])
    assert [1, 2, 3] == heap_sort([1, 3, 2])
    assert [1, 2, 3] == heap_sort([2, 1, 3])
    assert [1, 2, 3] == heap_sort([2, 3, 1])
    assert [1, 2, 3] == heap_sort([3, 2, 1])
    assert [1, 2, 3] == heap_sort([3, 1, 2])

def test_four():
    assert [1, 2, 3, 4] == heap_sort([1, 2, 3, 4])
    assert [1, 2, 3, 4] == heap_sort([4, 3, 2, 1])


def test_n():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == heap_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == heap_sort([1, 9, 2, 8, 3, 7, 4, 6, 5])
