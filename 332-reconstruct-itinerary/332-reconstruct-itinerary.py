class Solution:
    def findItinerary(self, tickets):
        ticket_graph = defaultdict(list)
        sorted_tickets = sorted(tickets)
        for start, end in sorted_tickets:
            ticket_graph[start].append(end)
        route = []
        self.visit('JFK', ticket_graph, route)
        route.reverse()
        return route


    def visit(self, airport, ticket_graph, route):
        while ticket_graph[airport]:
            next_city = ticket_graph[airport].pop(0)
            self.visit(next_city, ticket_graph, route)
        route.append(airport)