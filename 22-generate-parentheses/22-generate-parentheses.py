class Solution:
    
    # Neetcode solution
    def generateParenthesis(self, n):
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IIF oppen == closed == n
        
        stack, res = [], []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
    
    
    # CodePath solution
    def generateParenthesis(self, n: int) -> List[str]:
        
  
        def recursiveCall(result,str,open,close,n):
          if open == n and close == n:
            result.append(str)
            return
          if open < n:
            s = str + "("
            recursiveCall(result, s, open + 1, close, n)
          if close < open:
            s = str + ")"
            recursiveCall(result, s, open, close + 1, n)

        result = []
        recursiveCall(result,"",0,0,n)
        return result