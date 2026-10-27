class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create an empty array for the integers according to frequecy, call it tally
        create an empty dictionary
        loop throught the integers in the array nums
        if integer not in dictionary, count is equal to zero
        add one count to the integer
        if integer already in the dictionary, add one count
        add the integers in the dictionary to tally according to the       frequency of their value
        return the length of tally from 0 to k-1
        """

        frequency = [[] for i in range(len(nums) + 1)]
        dictionary = {}

        for num in nums:
            if num not in dictionary:
                dictionary[num] = 0

            dictionary[num] += 1

        for num, c in dictionary.items():
            frequency[c].append(num)
        
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res
            



