class Solution:
    

    def ladderLength(self, start, end, words):
        LETTERS = set('abcdefghijklmnopqrstuvwxyz')
        words = set(words)
        visited = set()
        queue = [(start, 1)] # queue for BFS, which stores the word and distance

        while len(queue) > 0:
            word, length = queue.pop(0)
            if word == end:
                return length
            for i, char in enumerate(word):
                for letter in LETTERS:
                    if char != letter:
                        candidate = word[:i] + letter + word[i + 1:]
                        if candidate in words and candidate not in visited:
                            queue.append([candidate, length + 1])
                            visited.add(candidate)
        return 0