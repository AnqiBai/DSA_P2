def swap(array, idx1, idx2):
    tmp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = tmp


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # cornor case
    if input_list is None or len(input_list) == 1:
        return input_list

    # use three pointers
    # zero and one starts from the left
    # two starts from the right
    zero = 0
    one = 0
    two = len(input_list) - 1
    # the 3 pointers divides the array into the following parts:
    # (left, zero) are 0s
    # [zero, one) are 1s
    # (two, right) are 2s
    # [one, two) is the range for the numbers that have not been checked / traversed

    # when one > two, we know that all elements in the array have been checked
    while one <= two:
        if input_list[one] == 0:
            swap(input_list, zero, one)
            zero += 1
            one += 1
        elif input_list[one] == 1:
            one += 1
        else:
            # input_list[one] == 2
            swap(input_list, one, two)
            two -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    # print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# edge case
test_function([])
test_function([2, 1])
test_function([1])
test_function([0])
test_function([2])
test_function([1, 0])
test_function([0, 2])
test_function([2, 1, 0])
test_function([2]*10000 + [0]*10000 + [1]*10000)
