class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootX] = rootY
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootY] += 1
class Solution:
    def accountsMerge(self, accounts):
        uf = UnionFind()
        emailToID = {}
        emailToName = {}

        # Assign a unique ID to each email and initialize the union-find structure
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToID:
                    emailToID[email] = len(emailToID)
                    emailToName[email] = name
                    uf.parent[emailToID[email]] = emailToID[email]
                    uf.rank[emailToID[email]] = 0

        # Union the emails in each account
        for account in accounts:
            rootEmail = account[1]
            for email in account[2:]:
                uf.union(emailToID[rootEmail], emailToID[email])

        # Group the emails by their roots
        grouped = {}
        for email in emailToID:
            root = uf.find(emailToID[email])
            if root not in grouped:
                grouped[root] = []
            grouped[root].append(email)

        # Convert the groups back to the desired format
        result = []
        for emails in grouped.values():
            name = emailToName[emails[0]]
            result.append([name] + sorted(emails))

        return result
def accountsMerge(accounts):
        uf = UnionFind()
        emailToID = {}
        emailToName = {}

        # Assign a unique ID to each email and initialize the union-find structure
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToID:
                    emailToID[email] = len(emailToID)
                    emailToName[email] = name
                    uf.parent[emailToID[email]] = emailToID[email]
                    uf.rank[emailToID[email]] = 0

        # Union the emails in each account
        for account in accounts:
            rootEmail = account[1]
            for email in account[2:]:
                uf.union(emailToID[rootEmail], emailToID[email])

        # Group the emails by their roots
        grouped = {}
        for email in emailToID:
            root = uf.find(emailToID[email])
            if root not in grouped:
                grouped[root] = []
            grouped[root].append(email)

        # Convert the groups back to the desired format
        result = []
        for emails in grouped.values():
            name = emailToName[emails[0]]
            result.append([name] + sorted(emails))

        return result
# Test the function
accounts1 = [["John","johnsmith@mail.com","john_newyork@mail.com"],
             ["John","johnsmith@mail.com","john00@mail.com"],
             ["Mary","mary@mail.com"],
             ["John","johnnybravo@mail.com"]]
accounts2 = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
             ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
             ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
             ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
             ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

result1 = accountsMerge(accounts1)
result2 = accountsMerge(accounts2)

result1, result2
