def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

   # binary search in the range [0, number]
    left = 0
    right = number // 2
    while left < (right - 1):
        mid = left + (right - left) // 2
        if mid * mid == number:
            return mid
        elif mid * mid > number:
            right = mid - 1  # discard the mid value here is how the "floored" is done
            # If use right = mid here, we will get rounded square root, e.g. 6 for 35
        else:
            left = mid
    diffleft = number - left * left
    diffright = right ** 2 - number
    result = left if diffleft < diffright else right
    return result


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (5 == sqrt(25)) else "Fail")
print("Pass" if (5 == sqrt(26)) else "Fail")
print("Pass" if (5 == sqrt(35)) else "Fail")
print("Pass" if (6 == sqrt(36)) else "Fail")
print("Pass" if (6 == sqrt(37)) else "Fail")
