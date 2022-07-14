class Solution:
    def calcEquation(self, equations, values, queries):
      graph = self.buildGraph(equations, values)
      results = []
      for query in queries:
        result = self.getPathWeight(query[0], query[1], graph, set())
        results.append(result)

      return results

    def getPathWeight(self, start, end, graph, visited):
      if start not in graph:
        return -1

      if end in graph[start]:
        return graph[start][end]

      visited.add(start)

      for neighbor in graph[start]:
        if neighbor not in visited:
          productWeight = self.getPathWeight(neighbor, end, graph, visited)
          if productWeight != -1:
                return graph[start][neighbor] * productWeight

      return -1

    def buildGraph(self, equations, values):
      graph = {}

      for equation, value in zip(equations, values):
        u, v = equation[0], equation[1]
        if u not in graph: graph[u] = {}
        graph[u][v] = value
        if v not in graph: graph[v] = {}
        graph[v][u] = 1 / value

      return graph