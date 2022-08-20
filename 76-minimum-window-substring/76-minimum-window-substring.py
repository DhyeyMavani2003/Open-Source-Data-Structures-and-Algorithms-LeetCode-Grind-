class Solution:
    def minWindow(self, s, t):
        if t == "":
            return ""

        target = {}
        for c in t:
            if c in target:
                target[c] += 1
            else:
                target[c] = 1

        left = 0
        current = {}
        have = 0 
        need = len(target)
        res = [-1, -1]
        resLen = float("infinity")

        for right in range(len(s)):
            character = s[right]
            if character in current:
                current[character] += 1
            else:
                current[character] = 1
            if character in target and target[character] == current[character]:
                have += 1
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left,right]
                    resLen = right - left + 1
                current[s[left]] -= 1
                if s[left] in target and current[s[left]] < target[s[left]]:
                    have -= 1
                left += 1

        finalLeft, finalRight = res
        return s[finalLeft : finalRight + 1] if resLen != float("infinity") else ""

    '''
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {},{}
        for c in t: 
            countT[c] = 1 + countT.get(c,0)
        have, need, l, res, resLen = 0, len(countT), 0, [-1,-1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        finalLeft, finalRight = res
        return s[finalLeft:finalRight+1] if resLen != float("infinity") else ""
    '''   