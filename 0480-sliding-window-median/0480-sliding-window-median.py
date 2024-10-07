
from heapq import heappush, heappop

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        max_heap, min_heap = [], []
        removed_set = set()
        self.max_heap_size, self.min_heap_size = 0, 0

        for i, num in enumerate(nums):
            self._add_number(max_heap, min_heap, num, i, removed_set)

            if i < k - 1:
                continue 
            
            if i > k - 1:
                self._delete_number(max_heap, min_heap, removed_set, nums[i - k], i - k)
            
            self._balance(max_heap, min_heap, removed_set)
            self._pop_removed_items(max_heap, min_heap, removed_set)
            if self.max_heap_size == self.min_heap_size + 1:
                median = -max_heap[0][0]
            else:
                median = (-max_heap[0][0] + min_heap[0][0]) / 2
            result.append(median)
        
        return result 
    

    def _add_number(self, max_heap, min_heap, number, index, removed_set):
        self._pop_removed_items(max_heap, min_heap, removed_set)
        if not max_heap or (number, index) <= (-max_heap[0][0], -max_heap[0][1]):
            heappush(max_heap, (-number, -index))
            self.max_heap_size += 1
        else:
            heappush(min_heap, (number, index))
            self.min_heap_size += 1 
    

    def _delete_number(self, max_heap, min_heap, removed_set, number, index):
        # it's guaranteed that max_heap is not empty
        self._pop_removed_items(max_heap, min_heap, removed_set)
        if (number, index) <= (-max_heap[0][0], -max_heap[0][1]):
            removed_set.add((-number, -index))
            self.max_heap_size -= 1 
        else:
            removed_set.add((number, index))
            self.min_heap_size -= 1 
    

    def _balance(self, max_heap, min_heap, removed_set):
        # at most one iteration in one of the while loops will be executed
        while self.max_heap_size > self.min_heap_size + 1:
            self._pop_removed_items(max_heap, min_heap, removed_set)

            negative_number, negative_index = heappop(max_heap)
            self.max_heap_size -= 1

            heappush(min_heap, (-negative_number, -negative_index))
            self.min_heap_size += 1 

        while self.max_heap_size < self.min_heap_size:
            self._pop_removed_items(max_heap, min_heap, removed_set)

            number, index = heappop(min_heap)
            self.min_heap_size -= 1 

            heappush(max_heap, (-number, -index))
            self.max_heap_size += 1 
    

    def _pop_removed_items(self, max_heap, min_heap, removed_set):
        while max_heap and max_heap[0] in removed_set:
            heappop(max_heap)
        
        while min_heap and min_heap[0] in removed_set:
            heappop(min_heap)