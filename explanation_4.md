# Problem 4

## Dutch national flag problem

**Requirements:**

1. Given an input array consisting of only 0, 1 and 2.
2. Need to sort the array in a single traversal.
3. Should not use Python sorting functions.

**Explanation for the implementation:**

The sorting will be done inplace, so there is no requirement/use for additional sapce. In order to solve this problem in a single traversal, we will need to use 3 pointers (refered to as zero, one and two).

(left, right) refers to the range of the array. The three pointers are intialized as:

- zero = left
- one = left
- two = right

For the traversal, we move the zero and one pointers from left to right, and move the two pointer from right to left. In the traversal process, we check the array element the pointer points to, and move the element(s) if necessary.

The three pointers divide the array into the following four parts:

- (left, zero) are 0s
- [zero, one) are 1s
- (two, right) are 2s
- [one, two) is the range for the numbers that have not been traversed (/checked)

So we are using the pointers zero and two as bounderies, and using the pointer one as a cursor and a boundary. For the element on the cursor (pointer one), there could be the following scenarios:

- element is 0:

In this case, this 0 should be moved to the (left, zero) section, so we swap the elements on pointers zero and one, and right move the pointer zero and one;

- element is 1

In this case, this 0 is already in the correct section, so we right move the pointer one;

- element is 2

In this case, this 2 should be moved to the (two, right) section, so we swap the elements on pointers one and two, and left move the pointer two;

Only when the pointer two is on the adjacent left of the pointer one, all elements of the array have been checked, i.e. the traversal is completed.
