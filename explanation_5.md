# Problem 5

## Autocomplete with Tries

**Explanation for the implementation:**

Trie is a special tree.

Each trie node could have multiple children, and each child itself is a trie node ( which is the root of a trie ). And we're using a value to tag each child, so for children of a trie node we need a key-value pair data structure, and thus we use dict.

### Complexity:

- TrieNoe class

1. suffixes

time: O(n\*l)

space: O(n\*l)

n is the number of words stored in the tree, l is the average length of the words.

- Trie class

1. insert

time: O(l), l is the length of the word

space: O(l), new nodes are created in the tree, l is the length of the word

2. find

time: O(l), l is length of the word

space: O(1)
