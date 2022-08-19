class Solution:
    def reverseWords(self, s: str) -> str:
        wordsArray = s.split(" ")
        while "" in wordsArray:                  #it removes all the spaces from the s
            wordsArray.remove("")
        ans = ""
        for i in range(len(wordsArray) - 1, -1, -1):
            
            ans += wordsArray[i]
            if i != 0:
                ans += " "
                
        return ans
    '''
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")                #it splits the string s
        while "" in s:                  #it removes all the spaces from the s
            s.remove("")
        i,j = 0,len(s)-1                #taking two pointers i and j where i starts from 0th index and j starts from last index
        while i < j:
            s[i],s[j] = s[j],s[i]       #swapping done
            i+=1
            j-=1
        s = " ".join(s)                 
        return s
    '''