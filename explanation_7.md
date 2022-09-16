# Problem 7

## HTTPRouter using a Trie

**Explanation for the implementation:**

This problem is very similar to problem 5 for the Trie implementation. Trie is based on some sequence structure, for p5 the sequence is string, and for p7 the sequence is array (in python we use list of strings ).

Implementation details need to be noted:

1. Input url string is converted to list of strings by the split function. And Trie is based on the list of strings.

### Complexity:

- add a url and handler mapping to the Router

Time: O(n), n is the length of the list (url.split('/'))

Space: O(n), n is the length of the list (url.split('/'))

- lookup a url in the Router

Time: O(n), n is the length of the list (url.split('/'))

Space: O(1) no additional space needed
