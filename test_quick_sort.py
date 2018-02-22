import pytest

# given:
# 1 9 2 8 3 7 4 6 5
#
# iterations:
# [1 9 2 8 3 7 4 6 5]
# [1 2 3 4][5][9 8 7 6]
# [1 2 3][4][5][6][9 8 7]
# [1 2][3][4][5][6][7][9 8]
# 1 2 3 4 5 6 7 8 9

# worst O(n^2)
# average O(n * lg n)

def hoare_partition(arr):
    i = 0
    j = len(arr) - 1
    pivot = arr[0]

    while True:
        while arr[j] > pivot:
            j -= 1

        while arr[i] < pivot:
            i += 1

        if i != j:
            arr[i],arr[j] = arr[j], arr[i]
        else:
            return (i, arr)

def lomuto_partition(arr):
    pivot = arr[len(arr) - 1]
    q = 0
    j = 0

    while j < len(arr):
        if arr[j] <= pivot:
            j += 1
            q += 1
        else:
            break

    while j < len(arr):
        if arr[j] <= pivot:
            arr[q], arr[j] = arr[j], arr[q]
            q += 1

        j += 1

    return (q - 1, arr)

def partition(arr):
    return lomuto_partition(arr)

def quick_sort(arr):
    pivot, a = partition(arr)

    ret = []
    if pivot > 0:
        ret.extend(quick_sort(arr[0:pivot]))

    ret.append(arr[pivot])

    if pivot < len(arr) - 1:
        ret.extend(quick_sort(arr[pivot + 1:]))

    return ret

def test_partition_one():
    assert (0, [1]) == partition([1])

def test_partition_two():
    assert (1, [1, 2]) == partition([1, 2])
    assert (0, [1, 2]) == partition([2, 1])

def test_partition_three():
    assert (1, [1, 2]) == partition([1, 2])
    assert (0, [1, 2]) == partition([2, 1])

def test_partition_four():
    assert (2, [1, 2, 3]) == partition([1, 2, 3])
    assert (0, [1, 2, 3]) == partition([3, 2, 1])
    assert (1, [1, 2, 3]) == partition([1, 3, 2])
    assert (1, [1, 2, 3]) == partition([3, 1, 2])

def test_partition_n():
    assert (3, [2, 1, 3, 4, 7, 5, 6, 8]) == partition([2, 8, 7, 1, 3, 5, 6, 4])

def test_hoare_partition():
    assert (3, [2, 3, 1, 4, 7, 5, 6, 8]) == hoare_partition([4, 8, 7, 1, 3, 5, 6, 2])

def test_one():
    assert [1] == quick_sort([1])

def test_two():
    assert [1, 2] == quick_sort([1, 2])
    assert [1, 2] == quick_sort([2, 1])

def test_three():
    assert [1, 2, 3] == quick_sort([1, 2, 3])
    assert [1, 2, 3] == quick_sort([1, 3, 2])
    assert [1, 2, 3] == quick_sort([2, 1, 3])
    assert [1, 2, 3] == quick_sort([2, 3, 1])
    assert [1, 2, 3] == quick_sort([3, 2, 1])
    assert [1, 2, 3] == quick_sort([3, 1, 2])

def test_n():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == quick_sort([1, 9, 2, 8, 3, 7, 4, 6, 5])
