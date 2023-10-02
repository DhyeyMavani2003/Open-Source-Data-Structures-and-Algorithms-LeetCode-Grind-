class Solution:
    def minWindow(self, s, t):
        if t == "": return ""
        target = {}
        for c in t:
            if c in target: target[c] += 1
            else:   target[c] = 1

        left = 0
        current = {}
        have, need = 0, len(target)
        res, resLen = [-1, -1], float("infinity")

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

    