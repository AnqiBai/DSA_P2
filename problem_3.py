import random


def swap(array, idx1, idx2):
    tmp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = tmp


def getPivotPos(left, right):
    # should use a random number between left and right
    # if the random module is not allowed, we can just return
    # left or right here, since we can assume the original array
    # is not sorted
    return random.randrange(left, right + 1)


def partition(array, left, right):
    pivotIndex = getPivotPos(left, right)
    pivot = array[pivotIndex]
    # swap the pivot element to the right most position first
    swap(array, pivotIndex, right)

    # use two pointers to traverse the array
    leftBound = left
    rightBount = right - 1
    while leftBound <= rightBount:
        if array[leftBound] < pivot:
            leftBound += 1
        elif array[rightBount] >= pivot:
            rightBount -= 1
        else:
            # array[leftBound] >= pivot and array[rightBound] < pivot
            swap(array, leftBound, rightBount)
            leftBound += 1
            rightBount -= 1
    # here leftBound > rightBound
    # . . . . rB lB . . . . . r
    # all the numbers that are to the left of lB are < pivot
    # move the pivot element back from the right most location
    # to the location it should be;
    swap(array, leftBound, right)
    return leftBound


def quickSort(array, left, right):
    if left >= right:
        return  # the only actual base case if when left == right

    pivotPos = partition(array, left, right)
    quickSort(array, left, pivotPos - 1)
    quickSort(array, pivotPos + 1, right)


def quick_sort(array):
    if not array:
        return array
    quickSort(array, 0, len(array) - 1)
    return array


def is_input_list_valid(array):
    if not isinstance(array, list):
        return "input should be a list"
    elif len(array) < 2:
        return "input list needs to have at lease two elements"
    else:
        for idx, item in enumerate(array):
            if not isinstance(item, int) or item not in range(10):
                return "invalid element of the input list at index " + str(idx)
    return "pass"


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sort the input list
    # python sorting not allowed
    # build two numbers
    check_input = is_input_list_valid(input_list)
    if check_input != "pass":
        print(check_input)
        return []
    quick_sort(input_list)
    n = len(input_list) // 2
    str1 = ""
    str2 = ""
    for i in range(n):
        str1 += str(input_list[2*i])
        str2 += str(input_list[2*i + 1])
    if len(input_list) % 2 != 0:
        str1 += str(input_list[2*i + 2])

    return [int(str1[-1::-1]), int(str2[-1::-1])]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Added test case
test_function([[1], []])
test_function(["test 33333", []])
test_function([[1, 3, 2, 99], []])
test_function([[1, 3, "str", 99], []])
test_function([[9, 9, 9, 9, 1, 1, 1, 1], [9911, 9911]])
test_function([[9, 9, 9, 9, 1, 1, 1, 1, 1], [99111, 9911]])
