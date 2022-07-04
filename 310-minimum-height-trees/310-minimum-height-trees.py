
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: 
            return [0]
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        # Fetch the leaves; the leaves are nodes with only one edge
        leaves = [key for key, val in graph.items() if len(val) == 1]

        # Keep removing leaves until there are only two or fewer nodes left
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1: 
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves