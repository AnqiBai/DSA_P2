# Problem 1

## Find the square root of an integer

**Requirements:**

1. Should not use any Python library;
2. Should find the floor value of the square root;
3. Time complexity should be O(log(n));

**Explanation for the implementation:**

For the given input number n, the problem is actually the following:

Given a sorted array of integers 0 to n, search for the element that is closest to but smaller than the number sqrt(n).

This is a typical binary search problem, just with the following two variations from the classical binary search:

1. For classical binary search, we compare the searching target with the array element directly; for this problem, we compare n with the square of the array element;

2. Instead of searching for the closest one, for this problem we're searching for the smaller cloest one. e.g. if the input number is 35, the floor value of square root should be 5 (which is expected by the requirement), while the closest integer to the square root is 6.

Implementation details need to be noted:

1. Solution is implemented as binary search, so the time complexity is O(logn).

2. When ( mid \* mid ) > target number n, since we're looking for the floor square root, we know if mid number should be discarded, the new right is changed to (mid - 1). (which is right = mid in classical binary search).

And due to this change, we need to also update the while-loop condition to
**left < (right - 1)**
. Without this change, the **while left <= right** condition and the **mid = left + (right -left) // 2** assignment for mid will together lead to infinite loop when left equals to right.

## Costs

time: O(log(n))
space: O(1) no additional data structure is used, no recursion
