class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def recurse(curList, i):
            if i == len(nums):
                if len(curList)>1:
                    ans.add(tuple(curList))
                return
            recurse(curList, i +1)
            if not curList or curList[-1] <= nums[i]: 
                curList.append(nums[i])
                recurse(curList, i +1)
                curList.pop()
        
        recurse([], 0)
        return ans
            