import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = [float('-inf'),float('inf')]
        m = len(nums)
        heap = []
        cur_max = float('-inf')
        for i in range(m):
            cur_max = max(cur_max,nums[i][0])
            heap.append((nums[i][0],i,0))
        heapq.heapify(heap)
        while len(heap)>0:
            ele,i,j = heapq.heappop(heap)
            if cur_max-ele<ans[1]-ans[0]:
                ans = [ele,cur_max]
            j+=1
            if j<=len(nums[i])-1:
                cur_max = max(cur_max,nums[i][j])
                heapq.heappush(heap,(nums[i][j],i,j))
            else:
                break
        return ans