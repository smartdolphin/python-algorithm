# 211. Add and Search Word - Data structure design
# https://leetcode.com/problems/add-and-search-word-data-structure-design
import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word)

    def dfs(self, node, word):
        for i, c in enumerate(word):
            if c == '.':
                for child in node.children.values():
                    if self.dfs(child, word[i + 1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.is_word


class TestAddAndSearchWord(unittest.TestCase):
    def test(self):
        # Your WordDictionary object will be instantiated and called as such:
        obj = WordDictionary()
        words = ['bad', 'dad', 'mad']
        for word in words:
            obj.addWord(word)
        search_list = ['pad', 'bad', '.ad', 'b..']
        self.assertEqual(
            [obj.search(search) for search in search_list],
            [False, True, True, True]
        )


if __name__ == '__main__':
    unittest.TestCase()
