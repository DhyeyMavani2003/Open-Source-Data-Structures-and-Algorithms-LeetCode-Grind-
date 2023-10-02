class Solution:
    def shortestDistance(self, words, word1, word2):
        i1, i2 = -1, -1
        minDistance = len(words)
        
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                minDistance = min(minDistance, abs(i1 - i2))
        
        return minDistance
