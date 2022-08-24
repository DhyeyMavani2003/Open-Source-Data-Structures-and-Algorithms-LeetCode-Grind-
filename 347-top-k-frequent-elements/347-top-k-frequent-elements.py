class Solution:
    # Using a Heap
    '''
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)
    '''
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        
        topKHeap = []
        for n,f in count.items():
            topKHeap.append((-f, n))
        heapq.heapify(topKHeap)
        
        res = []
        for _ in range(k):
            negFreq, val = heapq.heappop(topKHeap)
            res.append(val)
            
        return res
    '''
    # Using Bucket Sort Algorithm
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    '''