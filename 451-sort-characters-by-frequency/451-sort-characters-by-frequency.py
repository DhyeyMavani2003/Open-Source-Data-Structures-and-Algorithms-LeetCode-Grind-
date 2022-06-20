class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        
        pq = []
        for key in d:
            heapq.heappush(pq, (-d[key], key))
        
        ans = ''
        while pq:
            cnt, ch = heapq.heappop(pq)
            while cnt < 0:
                ans += ch
                cnt += 1
        
        return ans