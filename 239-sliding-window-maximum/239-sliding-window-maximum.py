class Solution:
    
    # monotonic decreasing queue
    def maxSlidingWindow(self, nums, k):
        output = []
        q = collections.deque() # index
        l, r = 0, 0
        
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output
            
            
    
    # my heap though process (not correct so far)
    def maxSlidingWindo(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        for i in range(k):
            maxHeap.append(-nums[i])
        
        heapq.heapify(maxHeap) # O(k)
        initialMax = -maxHeap[0]
        maxes = []
        maxes.append(initialMax)
        
        left, right = 0, k
        while right < len(nums):
            updatedMaxHeap = []
            for e in maxHeap:
                if e != -nums[left]:
                    updatedMaxHeap.append(e)
            heapq.heapify(updatedMaxHeap)
            
            heapq.heappush(updatedMaxHeap, -nums[right])
            right += 1
            left += 1
            curMax = -updatedMaxHeap[0]
            maxes.append(curMax)
        
        return maxes
            
            