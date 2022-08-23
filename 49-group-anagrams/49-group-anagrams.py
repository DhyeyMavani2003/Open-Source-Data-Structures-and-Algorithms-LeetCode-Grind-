class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # using defaultdict allows us to not worry about the empty edge cases
        result = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            # python doesn't allow list as key
            result[tuple(count)].append(s)
        
        return result.values()
    
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            if str(sorted(s)) in result:
                result[str(sorted(s))].append(s)
            else:
                result[str(sorted(s))] = [s]
        print(result.keys())
        return result.values()
        