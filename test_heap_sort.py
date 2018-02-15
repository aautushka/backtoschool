import pytest

# given:
# 1 9 2 8 3 7 4 6 5
#
# heapify:
# 1 9 [2] 8 3 [7] 4 6 5
# [1] [9] 7 8 3 2 4 6 5 
# 9 [1] 7 [8] 3 2 4 6 5
# 9 8 7 [1] 3 2 4 [6] 5 
# 9 8 7 6 3 2 4 1 5
#
# sort:
# 9 8 7 6 3 2 4 1 5
# 5 8 7 6 4 2 4 1 [9] swap
# 8 5 7 6 3 2 4 1 [9] heapify
# 8 6 7 5 3 2 4 1 [9] heapify
# 1 6 7 5 3 2 4 [8 9] swap 
# 7 6 1 5 3 2 4 [8 9] heapify
# 7 6 4 5 3 2 1 [8 9] heapify
# 1 6 4 5 3 2 [7 8 9] swap
# 6 1 4 5 3 2 [7 8 9] heapify
# 6 5 4 1 3 2 [7 8 9] heapify
# 2 5 4 1 3 [6 7 8 9] swap 
# 5 2 4 1 3 [6 7 8 9] heapify
# 5 3 4 1 2 [6 7 8 9] heapify
# 2 3 4 1 [5 6 7 8 9] swap
# 4 3 2 1 [5 6 7 8 9] heapify
# 1 3 2 [4 5 6 7 8 9] swap
# 3 1 2 [4 5 6 7 8 9] heapify
# 2 1 [3 4 5 6 7 8 9] swap
# 1 [2 3 4 5 6 7 8 9] swap
# [1 2 3 4 5 6 7 8 9] swap
# 
# complexity: O(n * lg(n))

def left(root):
    return root * 2 + 1

def right(root):
    return root * 2 + 2

def nearest_pow_of_two(num):
    # works only for int32
    num = num | (num >> 1)
    num = num | (num >> 2)
    num = num | (num >> 4)
    num = num | (num >> 8)
    num = num | (num >> 16)
    return (num + 1) >> 1

def leaves(arr_size):
    return nearest_pow_of_two(arr_size) - 1

def heapify(arr, root, depth):
    l = left(root)
    r = right(root)
    largest = root

    if l < depth and arr[l] > arr[largest]:
        largest = l

    if r < depth and arr[r] > arr[largest]:
        largest = r

    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        return heapify(arr, largest, depth)

    return arr

def heap_sort(arr):
    non_leaf = leaves(len(arr) - 1)
    for i in xrange(non_leaf, -1, -1):
        heapify(arr, i, len(arr))
    
    for i in xrange(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr

def heapify_all(arr):
    return heapify(arr, 0, len(arr))

def test_find_leaves():
    assert 0 == leaves(1)

    assert 1 == leaves(2)
    assert 1 == leaves(3)

    assert 3 == leaves(4)
    assert 3 == leaves(5)
    assert 3 == leaves(6)
    assert 3 == leaves(7)

def test_heapify_one():
    assert [1] == heapify_all([1])

def test_heapify_two():
    assert [2, 1] == heapify_all([2, 1])
    assert [2, 1] == heapify_all([1, 2])

def test_heapify_three():
    assert [3, 2, 1] == heapify_all([3, 2, 1])
    assert [3, 1, 2] == heapify_all([3, 1, 2])
    assert [3, 1, 2] == heapify_all([2, 1, 3])
    assert [3, 2, 1] == heapify_all([2, 3, 1])
    assert [3, 2, 1] == heapify_all([1, 2, 3])
    assert [3, 1, 2] == heapify_all([1, 3, 2])

def test_heapify_four():
    assert [4, 3, 2, 1] == heapify_all([4, 3, 2, 1])
    assert [3, 2, 1, 4] == heapify_all([1, 2, 3, 4])

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
