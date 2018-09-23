# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree
import unittest


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current_dic = self.dic
        for char in word:
            if char not in current_dic:
                current_dic[char] = {}
            current_dic = current_dic[char]
        current_dic['*'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_dic = self.dic
        for char in word:
            if char not in current_dic:
                return False
            current_dic = current_dic[char]
        if '*' in current_dic:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_dic = self.dic
        for char in prefix:
            if char not in current_dic:
                return False
            current_dic = current_dic[char]
        return True


class TestTrie(unittest.TestCase):
    def test(self):
        # Your Trie object will be instantiated and called as such:
        obj = Trie()
        obj.insert('apple')
        self.assertFalse(obj.search('app'))
        self.assertTrue(obj.startsWith('app'))
        obj.insert('app')
        self.assertTrue(obj.search('app'))
        self.assertTrue(obj.startsWith('app'))
        obj.insert('ap')
        self.assertFalse(obj.search('aps'))
        self.assertTrue(obj.startsWith('a'))


if __name__ == '__main__':
    unittest.TestCase()
