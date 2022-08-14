class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        fmap = {}
        for element in arr1:
            if element in fmap:
                fmap[element] += 1
            else:
                fmap[element] = 1
        
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            element = arr2[j]
            frequency = fmap[element]
            fmap.pop(element)
            for _ in range(frequency):
                arr1[i] = element
                i += 1
            j += 1
        for e in range(1001):
            if e in fmap:
                f = fmap[e]
                for _ in range(f):
                    arr1[i] = e
                    i += 1
        return arr1
            
            
            