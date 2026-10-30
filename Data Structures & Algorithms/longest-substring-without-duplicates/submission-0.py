class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        left = 0
        longest = 0
        seen = ()

        FOR right from 0 to length of string -1:
            WHILE string[right] in seen:
                REMOVE string[left] from seen
                left = left + 1
            
            add string[right] to seen

            current_length = right - left + 1
            longest = max(current_length, longest)
        
        RETURN longest
        """
        left = 0
        longest = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1
            
            seen.add(s[right])

            current_length = right - left + 1
            longest = max(current_length, longest)

        return longest

