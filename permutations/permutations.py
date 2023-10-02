class Solution:
    def permute(self, nums):
        def recur(i, s, vis):
            if i>=0:
                vis[i] = True
                s += str(nums[i]) + ' '
            if len(s.split())==len(nums):
                res.add(s)
                return
            for j in range(len(nums)):
                if not vis[j]:
                    recur(j, s, copy.deepcopy(vis))
        
                    
        res = set()
        recur(-1, '', [False]*len(nums))
        return [[int(e) for e in s.split()] for s in res]


        def backtrack(first=1, current=[], level=0):
            if len(current) == k:
                ans.append(current[:])
            for i in range(first, n + 1):
                if len(current) < k:
                    current.append(i)
                    backtrack(i + 1, current, level + 1)
                    current.pop()

        ans = []
        backtrack()
        return ans