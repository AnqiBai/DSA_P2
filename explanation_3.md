# Problem 3

## Rearrange array elements

**Requirements:**

1. Rearrange array elements to form two numbers so that their sum is maximum.
2. All given array elements are in the range [0,9], which means they are valid single digit to form a integer.
3. The number of digits in both the formed numbers cannot differ by more than 1.
4. Should not use python sort functions.
5. Time complexity should be O(nlog(n)).

**Explanation for the implementation:**

Per the requirements, we need to form two numbers using the elements of the given array. Since the number of the digits in both the formed numbers cannot differ by more than 1, the actual question is how to divide the array elemnts into two groups of same number of elements (or one of the group has 1 more element than the other).

So the problem is equivalent to assign array elements to two groups in turn. In order to get maximum sum, we need to assign higher digit number to greater place. So we need to sort the given array first.

The steps would be:

1. Sort the given array;
2. Traverse (loop through) the sorted array, and assign array elements to two groups in turn.
3. If the given array has odd number of elements, assign the last element to any one of the two groups.

For step 1 sorting we can achieve O(nlog(n)) time complexity by quick sort or merge sort. Step 2 traversal will need O(n) time complexity. Step 3 is only a single step of O(1). So the total time complexity of the alogrithm is O(nlog(n)).

Quick sort doesn't require additional space, so we choose quick sort instead of merge sort for this implementation.

For potential improvement, we can implement the quick sort to be sorting descendingly, so that there is no need to reverse the result at line 84. But for current implementation simplicity, we just do traditional ascending order.

## Costs:

time: O(nlog(n)), O(nlog(n)) for sorting the list and O(n) for constructing the two numbers, so O(nlog(n)) in total
space: O(n), quick sort doesn't require additional space since it's done inplace, two lists (of O(n) in total) are used to temporarily to store the formed numbers
