from heapq import heappush, heappop

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for i in range(min(len(nums1), k)):
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        ans = []
        i = j = 0
        while heap:
            _, i, j = heappop(heap)
            smallest_sum = heap[0][0] if heap else float('inf')
            while j < len(nums2) and nums1[i] + nums2[j] <= smallest_sum:
                ans.append([nums1[i], nums2[j]])
                j += 1
                k -= 1
                if k == 0:
                    return ans
            if j < len(nums2):
                heappush(heap, (nums1[i] + nums2[j], i, j))
        return ans