"""Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
Note:

    A word cannot be split into two lines.
    The order of words in the sentence must remain unchanged.
    Two consecutive words in a line must be separated by a single space.
    Total words in the sentence won't exceed 100.
    Length of each word is greater than 0 and won't exceed 10.
    1 ≤ rows, cols ≤ 20,000.
"""

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        count, row_count = 0, 0
        while True:
            if row_count < rows:
                curr_len = 0
                for word in sentence:
                    if curr_len + len(word) < cols:
                        curr_len += len(word)
                        curr_len += 1
                    elif curr_len + len(word) > cols:
                        if row_count < rows:
                            row_count += 1
                            curr_len = len(word)
                            curr_len += 1
                        else:
                            return count
                    else:
                        curr_len += len(word)
                count += 1
            else:
                break
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordsTyping(["a", "bcd", "e"], 3, 6))






