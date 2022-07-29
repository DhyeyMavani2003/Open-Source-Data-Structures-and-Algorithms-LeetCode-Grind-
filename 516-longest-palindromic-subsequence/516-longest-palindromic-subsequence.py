class Solution:
    def longestPalindromeSubseq(self, s: str, lookup={}) -> int:
        if len(s) <= 1:
            return len(s)
        if s not in lookup:
            if s[0] == s[-1]:
                lookup[s] = 2 + self.longestPalindromeSubseq(s[1:-1], lookup)
            else:
                lookup[s] = max(self.longestPalindromeSubseq(s[1:]), self.longestPalindromeSubseq(s[:-1], lookup))
        return lookup[s]