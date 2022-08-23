class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexes = {}
        
        for i, c in enumerate(s):
            lastIndexes[c] = i
        
        result = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if lastIndexes[c] > end:
                end = lastIndexes[c]
            if i == end:
                result.append(size)
                size = 0
        
        return result