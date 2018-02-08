import pytest

# given:
# 1 9 2 8 3 7 4 6 5
#
# iterations:
# 1: [1 9 2 8 3 7 4 6 5]
# 2: [1 9 2 8][3 7 4 6 5]
# 3: [[1 9][2 8]][[3 7][4 6 5]]]
# 4: [[1 9][2 8]][[3 7][[4][6 5]]]]
# 5: [[1 9][2 8]][[3 7][[4][5 6]]]]
# 6: [[[1] [9]][[2] [8]]][[[3] [7]][[4][[5] [6]]]]]
# 7: [[1 9][2 8]][[3 7][4 5 6]]]
# 8: [[1 2 8 9][3 4 5 6 7]]
# 9: [1 2 3 4 5 6 7 8 9]

# worst O(n*ln(n))

def merge(lhs, rhs):
    ret = []
    while True:
        if len(lhs) > 0 and len(rhs) > 0:
            if lhs[0] > rhs[0]:
                ret.append(rhs[0])
                rhs = rhs[1:]
            else:
                ret.append(lhs[0])
                lhs = lhs[1:]
        elif len(lhs) > 0:
            ret += lhs
            break
        else:
            ret += rhs
            break;

    return ret


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    k = len(arr) / 2

    lhs = merge_sort(arr[0:k])
    rhs = merge_sort(arr[k:len(arr)])
    return merge(lhs, rhs)

def test_one():
    assert [1] == merge_sort([1])

def test_two():
    assert [1, 2] == merge_sort([1, 2])
    assert [1, 2] == merge_sort([2, 1])

def test_three():
    # assert [1, 2, 3] == merge_sort([1, 2, 3])
    # assert [1, 2, 3] == merge_sort([1, 3, 2])
    assert [1, 2, 3] == merge_sort([2, 1, 3])
    # assert [1, 2, 3] == merge_sort([2, 3, 1])
    # assert [1, 2, 3] == merge_sort([3, 2, 1])
    # assert [1, 2, 3] == merge_sort([3, 1, 2])

def test_n():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == merge_sort([1, 9, 2, 8, 3, 7, 4, 6, 5])
