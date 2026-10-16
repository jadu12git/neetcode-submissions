class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we are going to use hashmap to save the current number and its index
        #loop through the numbers and keep the indice of the current number using the 
        #enumerate function
        #the target - the current number = the complement
        #if the complement is in the hashmap we return the indice of the complement
        #once the complement is found, return the indices of the number and the complement
        #the smallest index first

        seen = {}

        for i, num in enumerate (nums):
            comp = target - num
            if comp in seen:
                return[seen[comp], i]
            seen[num] = i

                
