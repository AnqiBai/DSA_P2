# Problem 2

## Search in a rotated sorted array

**Requirements:**

1. Given a sorted array which is rotated at some random pivot point;
2. Given a target value to search. If found in the array return its index, otherwise return -1;
3. Assumption: the array has no duplicates;
4. The implementation's time complexity should be O(log(n));

**Explanation for the implementation:**

This is a typical binary search problem (looking for a target value in a sorted array), so we can use binary search to achieve O(log(n)) time complexity.

The only variation is the rotation. We can treat this rotation as some kind of change of the coordinate system. So in order to solve the problem, we can just perform classic binary search with a helper function (**getShiftedEle** in the implementation) to map between the rotated array and the logical/virtual sorted original array. This is also the reason why we need to calculate the shift/pivot first in the algorithm.

## Costs

time: O(log(n)) n is the length of the list
space: O(1) no additional data structure is used, no recursion
