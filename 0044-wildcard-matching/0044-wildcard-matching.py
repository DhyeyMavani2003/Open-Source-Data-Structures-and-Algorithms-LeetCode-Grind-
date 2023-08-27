class Solution:        
    def isMatch(self, s: str, p: str) -> bool:
        
        def remove_duplicate_stars(p: str) -> str:
            new_string = []
            for char in p:
                if not new_string or char != '*':
                    new_string.append(char)
                elif new_string[-1] != '*':
                    new_string.append(char)
            return ''.join(new_string)

        def helper(s: str, p: str) -> bool:
            if (s, p) in dp:
                return dp[(s, p)]
            
            if p == s or p == '*':
                dp[(s, p)] = True
            elif p == '' or s == '':
                dp[(s, p)] = False
            elif p[0] == s[0] or p[0] == '?':
                dp[(s, p)] = helper(s[1:], p[1:])
            elif p[0] == '*':
                dp[(s, p)] = helper(s, p[1:]) or helper(s[1:], p)
            else:
                dp[(s, p)] = False
                
            return dp[(s, p)]
        
        dp = {}
        p = remove_duplicate_stars(p)        
        return helper(s, p)
    
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1
        
        while s_idx < s_len:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
    
            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
                              
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern 
            elif star_idx == -1:
                return False
                              
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        
        # The remaining characters in the pattern should all be '*' characters
        return all(p[i] == '*' for i in range(p_idx, p_len))