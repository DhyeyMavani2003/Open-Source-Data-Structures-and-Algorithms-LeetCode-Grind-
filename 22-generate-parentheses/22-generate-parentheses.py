class Solution:
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