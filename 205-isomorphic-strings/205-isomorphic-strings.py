class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dictionary = {}
        
        for index, char in enumerate(s):
            
            if char not in dictionary:
                if t[index] in dictionary.values():
                    return False
                else:
                    dictionary[char] = t[index]
                    
            else:
                if dictionary[char] != t[index]:
                    return False
                
        return True