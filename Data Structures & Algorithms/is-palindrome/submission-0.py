class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","")
        s=list(s)
        new_str=""
        for i in s:
            if i.isalnum():
                new_str+=i

        return new_str == new_str[::-1]
