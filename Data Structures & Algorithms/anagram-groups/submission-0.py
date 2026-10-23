from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #REACT
        """
        1. create a dictionary that stores words in the string in the sorted form and keep any other word that matches it when also sorted
        
        2. do this recursively until you have all the words in the array matched to a key

        3. return the sorted group of words in an array
        """
        result = []
        dictionary = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            dictionary[sorted_word].append(word)

        for key, value in dictionary.items():
            result.append(value)

        return result

            

        