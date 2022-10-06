# Problem 7

## HTTPRouter using a Trie

**Explanation for the implementation:**

This problem is very similar to problem 5 for the Trie implementation. Trie is based on some sequence structure, for p5 the sequence is string, and for p7 the sequence is array (in python we use list of strings ).

Implementation details need to be noted:

1. Input url string is converted to list of strings by the split function. And Trie is based on the list of strings.

### Complexity:

- RouteTrie Class

1. getRootHandler

   time & space: O(1)

2. getNotFoundHandler

   time & space: O(1)

3. insert

time: O(l)

space: O(l)

l is the number of segments in the url.

4. find

time: O(l)

space: O(1)

l is the number of segments in the url.

- Router Class

1. add_handler

Costs are the same as RouteTrie.insert method.

time: O(l)

space: O(l)

l is the number of segments in the url path.

2. lookup

Costs are the same as RouteTrie.find method.

time: O(l)

space: O(1)

l is the number of segments in the url.

3. split_path

Spliting is done with python's builtin function. Costs are based on python's builtin split function.

n: length of the input string

time: O(n)

space: O(n)
