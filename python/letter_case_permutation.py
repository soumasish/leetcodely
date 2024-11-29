from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        results = []
        def backtrack(i, sub):
            if i == n:
                results.append(sub)
                return
            curr = s[i].lower()
            backtrack(i+1, sub + curr)
            if curr.isalpha():
                backtrack(i+1, sub + curr.upper())

        backtrack(0, "")
        return results