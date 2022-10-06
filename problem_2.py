def getShiftedEle(input_list, loc, shift):
    arrLen = len(input_list)
    # 6, 7, 8, 1, 2, 3, 4
    # 4, 5, 6, 0, 1, 2, 3
    # 0, 1, 2, 3, 4, 5, 6
    shiftedLoc = (loc + shift) % arrLen
    return (shiftedLoc, input_list[shiftedLoc])


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not isinstance(input_list, list):
        print("invalid input list: not a list")
        return -1
    if not isinstance(number, int):
        print("invalid input number: not an int")
        return -1
   # look for the shifted/pivot number
    shift = 0
    for idx in range(len(input_list) - 1):
        if input_list[idx] > input_list[idx + 1]:
            shift = idx + 1
            break

    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        (shiftedMid, mid_ele) = getShiftedEle(input_list, mid, shift)
        if mid_ele == number:
            return shiftedMid
        elif mid_ele > number:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# test edge case
test_function([[], 10])
test_function([[10000, *[i for i in range(10000)]], 10000])
test_function([[10000, *[i for i in range(10000)]], 1])
