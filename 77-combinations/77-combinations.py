class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
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