"""This class implements a set of methods with different complexities to find if a substring p is present
in a string t."""


class SubStringSearch:

    @staticmethod
    def naive_search(t, p):
        i, j, count, idx, started = 0, 0, 0, -1, False
        while i < len(t) and j < len(p):
            if t[i] == p[j]:
                count += 1
                if not started:
                    started = True
                    idx = i
                else:
                    if count == len(p):
                        return idx
                j += 1
                i += 1
            else:
                if started:
                    started = False
                    count = 0
                    j = 0
                    idx = -1
                else:
                    i += 1
        return -1

    @staticmethod
    def kmp(t, p):
        pass

    @staticmethod
    def rabin_karp(t, p):
        pass

    @staticmethod
    def boyer_moore(t, p):
        pass


if __name__ == '__main__':
    searcher = SubStringSearch()
    print(searcher.naive_search('abcbcglx', 'bcglx'))

