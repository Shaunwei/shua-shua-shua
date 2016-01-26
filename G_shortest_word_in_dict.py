"""
given a list of 100 strings and a dictionary of 1M words, for each input string, find the shortest word in the dictionary that contains all letters in the string.
"""
##
# Trie Solution
import collections
class Trie:
    class TrieRoot:
        def __init__(self):
            self.children = {}
            self.shortest_word = None
    class TrieNode:
        def __init__(self, char=''):
            self.char = char
            self.cnts = {}

    def __init__(self, dictionary):
        self.root = Trie.TrieRoot()
        for word in dictionary:
            self.add(word)

    def add(self, word):
        letters = self.get_letters(word)
        root = self.root

        for char, cnt in letters:
            if char not in root.children:
                root.children[char] = Trie.TrieNode(char)
            node = root.children[char]
            if cnt not in node.cnts:
                node.cnts[cnt] = Trie.TrieRoot()
            root = node.cnts[cnt]
            if not root.shortest_word or len(root.shortest_word) > len(word):
                root.shortest_word = word

    def get_letters(self, word):
        counter = collections.defaultdict(int)
        for char in word:
            counter[char] += 1
        return sorted(counter.items())

    def search(self, word):
        letters = self.get_letters(word)
        ret = []
        self.search_rec(self.root, letters, ret)
        return ret

    def search_rec(self, root, letters, ret):
        if not letters:
            ret.append(root.shortest_word)
            return
        char, cnt = letters[0]
        if char in root.children:
            node = root.children[char]
            for mcnt, mroot in sorted(node.cnts.items()):
                if cnt <= mcnt:
                    self.search_rec(mroot, letters[1:], ret)

class Solution:
    def find_shortest_words(self, strings, dictionary):
        ret = []
        trie = Trie(dictionary)
        for s in strings:
            ret.append(self.find_shortest_word(trie, s))
        return ret

    def find_shortest_word(self, trie, s):
        word = '*' * 1000
        for mword in trie.search(s):
            if len(mword) < len(word):
                word = mword
        return word


##
# Inveted Index Solution
class Solution0:
    def find_shortest_words(self, strings, dictionary):
        inveted_index = self.build(dictionary)

        ret = []
        for string in strings:
            words = set()
            for s in set(string):
                words |= inveted_index[s]
            for word in sorted(words, key=len):
                if self.valid(word, string):
                    ret.append(word)
                    break
        return ret

    def build(self, dictionary):
        index = collections.defaultdict(set)
        for word in dictionary:
            for char in set(word):
                index[char].add(word)
        return index

    def valid(self, word, s):
        wcnt = collections.Counter(word)
        scnt = collections.Counter(s)
        for s, cnt in scnt.items():
            if s not in wcnt or wcnt[s] < cnt:
                return False
        return True



if __name__ == '__main__':
    strings = ['abbc', 'ab']
    dictionary = ['afklj', 'cbaa', 'cabb', 'cbaab','bbbbcca','jba']
    print(Solution0().find_shortest_words(strings, dictionary))
