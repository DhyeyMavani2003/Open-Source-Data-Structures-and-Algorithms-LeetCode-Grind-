class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        tuples = []
        for i in range(len(username)):
            tuples.append([timestamp[i], username[i], website[i]])
        
        tuples.sort()
        currentUsername = tuples[0][1]
        
        patternsMap = {}
        res = []
        for t in tuples:
            if t[1] == currentUsername:
                res.append(t[2])
            else:
                if str(res) in patternsMap:
                    patternsMap[str(res)] += 1
                else:
                    patternsMap[str(res)] = 1
                res = []
                currentUsername = t[1]
                res.append(t[2])
        if str(res) in patternsMap:
            patternsMap[str(res)] += 1
        else:
            patternsMap[str(res)] = 1
        
        reqPattern, maxFreq = "", 0
        for pattern in patternsMap:
            if patternsMap[pattern] > maxFreq:
                reqPattern = pattern
        
        return reqPattern

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        username = [x for _,x in sorted(zip(timestamp, username))]
        website = [x for _,x in sorted(zip(timestamp, website))]
        
        patterns = collections.defaultdict(list)
        for i,user in enumerate(username):
            patterns[user].append(website[i])
                        
        scores = collections.defaultdict(set)
        for user, pattern in patterns.items():
            if len(pattern)<3:
                continue
            for i in range(len(pattern)-2):
                for j in range(i+1, len(pattern)-1):
                    for k in range(j+1, len(pattern)):
                        scores[(pattern[i],pattern[j],pattern[k])].add(user)
        
        scores = sorted(scores.items(), key=lambda y:(-len(y[1]), y[0]))
        
        return list(scores[0][0])
                        