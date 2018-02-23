import pytest

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

def select(arr, i):
    pivot, a = hoare_partition(arr)
    
    if pivot == i:
        return arr[i]
    elif i < pivot:
        return select(arr[0:pivot], i)
    else:
        return select(arr[pivot + 1:], i - pivot - 1)


def test_select_first_lowest():
    assert 1 == select([1], 0)
    assert 1 == select([2, 1], 0)
    assert 1 == select([3, 2, 1], 0)
    assert 1 == select([4, 3, 2, 1], 0)
    assert 1 == select([5, 4, 3, 2, 1], 0)

def test_select_second_lowest():
    assert 2 == select([2, 1], 1)
    assert 2 == select([3, 2, 1], 1)
    assert 2 == select([4, 3, 2, 1], 1)
    assert 2 == select([5, 4, 3, 2, 1], 1)

def test_third_lowest():
    assert 3 == select([3, 2, 1], 2)
    assert 3 == select([4, 3, 2, 1], 2)
    assert 3 == select([5, 4, 3, 2, 1], 2)

def test_fourth_lowest():
    assert 4 == select([4, 3, 2, 1], 3)
    assert 4 == select([5, 4, 3, 2, 1], 3)

def test_fifth_lowest():
    assert 5 == select([5, 4, 3, 2, 1], 4)
    
    
