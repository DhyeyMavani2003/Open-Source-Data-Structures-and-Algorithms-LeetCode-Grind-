class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        wordSet = set(wordList) # ["hot","dot","dog","lot","log","cog"]
        visitedSet = set() # [hot, dot, dog, cog]
        queue = [(beginWord,1)] # [(hit,1), (hot,2), (dot, 3), (dog, 4), (cog, 5) ]
        
        while queue:
            curWord, curLength = queue.pop(0)
            if curWord == endWord:
                return curLength
            for index, character in enumerate(curWord):
                for letter in alphabet:
                    if character != letter:
                        possibleWord = curWord[:index] + letter + curWord[index+1:]
                        if possibleWord in wordSet and possibleWord not in visitedSet:
                            queue.append((possibleWord, curLength + 1))
                            visitedSet.add(possibleWord)
        
        return 0