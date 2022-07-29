class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = ""
        
        for i in range(len(s)):
            # get the substring with odd length
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > maxLen:
                    res = s[l:r+1]
                    maxLen = curLen
                l -= 1
                r += 1
                
            # get the substring with even length
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > maxLen:
                    res = s[l:r+1]
                    maxLen = curLen
                l -= 1
                r += 1        
        
        return res