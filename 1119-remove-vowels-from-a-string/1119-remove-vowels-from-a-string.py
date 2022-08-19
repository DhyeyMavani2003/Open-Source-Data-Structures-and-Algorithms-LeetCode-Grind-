class Solution:
    def removeVowels(self, s: str) -> str:
        res = ""
        vowels = ["a", "e", "i", "o", "u"]
        for char in s:
            if char not in vowels:
                res += char
        return res