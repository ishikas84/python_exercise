from itertools import product
from typing import List

class Solution:
    def __init__(self):
        self.digit_map = {
                          "2":["a", "b", "c"],
                          "3":["d", "e", "f"],
                          "4":["g", "h", "i"],
                          "5":["j", "k", "l"],
                          "6":["m", "n", "o"],
                          "7":["p", "q", "r", "s"],
                          "8":["t", "u", "v"], 
                          "9":["w", "x", "y", "z"]}

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return self.digit_map[digits]
        else:
            char_list = []
            for key in digits:
                char_list.append(self.digit_map[key])
            charlist = product(*char_list)
            print(charlist)
            result = ["".join(chars) for chars in charlist]
            return result

a = Solution()

digits = "23"

hoge = a.letterCombinations(digits)
print(hoge)