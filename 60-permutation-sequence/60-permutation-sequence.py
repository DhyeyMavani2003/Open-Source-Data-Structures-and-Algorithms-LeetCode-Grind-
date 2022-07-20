class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        listFactorials, nums = [1], ['1']
        for i in range(1,n):
            listFactorials.append(listFactorials[i-1] * i)
            nums.append(str(i+1))
        
        k -= 1
        
        output = []
        for i in range(n-1, -1, -1):
            index = k // listFactorials[i]
            k -= index * listFactorials[i]
            output.append(nums[index])
            del nums[index]
            
        
            
        return ''.join(output)