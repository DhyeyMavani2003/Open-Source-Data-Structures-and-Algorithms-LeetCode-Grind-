# precise condition judgement and backtracking
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.ans = []
        
        def find(offset, comb):
            if offset==len(S):
                if len(comb)>2:
                    self.ans = comb[:]
                return
            for i in range(offset, len(S) if S[offset]!='0' else offset+1):
                n_str = S[offset:i+1]
                n_int = int(n_str)
                if n_int > 2147483648:
                    return
                if len(comb)==0 or len(comb)==1:
                    find(i+1, comb+[n_int])
                elif n_int == comb[-1]+comb[-2]:
                    return find(i+1, comb+[n_int])
        
        find(0, [])
        return self.ans
