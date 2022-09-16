# Problem 5

## Autocomplete with Tries

**Explanation for the implementation:**

Trie is a special tree.

Each trie node could have multiple children, and each child itself is a trie node ( which is the root of a trie ). And we're using a value to tag each child, so for children of a trie node we need a key-value pair data structure, and thus we use dict.

### Complexity:

- insert a string to the Trie

Time: O(n), n is the length of the string

Space: O(n), n is the length of the string

- search a string in the Trie

Time: O(n), n is the length of the string

Space: O(1) no additional space needed

- traverse from a root trie node

Time: O(nl), n is the number of the words, l is the average length of the words

Space: O(1) no additional space needed

- create a Trie

Time: O(nl), n is the number of the words, l is the average length of the words

Space: O(nl)
