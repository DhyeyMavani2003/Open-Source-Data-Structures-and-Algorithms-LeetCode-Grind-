class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        
        return True
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = {}
        
        # we need to split the s over the space(" ")
        s = s.split(" ")   
        
        # if the lengths of pattern and s are not same then return False
        if len(s) != len(pattern):
            return False
        
        # loop over both pattern and s at same time using the index, as they are of same length
        for i in range(len(s)):
            '''
            if both pattern and s has same characters as shown below
                pattern: 'xyyx'
                s: 'y x x y'
            
            Then using the same keys in hashmap will result in error, so we need to prefix these with some thing 
            Here I am prefixing pattern and s with `pat` and `str` respectively
            '''  
            pv, sv = "pat"+pattern[i] , "str"+s[i]
            
            # add the pattern value and s value if its not in hashmap
            if pv not in hm:
                hm[pv] = i
                
            if sv not in hm:
                hm[sv] = i
            
            # if both are not returning the same index, it means the pattern is not being followed
            if hm[sv] != hm[pv]:
                return False

        return True