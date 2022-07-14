class Solution:
    def removeStones(self, stones):
      f = {}
      islands = 0
      def find(x):
        nonlocal islands
        if x not in f:
          f[x] = x
          islands += 1
        if x != f[x]:
          f[x] = find(f[x])
        return f[x]

      def union(x, y):
        nonlocal islands
        x = find(x)
        y = find(y)
        if x != y:
          f[x] = y
          islands -= 1

      for [x, y] in stones:
        union(x, ~y)
      return len(stones) - islands