"""Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means
 it can represent any one letter."""
import collections

# TODO: Failing tests

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.word_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        word_list = self.word_dict[len(word)]
        if word_list is None:
            return False
        trigger = True
        for i, v in enumerate(word_list):
            for j, w in enumerate(v):
                if word[j] == w or word[j] == '.':
                    continue
                else:
                    trigger = False
                    break
            if trigger:
                return True
        return False

if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord('bad')
    print(wordDictionary.search('.ad'))