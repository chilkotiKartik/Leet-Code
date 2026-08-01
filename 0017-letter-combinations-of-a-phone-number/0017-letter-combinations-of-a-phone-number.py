from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(index, path):
            if index == len(digits):
                ans.append(path)
                return

            letters = phone[digits[index]]

            for ch in letters:
                backtrack(index + 1, path + ch)

        backtrack(0, "")

        return ans