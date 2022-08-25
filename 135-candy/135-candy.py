class Solution:
    def candy(self, ratings):
        
        # Concept - Just do what the problem is saying, we can 
        # fill our result array with one, now the first requirement
        # is fulfilled and for 2nd requirement, there will be 2 cases
        # 1 - Rating at i is greater than at i-1 --> Forward Pass
        # 2 - Rating at i is greater than i + 1 --> Backward Pass
        
        
        # Condition-1 Fulfilled as we gave 1 candy to everyone
        candies = [1] * len(ratings)
        
        # Calculate the candies needed to fulfill left condition     
        # We drop the 0th element as nothing is located left to it
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Calculate the candies needed to fulfill right condition  
        # We drop the last element as nothing is located right to it
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # Take the summation --> Minimum candies
        return sum(candies)
