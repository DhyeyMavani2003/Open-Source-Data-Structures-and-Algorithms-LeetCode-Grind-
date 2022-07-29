class Solution:
    def longestValidParentheses(self, s):
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack += (i, paren),
        return result