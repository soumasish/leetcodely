import collections


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.complete = False

    def add(self, word):
        if not word:
            self.complete = True
        self.children[word[0]].add(word[1:])

    def check_word(self, word):
        if not word:
            return self.complete
        else:
            if word[0] in self.children:
                return self.children.check_word(word[1:])
            else:
                return False

    def check_prefix(self, word):
        if not word:
            return True
        else:
            if word[0] in self.children:
                return self.children.check_prefix(word[1:])
            else:
                return False

    def find_all(self):
        pass





