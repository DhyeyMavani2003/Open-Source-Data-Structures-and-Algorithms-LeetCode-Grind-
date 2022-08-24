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
    
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dic = defaultdict(list)
        for i in range(len(username)):
            dic[username[i]].append((website[i], timestamp[i]))
        for k, v in dic.items():
            v.sort(key=lambda x: x[1])
            new_v = []
            for web, time in v:
                new_v.append(web)
            dic[k] = new_v
        combs = defaultdict(list)
        for k, v in dic.items():
            self.get_all_combinations(v, combs, [], 0, k)
        max_size = -1
        for k, v in combs.items():
            max_size = max(max_size, len(v))
        max_list = []
        for k, v in combs.items():
            if len(v) == max_size and (not max_list or list(k) < max_list):
                max_list = list(k)
        return max_list
        
    def get_all_combinations(self, website, combs, comb, start, user):
        if user in combs[tuple(comb)]:
            return
        if len(comb) == 3:
            combs[tuple(comb)].append(user)
            return
        for i in range(start, len(website)):
            comb.append(website[i])
            self.get_all_combinations(website, combs, comb, i+1, user)
            comb.pop()
                        