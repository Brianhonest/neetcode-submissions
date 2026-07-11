class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        empty_set = set()
        L=0
        for R in range(len(s)):
            while s[R] in empty_set:
                empty_set.remove(s[L])
                L+=1
            empty_set.add(s[R])
            max_length = max(max_length,R-L+1)
        return max_length