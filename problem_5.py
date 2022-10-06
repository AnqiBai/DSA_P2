import huffman_coding


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        def traverse(nodes, prefix):
            result = []
            for c, node in nodes.items():
                if node.is_word:
                    result.append(prefix + c)
                if node.children:
                    result += traverse(node.children, prefix+c)
            return result
        return traverse(self.children, '')


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root
        for c in word:
            if not current_node.children.get(c):
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return None
            else:
                current_node = current_node.children[c]
        return current_node


# Test Case 1
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod",
    "best"
]
for word in wordList:
    MyTrie.insert(word)


prefix = 'an'
prefixNode = MyTrie.find(prefix)
assert '-'.join(prefixNode.suffixes()) == "t-thology-tagonist-tonym"


# Test Case 2: edge case
Trie_2 = Trie()
wordList = []
for word in wordList:
    MyTrie.insert(word)

prefix = 'an'
prefixNode = Trie_2.find(prefix)
assert prefixNode is None

# Test Case 3: test against a bigger sample data
Trie_3 = Trie()
huffmanCodes = huffman_coding.get_sample_huffman_codes()

for code in huffmanCodes:
    Trie_3.insert(code)
for ele in huffmanCodes:
    prefixNode = Trie_3.find(ele)
    test = '-'.join(prefixNode.suffixes())
    assert test == ''
