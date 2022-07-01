class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        visited[0] = True
        stack = [0]
        count = 1
        
        while stack:
            nextRooms = rooms[stack.pop()]
            for k in nextRooms:
                if not visited[k]:
                    stack.append(k)
                    visited[k] = True
                    count += 1
                    
        return len(rooms) == count
                    
        