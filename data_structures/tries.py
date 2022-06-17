class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf_node = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.is_leaf_node = True


    def seach_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.is_leaf_node


    def word_and_all_prefix(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            if not curr.children[letter].is_leaf_node:
                return False
            curr = curr.children[letter]

        return curr.is_leaf_node
