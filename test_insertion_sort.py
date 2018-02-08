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

def insertion_sort(arr):
    # iterate forwards starting from element 1
    for i in xrange (1, len(arr)):
        key = arr[i]

        # iterate backwards
        # could it be optimized with SIMD?
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

            
    return arr

def test_one():
    assert [1] == insertion_sort([1])

def test_two():
    assert [1, 2] == insertion_sort([1, 2])
    assert [1, 2] == insertion_sort([2, 1])

def test_three():
    assert [1, 2, 3] == insertion_sort([1, 2, 3])
    assert [1, 2, 3] == insertion_sort([1, 3, 2])
    assert [1, 2, 3] == insertion_sort([2, 1, 3])
    assert [1, 2, 3] == insertion_sort([2, 3, 1])
    assert [1, 2, 3] == insertion_sort([3, 2, 1])
    assert [1, 2, 3] == insertion_sort([3, 1, 2])

def test_n():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == insertion_sort([1, 9, 2, 8, 3, 7, 4, 6, 5])
