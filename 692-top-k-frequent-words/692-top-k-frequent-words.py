class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = {}
        for word in words:
            if word in hashMap:
                hashMap[word] += 1
            else:
                hashMap[word] = 1
        
        heap = []
        for word, freq in hashMap.items():
            heap.append((-freq, word))
        
        heapq.heapify(heap) # O(n)
        
        res = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            res.append(word)
        
        return res
            